import sys, os, glob, json
from pypdf import PdfReader
src, out = sys.argv[1], sys.argv[2]
rows=[]
for p in sorted(glob.glob(os.path.join(src,'**','*.pdf'), recursive=True)):
    rel=os.path.relpath(p, src)
    try:
        r=PdfReader(p); pages=len(r.pages)
        text="\n\n".join((pg.extract_text() or "") for pg in r.pages)
    except Exception as e:
        rows.append({"pdf":rel,"error":str(e)}); continue
    dst=os.path.join(out, os.path.splitext(rel)[0]+".txt")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst,"w",encoding="utf-8",errors="replace").write(text)
    rows.append({"pdf":rel,"pages":pages,"chars":len(text),"est_tokens":len(text)//4,"txt":dst})
json.dump(rows, open(os.path.join(out,"index.json"),"w"), indent=1)
ok=[r for r in rows if "pages" in r]
print("papers",len(ok),"errors",len(rows)-len(ok))
print("total pages",sum(r["pages"] for r in ok),"total est tokens",sum(r["est_tokens"] for r in ok))
print("median tokens",sorted(r["est_tokens"] for r in ok)[len(ok)//2],"max",max(r["est_tokens"] for r in ok))
for r in rows:
    if "error" in r: print("ERR",r)
