# Deep analysis of the 13 template images

Extracted from `11zon_JFIF-to-PDF.pdf` to `refs/ref-01.png` … `ref-13.png`. No images were
generated for this document — analysis only.

---

## ⚠️ The biggest finding: most of these are NOT single-photo edits

I had been treating all 13 as "one photo, one filter". They are not. They split into three
fundamentally different **production types**, and that distinction is what I kept getting wrong.

| Type | Which refs | What it actually is |
|---|---|---|
| **A · True single-image look** | 1, 3, 7 | One photo, one grade/relight. These are the only ones a single image prompt can fully reproduce. |
| **B · Multi-frame video stills** | 2, 4, 5, 6, 11 | Stacked frames from a **video/Reel** — different poses, different moments, stitched vertically. Not one photo. |
| **C · Designed graphic composites** | 8, 9, 10, 12, 13 | Built in an editing app (CapCut/Picsart/Photoshop) — layers, cut-outs, stickers, typography, UI chrome. |

**Implication:** for types B and C, a single prompt to an image model will always be an
approximation. The honest routes are (i) generate the individual panels and assemble them, or
(ii) accept a "single-image homage". I should have said this earlier instead of iterating blindly.

---

## Why P1 went wrong — I misread the reference

**Ref 7 is the golden backlit one, and it carries its own printed prompt.** Reading it directly:

> "…strong golden backlight creating a glowing halo effect around her hair. The scene has a shallow
> depth of field with a soft bokeh background, **almost completely dark**… slight motion blur is
> visible in her hand… diffused lighting, soft highlights, slightly hazy, dreamy lens effect.
> 85mm lens, f/1.8."

The background is **almost completely dark**. My v3 replaced it with a **bright sunlit meadow** —
the opposite. That is why you preferred v2: v2 was at least dark and warm, even with the window
artefact. I fixed the wrong variable.

**Correct P1 direction:** keep the near-black background, add a warm dark bokeh field (no
recognisable objects, no meadow, no sky), strong golden hair halo, slight motion blur on the hand.
The window should be dissolved into darkness, not swapped for a landscape.

Ref 7 also tells us the source is a **mid-turn over-the-shoulder pose**. Photo B (arms raised, eyes
closed) is not that pose, so it will never fully match — Photo A is the better candidate, or accept
the difference.

---

## Ref-by-ref breakdown

**Ref 1 — Type A.** Night, direct flash-ish key with heavy diffusion. Blown warm highlight top-right,
black surround, glossy dewy skin with visible cheek sheen, pearl earring, motion-blurred hand
sweeping through the foreground, hair catching a bright rim. Grade is neutral-warm, not orange.
*This is closest to my P4 Dreamy Diffusion, not to a firelight look.*

**Ref 2 — Type B, 4 stacked frames.** Deep B&W, extreme macro crops: eye → eye+jhumka → lips/chin →
jawline+earring. Every frame has **hair blowing across the face**. Beauty mark visible. Very shallow
focus, creamy bokeh. The look is *macro detail study*, not a portrait.

**Ref 3 — Type A.** Cool blue-grey ambient with a warm golden patch of light falling across her face
only. Teal/blue saree, blue-turquoise jhumka. Soft focus, painterly smoothing, low contrast.
Background is a plain blue wall + beige panel. Genuinely reproducible as a single edit.

**Ref 4 — Type B, 3 frames.** Hot orange/amber, very high saturation, gold-embroidered dupatta over
the head, jhumkas, strong white light streaks slashing across the frame (looks like light leaking
past fabric). Heavily blurred, dreamy, almost abstract. Motion blur throughout.

**Ref 5 — Type B, 3 frames.** Warm domestic interior at golden hour — an actual room with brass
objects, wall photos, a window. Cream/ivory kurta, gold jhumkas, **henna-covered hands**, stacked
bangles. All three frames are "putting on earrings" moments. Soft warm cinematic grade.
*This is the closest reference to your own outfit and hands.*

**Ref 6 — Type B, 3 frames.** Soft pink/blush grade, pink lace top, gold chandbali earrings, hand on
chin. Middle frame is a tight **eyes-only band**. Slightly hazy, bright, low contrast.

**Ref 7 — Type A + printed prompt.** See above. Golden halo, dark bokeh, mid-turn.

**Ref 8 — Type C.** CapCut composite: large blurred portrait as background, a **rounded-corner inset
card** of a second sharper photo, a **cut-out white hibiscus** bridging the two layers. Olive/khaki
background. Visible CapCut watermark. Two different poses = two source photos.

**Ref 9 — Type C.** Vintage sepia base, heavy grain and vertical scratches. A **horizontal band across
the eyes** that is brighter and more orange than the base. **Flat illustrated sunflower stickers**,
one bunch top-left overlapping the band, one bottom-right. Band edges are hard and rectangular.

**Ref 10 — Type C.** Grainy B&W base (woman looking left). A **hard-edged colour rectangle** pasted
over the middle — but it's a *different photo*, different pose, different saree (green blouse,
orange striped saree). This is a two-photo collage, not selective colour on one image.

**Ref 11 — Type B+C, 3 torn strips.** B&W outer strips, **colour middle strip**, torn white paper
edges. Same subject, same pose family (hand shading eyes), but three distinct frames. Grey border
around the whole composition. *This is the family your approved P7 belongs to.*

**Ref 12 — Type C, the most complex.** Editorial poster: huge blurred greyscale portrait as
background; a **mock Instagram post UI** (username bar, music line, heart/comment/share icons,
"2,211" and "880" counts); the subject in a magenta lehenga cut out and **breaking out of the post
frame**; falling rose petals; three **small black eye-strip crops** scattered around; large
semi-transparent "RUKMINI" type; a script signature; "WOMEN AESTHETICS" footer.

**Ref 13 — Type C.** Heavily grained, desaturated, dark portrait, very soft/blurred. A **thin white
rectangle outline** around the eyes, containing a sharper version of them. White script text
"The Eyes Chico" + "They Never lie" in a handwriting font.

---

## Cross-cutting patterns

1. **Eye-band motif appears in 5 of 13** (refs 6, 9, 12, 13, and partly 2). A sharp, brighter
   horizontal strip across the eyes over a softer/duller base is the single most recurring device.
2. **Torn or hard-edged layer bands appear in 4** (9, 10, 11, and 13's outline). Your approved P7
   is the torn variant.
3. **Vertical multi-frame stacking appears in 5** (2, 4, 5, 6, 11) — always 3 or 4 panels,
   always the same person in slightly different moments.
4. **Warm/amber dominates 5** (1, 4, 5, 7, 9); **B&W or desaturated 4** (2, 10, 11, 13);
   only ref 3 is cool-toned.
5. **Jhumka earrings + bangles + henna recur constantly** — the shared visual vocabulary. Your
   outfit already fits this; ref 5 is nearly a match.
6. **Motion blur and haze are used deliberately** in refs 1, 4, 7, 8, 13 — imperfection is the
   aesthetic, not a defect.

---

## What this means for the prompt set

**Rewrite needed:**
- **P1** — restore the dark bokeh background (v2 direction), drop the meadow entirely.
- **P2** — ref 4 is *blurred, abstract, light-streaked*, not the clean candlelit portrait I wrote.
- **P4** — should be modelled on ref 1 specifically (neutral-warm, blown highlight, blurred hand).

**Should be split into new, more accurate styles:**
- **Eye-Band Overlay** (refs 13 + 9's band) — the most reusable single-image device, and it works on
  one photo, so it is high-value.
- **Golden Hour Room** (ref 5) — a warm interior, closest to your actual photos and outfit.
- **Macro Detail Stack** (ref 2) — B&W extreme close-ups.

**Honest limitations to accept:**
- **Refs 8, 10, 12** need two or more different source photos. Single-prompt versions will be
  approximations at best.
- **Ref 12** additionally needs fake Instagram UI and clean typography — image models render both
  poorly. Better assembled in Canva/CapCut using AI-generated pieces.
- **Type B stacks** are best produced as separate panel renders, then combined — which I can do
  programmatically once the panels exist.

---

## Recommended next step (no generation yet)

Rewrite P1, P2 and P4 against the correct references, add the three new styles above, and mark
refs 8/10/12 as assembly jobs. Then test **one** style — the Eye-Band Overlay on Photo A, since it
is single-image, reproducible, and matches the most common motif in your board.
