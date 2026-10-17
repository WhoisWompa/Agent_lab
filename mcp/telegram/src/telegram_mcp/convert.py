"""Turning what comes in and goes out into the right shapes: dates from text, Telethon dicts to JSON."""

import base64
from datetime import datetime


def parse(text):
    """'2026-10-01' or '2026-10-01 18:00' (local time) as an aware datetime; None or '' stays None."""
    if text is None or text == "":
        return None
    try:
        return aware(datetime.fromisoformat(text))
    except ValueError:
        raise ValueError(f"cannot read date {text!r}: use YYYY-MM-DD or 'YYYY-MM-DD HH:MM'")


def aware(when):
    """A naive datetime read as local time; an aware one unchanged; None stays None."""
    if when is None:
        return None
    if when.tzinfo is None or when.tzinfo.utcoffset(when) is None:
        return when.astimezone()
    return when


def plain(obj):
    """Telethon's to_dict() made JSON-safe: datetimes to ISO strings, bytes to base64, recursively."""
    if isinstance(obj, dict):
        return {str(k): plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [plain(v) for v in obj]
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, (bytes, bytearray)):
        return base64.b64encode(bytes(obj)).decode("ascii")
    return obj
