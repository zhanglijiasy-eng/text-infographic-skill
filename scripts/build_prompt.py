#!/usr/bin/env python3
"""Build a stable image-generation prompt for the text-infographic skill."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path


LAYOUTS = {
    "explainer-flow": "Use a left-to-right explainer flow: problem card -> mechanism card -> outcome card, connected by red arrows, with a wide dashed summary band at the bottom.",
    "system-map": "Use a system map layout with multiple color-coded rounded panels, numbered tabs, icons inside each panel, and a final bottom summary strip.",
    "comparison": "Use a two-column comparison layout with a small VS badge, blue for one side and red for the recommended side, plus a bottom recommendation band.",
    "dense-cheatsheet": "Use a dense cheat-sheet layout: 4-6 compact cards in a grid, each with a colored tab and icon, plus a full-width footer summary.",
}


def read_source(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8").strip()
    if args.text:
        return args.text.strip()
    raise SystemExit("Provide --text or --file.")


def build_prompt(source: str, layout: str, orientation: str) -> str:
    aspect = "3:2 landscape, similar to 1536 x 1024" if orientation == "landscape" else "mobile-friendly portrait, similar to 1024 x 1536"
    layout_text = LAYOUTS[layout]
    return textwrap.dedent(
        f"""
        Create a single Chinese teaching infographic in the "智能体应用与skill开发实战" reference style.

        Source idea:
        {source}

        Layout:
        {layout_text}

        Visual style:
        White or warm-white background, {aspect}; clean hand-drawn educational whiteboard infographic; huge bold handwritten Chinese title at top-left; black marker-like text; thin rounded cards; red accent for the key conclusion; optional blue/green/orange section tabs; simple line icons that match the nouns; arrows between ideas; dashed bottom summary band; soft translucent red/blue/green fills; balanced spacing and generous margins.

        Content rules:
        Compress the source into one title, 3-5 short sections, and one final summary sentence. Use clear Chinese labels. Keep all text large and readable. Use short bullets instead of paragraphs. Highlight only the highest-leverage phrase in red. Do not add unrelated facts. Do not copy any existing reference image verbatim.

        Output:
        One polished infographic only, no surrounding explanation.
        """
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", help="Source text to transform.")
    parser.add_argument("--file", help="UTF-8 text file containing the source text.")
    parser.add_argument("--layout", choices=sorted(LAYOUTS), default="explainer-flow")
    parser.add_argument("--orientation", choices=["landscape", "portrait"], default="landscape")
    args = parser.parse_args()
    print(build_prompt(read_source(args), args.layout, args.orientation))


if __name__ == "__main__":
    main()
