"""Reading Telegram through an open client: the list of chats, and one chat's messages over a window."""

from .convert import aware, plain


async def list_chats(client, only=None, exclude=None):
    """The user's chats, newest activity first. `only` keeps these names, `exclude` drops them.

    Returns:
        One dict per chat: {"id", "name", "kind" (user|group|channel), "unread", "last_message" (ISO)}.
    """
    out = []
    async for d in client.iter_dialogs():
        if only is not None and d.name not in only:
            continue
        if exclude is not None and d.name in exclude:
            continue
        out.append({
            "id": d.id,
            "name": d.name,
            "kind": "user" if d.is_user else "group" if d.is_group else "channel",
            "unread": d.unread_count,
            "last_message": d.date.isoformat() if d.date else None,
        })
    return out


async def read_messages(client, chat, start=None, end=None, limit=None):
    """Every message in the chat named `chat` sent between `start` and `end`, oldest first.

    `start` and `end` are datetimes (naive = local time) or None for unbounded.
    `limit` keeps only the newest N of the window.

    Returns:
        {"chat": full chat record, "window": {"start", "end"} as ISO strings or None,
         "users": {sender id: full user record}, "messages": [full Telethon message dicts]}.
        Raises ValueError if no chat has that name.
    """
    dialog = None
    async for d in client.iter_dialogs():
        if d.name == chat:
            dialog = d
            break
    if dialog is None:
        raise ValueError(f"no chat named {chat!r}")

    start, end = aware(start), aware(end)
    users, out = {}, []
    async for m in client.iter_messages(dialog.entity, offset_date=end):
        if limit is not None and len(out) >= limit:
            break
        if start is not None and m.date < start:
            break
        if m.sender_id is not None and m.sender_id not in users:
            sender = await m.get_sender()
            users[m.sender_id] = plain(sender.to_dict()) if sender is not None else None
        out.append(plain(m.to_dict()))
    out.reverse()

    return {
        "chat": plain(dialog.entity.to_dict()),
        "window": {"start": start.isoformat() if start else None,
                   "end": end.isoformat() if end else None},
        "users": users,
        "messages": out,
    }
