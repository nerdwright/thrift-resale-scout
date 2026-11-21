#!/usr/bin/env python3
"""Build the Claude Project instructions paste from the plugin skill.

The plugin (skills/thrifting-assistant) is the single source of truth.
This flattens SKILL.md + references/*.md into one Markdown file that can be
pasted into a Claude Project's custom instructions.

Usage:  python tools/build_project_instructions.py
Output: instructions/thrifting-assistant-project.md

Personal settings (preferred browser, device IDs) never go in this repo.
Append them by hand below the generated text in your own Project.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "thrifting-assistant"
OUT = ROOT / "instructions" / "thrifting-assistant-project.md"

# Order the references appear in the flattened file, with the section name
# used when SKILL.md points at them.
REFS = [
    ("haul-mode.md", "Haul mode"),
    ("identify.md", "Identify the item"),
    ("price-and-fees.md", "Price, fees, and verdict"),
    ("fakes-and-niche.md", "Fakes and collector value"),
    ("quick-links.md", "Quick links"),
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.index("\n---", 3)
        return text[end + 4 :].lstrip("\n")
    return text


def demote(text: str) -> str:
    """Make a reference file's headings one level deeper (# -> ##)."""
    return re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", text, flags=re.M)


def main() -> None:
    version = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text("utf-8"))["version"]
    body = strip_frontmatter((SKILL / "SKILL.md").read_text("utf-8"))

    # Drop the "Read these references" list; everything is inline here.
    body = re.sub(r"Read these references as you need them:\n\n(?:- .*\n)+\n", "", body)
    for fname, title in REFS:
        body = body.replace(f"`references/{fname}`", f"the {title} section below")

    parts = [
        f"<!-- Thrifting Assistant v{version} — generated from the plugin by "
        "tools/build_project_instructions.py. Paste everything below this line "
        "into a Claude Project's instructions. Add any personal settings "
        "(preferred browser) after the generated text. -->\n\n",
        body.rstrip() + "\n",
    ]
    for fname, title in REFS:
        text = (SKILL / "references" / fname).read_text("utf-8")
        for other, other_title in REFS:
            text = text.replace(f"`references/{other}`", f"the {other_title} section")
        parts.append("\n---\n\n" + demote(text).rstrip() + "\n")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("".join(parts), "utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} (v{version}, {OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
