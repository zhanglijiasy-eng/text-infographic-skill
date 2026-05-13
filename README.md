# Text Infographic Skill

Turn a paragraph, lesson note, article section, or Chinese explainer text into a structured hand-drawn teaching infographic.

This skill recreates the visual system used in the reference PDF style:

- White or warm-white teaching-board canvas
- Bold handwritten Chinese title
- Rounded cards and color-coded panels
- Red emphasis for the main conclusion
- Simple line icons and arrows
- Bottom summary band
- Short, readable Chinese labels instead of pasted paragraphs

## Use

Ask Codex or a compatible skill runner:

```text
Use the text-infographic skill to turn this paragraph into a teaching infographic:

Agent 不只是聊天机器人，而是能调用工具、操作文件、运行代码、自动完成复杂任务的 AI 助手。
```

For long source text, generate a stable image prompt first:

```bash
python scripts/build_prompt.py --text "你的输入文字" --layout system-map
python scripts/build_prompt.py --file input.txt --layout dense-cheatsheet
```

Layouts:

- `explainer-flow`: problem -> mechanism -> outcome
- `system-map`: components, architecture, frameworks
- `comparison`: A vs B, old vs new, Chatbot vs Agent
- `dense-cheatsheet`: compact grid for longer lessons

## Install

Copy this folder into your Codex skills directory:

```bash
~/.codex/skills/text-infographic
```

Then ask for `text-infographic` when transforming text into an infographic.

## Notes

The skill describes a reusable style system. It should not copy any specific reference image verbatim.
