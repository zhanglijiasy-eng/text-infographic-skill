---
name: text-infographic
description: Generate structured teaching infographics from a paragraph, article section, lesson note, Chinese explainer text, or slide-style content. Use when the user asks to turn text into an information graphic, visual explanation, hand-drawn infographic, whiteboard diagram, course graphic, Xiaohongshu/Bilibili-style knowledge card, or a visual matching the "智能体应用与skill开发实战" PDF style.
---

# Text Infographic

## Overview

Turn source text into a single polished teaching infographic with the same visual grammar as the reference deck: white canvas, hand-drawn black type, red emphasis, rounded outlined cards, arrows, linear icons, section tabs, and a final summary band.

Use image generation for the final artifact. Do not answer with only a textual summary unless the user explicitly asks for a prompt instead of an image.

## Quick Workflow

1. Read the user's source text and identify one teachable idea, not every sentence.
2. Extract 3-6 information units: definition, contrast, process, components, examples, warning, conclusion.
3. Choose a layout from `references/style-guide.md`:
   - `explainer-flow` for cause/effect or before/after content.
   - `system-map` for components and relationships.
   - `comparison` for two modes, tools, options, or eras.
   - `dense-cheatsheet` for long text with many concepts.
4. Build an image prompt with `scripts/build_prompt.py` when the text is longer than a few lines or when consistency matters.
5. Generate a 3:2 landscape infographic by default. Use portrait only when the user asks for mobile/poster output or the content is a sequential checklist.
6. After generation, inspect the image for legibility, missing Chinese text, broken hierarchy, and over-crowding. Regenerate with fewer words if needed.

## Prompt Construction

Always include these constraints in the image prompt:

- White or very light warm-white background, no dark hero background.
- 1536x1024-style 3:2 landscape teaching board unless otherwise requested.
- Hand-drawn educational diagram style, clean black marker lines, rounded boxes, thin red/blue/green/orange borders.
- Large bold handwritten Chinese title at top left.
- Red accent for the key conclusion, critical verb, or highest-leverage phrase.
- Modular layout with 3-5 cards or panels, arrows between panels, and a bottom summary strip.
- Simple line icons that match the nouns in the text; use small illustrative icons, not decorative stock art.
- Clear Chinese labels, short phrases, no tiny paragraphs, no illegible microtext.

Never ask the image model to copy a PDF page. Ask it to recreate the style system while making an original infographic for the new text.

## Content Compression Rules

Compress before drawing:

- Title: 4-12 Chinese characters or a short mixed Chinese/English phrase.
- Subtitle: one short sentence only when needed.
- Section labels: 2-6 characters each.
- Card body: 1-3 bullets per card, each under 12 Chinese characters when possible.
- Final summary: one strong sentence, with the key phrase in red.
- If source text is long, prioritize structure over completeness. The infographic should teach, not transcribe.

## Quality Bar

The output should look like a teacher drew a precise whiteboard explainer and then polished it digitally:

- The eye can follow the path in under 3 seconds.
- Every card has a reason to exist.
- Icons reinforce meaning rather than filling space.
- Red marks the thesis, not random decoration.
- The bottom band closes the idea with a memorable takeaway.
- The image contains no invented brand logos unless the source text names them.

## Resources

- Read `references/style-guide.md` for layout recipes, visual tokens, and anti-patterns.
- Run `scripts/build_prompt.py` to turn source text into a ready-to-use image prompt:

```bash
python scripts/build_prompt.py --text "你的输入文字"
python scripts/build_prompt.py --file input.txt --layout system-map --orientation landscape
```
