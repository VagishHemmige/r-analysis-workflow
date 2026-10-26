"""Check the plugin before release.

- Every relative link in the plugin's Markdown files resolves, and every
  #anchor matches a heading in its target file.
- The two manifests (plugin.json for ChatGPT, .claude-plugin/plugin.json for
  Claude) agree on name, version, description, author, license and keywords.

Run from the plugin root: python3 check_links.py
Links inside code fences, and links in assets/starter/ (which point within a
future project), are skipped.
"""
import json, os, re, sys

LINK = re.compile(r"\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(`{3,}).*?^\1\s*$", re.S | re.M)
HEAD = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.M)


def slug(text):
    text = re.sub(r"[`*_]", "", text.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path):
    body = FENCE.sub("", open(path, encoding="utf-8").read())
    return {slug(h) for h in HEAD.findall(body)}


bad = []
for d, _, files in os.walk("."):
    if d.startswith("./assets/starter"):
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        p = os.path.join(d, f)
        for t in LINK.findall(FENCE.sub("", open(p, encoding="utf-8").read())):
            if re.match(r"^[a-z]+:", t) or t.startswith("../../issues"):
                continue
            target, _, anchor = t.partition("#")
            path = os.path.normpath(os.path.join(d, target)) if target else p
            if not os.path.exists(path):
                bad.append(f"{p} -> {t} (file not found)")
            elif anchor and path.endswith(".md") and anchor not in anchors(path):
                bad.append(f"{p} -> {t} (no such heading)")

if os.path.exists(".claude-plugin/plugin.json"):
    a = json.load(open("plugin.json", encoding="utf-8"))
    b = json.load(open(".claude-plugin/plugin.json", encoding="utf-8"))
    for k in ("name", "version", "description", "author", "license", "keywords"):
        if a.get(k) != b.get(k):
            bad.append(f"manifests differ on {k}: plugin.json and .claude-plugin/plugin.json")
if bad:
    sys.exit("Problems:\n  " + "\n  ".join(bad))
print("All links and anchors resolve; manifests agree.")
