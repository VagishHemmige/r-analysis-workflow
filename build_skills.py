"""Copy the shared files each skill uses into that skill's folder.

The shared files have one source: references/ and assets/ at the plugin root.
Edit them there, never inside a skill. ChatGPT's cloud skills package only a
skill's own folder, so each skill also carries generated copies of the shared
files it reaches, at the same relative paths (skills/<skill>/references/...,
skills/<skill>/assets/...). Links in SKILL.md point inside the skill
(references/x.md), and links between shared files stay valid in the copies.

A skill reaches a file when its SKILL.md links to it, or a reached Markdown
file links to it. A link to a folder brings the whole folder (as
initialize-analysis does with assets/starter/, since a project is set up from
all of it).

The plugin is the plugin/ folder of the repository; this script works there
wherever it is run from. Run it after changing a SKILL.md, references/ or assets/:
    python3 build_skills.py           rebuild every skill's copies
    python3 build_skills.py --check   fail if any copy is missing or stale
Commit the regenerated copies with the change. check_links.py runs the check.
"""
import filecmp, os, re, shutil, sys, tempfile

PLUGIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugin")

LINK = re.compile(r"\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(`{3,}).*?^\1\s*$", re.S | re.M)
SHARED = ("references", "assets")


def links(path):
    """Relative link targets in a Markdown file, outside code fences and inline code."""
    body = FENCE.sub("", open(path, encoding="utf-8").read())
    body = re.sub(r"`[^`\n]*`", "", body)
    for t in LINK.findall(body):
        t = t.split("#")[0]
        if t and not re.match(r"^[a-z]+:", t):
            yield t


def reached(skill):
    """Shared files (paths from the plugin root) that a skill reaches."""
    # Paths are as seen from inside the skill folder, which mirrors the root.
    seen, read, todo = set(), set(), [os.path.join("skills", skill, "SKILL.md")]
    while todo:
        src = todo.pop()
        read.add(src)
        here = "" if src.startswith("skills" + os.sep) else os.path.dirname(src)
        for t in links(src):
            q = os.path.normpath(os.path.join(here, t))
            if q.split(os.sep)[0] not in SHARED:
                continue
            if os.path.isdir(q):
                for d, _, fs in os.walk(q):
                    seen.update(os.path.join(d, f) for f in fs)
                continue
            if not os.path.isfile(q):
                sys.exit(f"{src} links to {t}, but {q} does not exist at the plugin root")
            seen.add(q)
            if q.endswith(".md") and q not in read:
                todo.append(q)
    return sorted(seen)


def build(dest_root):
    for skill in sorted(os.listdir("skills")):
        dest = os.path.join(dest_root, "skills", skill)
        for d in SHARED:
            shutil.rmtree(os.path.join(dest, d), ignore_errors=True)
        for f in reached(skill):
            os.makedirs(os.path.join(dest, os.path.dirname(f)), exist_ok=True)
            shutil.copy2(f, os.path.join(dest, f))


def stale():
    """Differences between the committed copies and a fresh build."""
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp)
        for skill in sorted(os.listdir("skills")):
            for d in SHARED:
                a, b = os.path.join("skills", skill, d), os.path.join(tmp, "skills", skill, d)
                files = set()
                for root in (a, b):
                    for r, _, fs in os.walk(root):
                        files.update(os.path.relpath(os.path.join(r, f), root) for f in fs)
                for f in sorted(files):
                    x, y = os.path.join(a, f), os.path.join(b, f)
                    if not os.path.exists(y):
                        problems.append(f"{x} is not reached by the skill; rebuild removes it")
                    elif not os.path.exists(x):
                        problems.append(f"{x} is missing")
                    elif not filecmp.cmp(x, y, shallow=False):
                        problems.append(f"{x} differs from {d}/{f} at the plugin root")
    return problems


if __name__ == "__main__":
    os.chdir(PLUGIN)
    if "--check" in sys.argv:
        p = stale()
        if p:
            sys.exit("Skill copies are out of date; run python3 build_skills.py:\n  " + "\n  ".join(p))
        print("Skill copies match the shared files.")
    else:
        build(".")
        for skill in sorted(os.listdir("skills")):
            print(f"{skill}: {len(reached(skill))} shared files")
