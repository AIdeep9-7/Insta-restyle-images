# Brief for an AI assistant

You are continuing an existing project. Read this fully before generating anything.

## What this is

Instagram's AI Restyle tool is usage-limited, so its effects — plus a set of Pinterest/Reels
aesthetics — were reverse-engineered into long, self-contained prompts that work in any image AI
with a photo attached. There are 21 styles in `prompts/styles.json`, each already written for both
photos in `photos/`.

## The prompt structure — always this, in this order

```
Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority.
[optional scope line: "This is a LIGHTING AND GRADE change, not a scene rebuild."]

PRESERVE EXACTLY: [every specific — face, hair, each garment, each piece of jewellery, pose, crop]

CHANGE ONLY: [the effect, described in detail]

AVOID: [the specific failure you fear]
```

The identity instruction must come **first** — models weight earlier text more heavily, and an
identity lock placed at the end measurably fails.

## The three style types

| Type | Meaning | How to run |
|---|---|---|
| **A** | One photo, one prompt | Paste and go |
| **B** | Panels stacked in sequence | 3–4 separate renders then stitch — or `tools/panels.py` to build panels from crops of one photo |
| **C** | Layers stacked on one photo | One prompt, but describe every layer explicitly |

Treating a Type B reference as a Type A style was the biggest mistake made here. One prompt cannot
produce three different poses.

## Rules learned the hard way — don't relearn these

1. **Negative prompts do not delete objects.** "No window" made the window *stronger*, twice.
   Naming a thing raises its salience. Use **positive substitution** — describe what the background
   *is*, or let it dissolve into darkness.
2. **Describe what an effect outputs, not what its name implies.** Instagram's "Sketch" is coloured,
   not graphite. Its vintage grade is green-teal, not warm orange.
3. **For art styles, demand intensity.** `bold`, `loose`, `scribbly`,
   `strokes that do not stay inside the lines`, `NOT photorealistic`, plus AVOID
   `do not make it muted, realistic or carefully rendered`. Polite prompts give weak, over-tasteful
   results — realism is the model's default gravity and must be explicitly refused.
4. **Never ask for "pores" or "natural skin texture"** — it produces blemishes. Say "smooth, clean
   and even skin, no blemishes or patchiness".
5. **Protect the gaze explicitly** on close-ups and overlays. Asking for "bright catchlights" or
   "clear irises" makes the model redraw the eyes toward the camera and drag the face with them.
   Say: "keep her gaze direction exactly as in the original."
6. **If a style only rearranges existing pixels — crop, grade, overlay — write code, not a prompt.**
   Free, exact, and it cannot drift the face. See `tools/`. Use the image model only when new
   content must be *invented*: new lighting, new background, a new art medium.
7. **Multi-panel zoom spread must be wide.** Panels at 1.35/2.05/3.10 look identical; use
   1.05/2.10/4.20 so each is clearly distinct.
8. **Expect 2–4 rounds per style.** Change one variable at a time.

## How to judge results

Compare against `refs/` and `examples/`. Be honest — say when a render misses and why. The owner
judges by direct side-by-side comparison and prefers a real critique to praise. Log every new
failure and its fix in the debug table at the end of `ig-effects-recreated.md`.

## Current state

| Style | Status |
|---|---|
| Golden Halo (A) | ✅ 10/10 on both photos — best in project |
| Torn Colour Collage (C) | ✅ approved standard for layered styles |
| Golden Hour Room Stack (B) | ✅ 9/10 — proves the multi-render pipeline |
| Eye Band Poster (C) | ✅ solved in code; every AI attempt drifted the face |
| Sepia Sunflower (C) | ✅ works both as code and as an AI prompt |
| Push-In & Macro stacks (B) | ✅ code recipes in `tools/panels.py` |
| Blue Painterly, Dreamy Diffusion, Pink Triptych | ⬜ written, never tested |

## Workflow

- `prompts/styles.json` is the source of truth. Add new styles as entries there.
- Regenerate `style-picker.html` from the JSON after changes.
- Image tools usually cap generations per turn (often 10) — batch accordingly.
- Try code polish (recrop, regrade, restitch) before spending a generation. One stack went 8→9/10
  that way at zero cost.

---

## Reference coverage map (all 13 refs)

| Ref | Style id | Route | State |
|-----|----------|-------|-------|
| 1  | `flash` | AI | done |
| 2  | `macro-stack` / `stack-detail` | code | done |
| 3  | `blue-painterly` | AI | done |
| 4  | `amber-veil-stack` | AI ×3 + stitch | done |
| 5  | `earring-stack` (Golden Hour Room) | AI | done |
| 6  | `pink-triptych` | AI ×3 + stitch | done — panels 1/3 are near-identical **in the reference too**, so this is correct, not a defect |
| 7  | `golden-halo` | AI | done — best in project |
| 8  | `inset-card` | code | done |
| 9  | `sepia-sunflower` | code + AI | done |
| 10 | `colour-block` | code | done |
| 11 | `torn-strips` | code | done |
| 12 | `poster` | code + rembg | done |
| 13 | `eye-band` | code | done |

All 13 references are now covered. 26 styles total, every one illustrated.

## Dependencies for the code styles

Pillow and numpy only, except `poster()`, which wants a subject cut-out:

    pip install rembg onnxruntime

Use the **`u2netp`** model. The default `bria-rmbg` model is ~1 GB and is killed by
the OOM reaper in a 2 GB sandbox. `cutout()` already defaults to `u2netp`.
Without rembg the poster still renders, just without the break-out cut-out.
