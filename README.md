# Photo Style Prompts

A library of **21 photo-editing styles**, each written as a complete prompt you can paste into any
AI image tool with your own photo attached.

Open **`style-picker.html`** in a browser → filter → copy a prompt → paste it into ChatGPT, Gemini,
Grok or Arena with your photo.

---

## 🤖 If you are an AI assistant

You've been given this repository to continue work on it. **Read `AGENT.md` first** — it has the
prompt structure, the rules learned the hard way, and what's already done.

---

## What's here

| Path | What it is |
|---|---|
| `style-picker.html` | **Start here.** Visual picker — filter by type and mood, preview, copy. |
| `prompts/styles.json` | All 21 styles as data. The source of truth. |
| `AGENT.md` | Brief for any AI assistant continuing this work. |
| `GITHUB-SETUP.md` | How to publish this and hand it to a new AI in one line. |
| `ig-effects-recreated.md` | Full knowledge base — every prompt plus a debug table of failures and fixes. |
| `REFERENCE-ANALYSIS.md` | Analysis of the 13 reference images behind the styles. |
| `tools/` | Python scripts for styles that need no AI at all. |
| `photos/` | The two source photos. |
| `examples/` | Best results so far — the quality bar. |
| `refs/` | Original reference images. |

## The three style types

- **A · Single-image** — one photo, one prompt. Paste and go.
- **B · Multi-panel** — stacked panels. Either render 3–4 images and stitch, or use
  `tools/panels.py` to build panels from crops of a single photo.
- **C · Layered** — collage, torn bands, overlays. One photo, layers stacked on itself.

## Styles that need no AI

Some styles only rearrange pixels that already exist, so a script does them perfectly, free, and
without any risk of altering the face:

```bash
pip install pillow numpy
python3 tools/template9.py    # sepia + eye band + sunflower stickers
python3 tools/panels.py       # multi-panel stacks from a single photo
```

## Using a prompt

1. Open `style-picker.html`
2. Choose Photo A or Photo B — prompts update with that photo's description
3. Copy the prompt
4. Paste into your AI image tool **with the photo attached**

Using your own photo? Replace the `PRESERVE EXACTLY:` section with a description of what's in
yours — face, hair, clothing, jewellery, pose.

## Best results

| Style | Type |
|---|---|
| Golden Halo | A — strong backlight, dark bokeh background |
| Torn Colour Collage | C — B&W base with a saturated torn band |
| Golden Hour Room Stack | B — three warm interior moments |
| Eye Band Poster | C — grainy base, crisp bright band across the eyes |
| Sepia Sunflower | C — vintage grade with flat sticker flowers |
