# Text Infographic Style Guide

## Visual DNA

The reference style is a clean Chinese teaching infographic:

- Canvas: mostly white, subtle paper warmth, wide margins.
- Aspect: 3:2 landscape by default, often 1536 x 1024.
- Typography: bold handwritten/marker-like Chinese title, casual hand lettering for English words such as `Agent`, `Skill`, `Workbuddy`, `Prompt`.
- Line work: black sketch lines plus thin colored outlines.
- Palette: black text, red emphasis, cobalt blue, emerald green, orange/yellow highlights, occasional soft pink/blue/green translucent fills.
- Components: rounded rectangles, dashed summary boxes, section tabs, arrows, icon rows, comparison panels, callout notes.
- Icons: simple line icons for document, folder, browser, database, robot, target, light bulb, shield, workflow, code, chart, phone, cloud, lock.
- Mood: educational, structured, friendly, hand-drawn but not messy.

## Layout Recipes

### explainer-flow

Use for "why", "how", causality, and transformation.

Structure:

1. Top-left title.
2. Left card: current problem / old way / examples.
3. Center card: key mechanism with a red-highlighted thesis.
4. Right card: resulting actions / capabilities / new way.
5. Bottom dashed band: objects affected or final conclusion.

Prompt phrase:

`Use a left-to-right explainer flow: problem card -> mechanism card -> outcome card, connected by red arrows, with a wide dashed summary band at the bottom.`

### system-map

Use for components, architecture, product explanation, frameworks.

Structure:

1. Large title at top.
2. 3-4 colored section panels with tab labels.
3. Each panel contains icon + 2-4 short labels.
4. Bottom strip summarizes the system's value.

Prompt phrase:

`Use a system map layout with multiple color-coded rounded panels, numbered tabs, icons inside each panel, and a final bottom summary strip.`

### comparison

Use for A vs B, modes, options, generations, Chatbot vs Agent.

Structure:

1. Two large side-by-side cards with different border colors.
2. A central `VS` badge or arrow.
3. Each side has icon, 3 short bullets, and a tiny example.
4. Bottom band states which option is recommended or when to use each.

Prompt phrase:

`Use a two-column comparison layout with a small VS badge, blue for one side and red for the recommended side, plus a bottom recommendation band.`

### dense-cheatsheet

Use for long lessons with many related concepts.

Structure:

1. Big top-left title.
2. 4-6 small cards arranged in a grid.
3. Each card has colored tab, icon, and 2-3 bullets.
4. Footer has a trophy/target/lightbulb icon and a one-sentence summary.

Prompt phrase:

`Use a dense cheat-sheet layout: 4-6 compact cards in a grid, each with a colored tab and icon, plus a full-width footer summary.`

## Text Hierarchy

Use this hierarchy:

- H1: huge black handwritten title, top-left.
- Section tab: white text on solid red/blue/green/orange rounded pill.
- Card header: black or colored, 1 short line.
- Body: short black phrases, occasional red keywords.
- Summary: black sentence with the main conclusion in red.

Keep Chinese text large and legible. Avoid long paragraphs. Replace prose with labels and bullets.

## Common Motifs

Use these motifs when relevant:

- `问题 -> 原因 -> 解决方案`
- `输入 -> 处理 -> 输出`
- `旧方式 -> 新方式`
- `工具层 -> 模型层 -> 本地执行`
- `一次对话 -> 固化流程 -> 可复用能力`
- `普通用户 -> Agent -> 结果`
- `SOP -> Skill -> 自动化任务`

## Anti-Patterns

Avoid:

- Photorealistic stock illustration.
- Dark backgrounds.
- Decorative gradient blobs.
- Dense paragraphs pasted into cards.
- Tiny unreadable Chinese text.
- Random icons that do not map to text.
- Too many colors in one panel.
- Corporate SaaS dashboard style.
- Comic/manga style.
- Copying an existing reference image verbatim.

## Image Generation Prompt Template

```text
Create a single Chinese teaching infographic in the reference style.

Source idea:
{source_text}

Layout:
{layout_recipe}

Visual style:
White background, 3:2 landscape, clean hand-drawn educational whiteboard infographic, bold handwritten Chinese title at top-left, black marker text, thin rounded cards, red accent for the key conclusion, simple line icons, arrows, dashed summary band, soft translucent color fills, balanced spacing.

Content rules:
Compress the text into a title, 3-5 short sections, and one final summary sentence. Use clear Chinese labels. Keep all text large and readable. Do not include long paragraphs. Do not add unrelated facts.

Output:
One polished infographic only, no surrounding explanation.
```
