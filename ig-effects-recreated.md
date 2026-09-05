# Instagram Restyle Effects — Recreated Elsewhere (v2, tested)

Paste into ChatGPT / Gemini (Nano Banana) / Grok / Arena with your photo attached.

---

## ✅ Test results — 17 effects run on the same reference photo

| Effect | Score | Notes |
|---|---|---|
| Polaroid | 10 | Film border, chemical edge blotches, cyan shadows. |
| VHS | 10 | Scanlines, RGB fringing, tracking bands, timestamp. |
| Manga | 10 | 🆕 Screentone, ink linework, seinen style. Flawless. |
| 8-bit (voxel) | 10 | 🆕 Corrected — it's Minecraft-style 3D, not flat pixels. |
| Mural | 9 | 🆕 Street-art wall, flat colour blocks, concrete texture. |
| Illustrated | 9 | 🆕 Soft storybook gouache. Identity held. |
| Lofi Dusk | 9 | ✅ v2-warm — **corrected: warm amber, not cold blue.** |
| Golden Hour | 9 | Rim light, sun glitter, flare. No drift. |
| Underwater | 9 | Caustics, bubbles, floating hair. |
| Porcelain | 9 | Delft blue glaze, crackle, correct pose. |
| Soft Focus | 9 | ✅ v2 — v1 too weak (AVOID cancelled CHANGE). |
| Flash | 9 | ✅ v2 — it's a regeneration, not a relight. |
| Sketch | 9 | ✅ v2 — **corrected: coloured pencil, not graphite.** |
| Anime | 8 | ✅ v2 — v1 recoloured the shirt purple. |
| Film Noir | 8 | ✅ v2 — v1 invented a trench coat. |
| Super HD | 8 | ✅ v2 — v1 added a fake watermark. |

### Corrections made from looking at REAL user outputs (not descriptions)
| Effect | I had it as | It actually is |
|---|---|---|
| **Lofi Dusk** | Cold blue-hour night | **Warm amber sunset**, golden rim light |
| **Sketch** | Monochrome graphite | **Coloured pencil** on paper |
| **8-bit** | Flat 2D pixel sprites | **3D voxel** Minecraft-style render |
| **Flash** | Lighting tweak | **Full regeneration**, glossy glow-up |

**Hardest to control:** genre effects (noir, anime) — they drag wardrobe and face along.
**Easiest:** film/degradation effects (Polaroid, VHS) — they only touch the surface.

---

# ⚠️ READ THIS FIRST — the structure is why it works

v1 of this file put the identity lock at the **end**. That was backwards and it caused real failures
(shirt turned purple in anime; a trench coat appeared in film noir). Fixed by three rules:

### Rule 1 — Identity goes FIRST
These models weight earlier instructions more heavily. Lead with identity, then the style.

### Rule 2 — PRESERVE must NAME things
"Keep everything the same" anchors nothing. `the oversized white sweatshirt, the ribbed cream sleeve,
the black crossbody strap, the right hand raised into the hair` anchors everything.
**Look at your photo and list what's actually in it.**

### Rule 0 — Look at the effect's THUMBNAIL, not its name
The single biggest mistake in v1: I wrote prompts from effect *names*. "Sketch" sounds like graphite —
IG's is **coloured pencil**. "Flash" sounds like a lighting tweak — IG's is a **full glow-up
regeneration**. Before recreating any effect, open the tile in the app and actually look at what it did.

### Rule 3 — Declare the scope, and name the failure in AVOID
Genre nouns ("film noir", "cyberpunk") make the model rebuild the whole scene — wardrobe included.
Say `this is a LIGHTING AND COLOUR GRADE change only, not a scene rebuild`, then explicitly
`do not add a trench coat`.

---

## THE TEMPLATE — fill this in, use it for everything

```
Use the uploaded photo as the only identity reference.
Treat identity preservation as the top priority.
[If it's a lighting/grade effect, add: This is a LIGHTING AND COLOUR GRADE change only,
not a scene rebuild.]

PRESERVE EXACTLY: the same facial structure, eye shape and spacing, nose, lips, jawline,
skin tone and age. The same [HAIR: length, colour, parting]. The same [EVERY GARMENT + COLOUR].
The same [ACCESSORIES — strap, jewellery, bag]. The same pose with [WHAT THE HANDS ARE DOING].
The same expression. The same crop and camera angle.

CHANGE ONLY: [the one thing].

AVOID: do not [the specific failure you fear]. Do not beautify, slim, or change age.
Keep natural skin texture with visible pores — no plastic smoothing.
```

**Your PRESERVE list is the whole game.** Two minutes describing your actual photo beats any
amount of style wording.

---

# TRENDING

## 🔥 Lofi Dusk — ✅ tested v2-warm — ⚠️ IT'S WARM AMBER, NOT COLD BLUE
> **Corrected against real user outputs.** I originally wrote this as a cold blue-hour night scene.
> Real Lofi Dusk results are **warm sunset**: orange horizon, golden rim light through the hair,
> rich warm-dark foreground. "Dusk" means *sunset glow*, not *night*.

```
Use the uploaded photo as the only identity reference. Treat identity preservation as the top
priority.

PRESERVE EXACTLY: the same facial structure, eye shape and spacing, nose, lips, jawline, skin tone
and age. The same [HAIR]. The same [GARMENTS + COLOURS]. The same [ACCESSORIES]. The same pose
with [HANDS]. The same expression, crop and camera angle.

CHANGE ONLY: re-photograph this at dusk just after sunset. A warm amber-orange sun sits low directly
behind the subject, throwing a strong glowing golden rim light along the top of the hair, the
shoulders and the arm edges. The face sits in soft warm shadow, gently lifted by warm bounce. The
sky behind glows deep orange fading to dusky indigo at the top, with dark silhouetted trees and a
few tiny warm distant lights. Foreground and ground fall into rich warm darkness. Overall grade is
warm amber and bronze with deep crushed shadows — nostalgic, moody, emotional. Cinematic bloom and
halation around the rim light, atmospheric haze catching the sun, heavy nostalgic film grain,
shallow depth of field.

AVOID: do not make the image cold, blue or cyan — this must be warm amber and golden. Do not change
the clothing, pose or facial features. No text or watermarks.
```
**Variants:** `rainy Tokyo street with neon reflections` · `empty parking lot under one sodium lamp` · `beach at last light` · `rooftop, city glowing below`
**Cold-blue version** (my original — a fine look, just not Lofi Dusk): swap the warm clauses for `cool blue-hour tones, cyan shadows, blue city bokeh`.

## 🔥 Flash — ✅ tested v2 — ⚠️ this is a REGENERATION, not a relight
> **v1 undershot this.** IG's Flash is the viral "glow-up" filter: glossy luminous skin, features
> pushed forward, background dropped to a moody dark night scene. It's a full AI re-render.
> It went viral *and* controversial — users reported it changing eye colour and even ethnicity.
> **So the AVOID line here is not optional.**

```
Use the uploaded photo as the only identity reference. Treat identity preservation as the top
priority — preserve the exact facial structure, eye shape and spacing, nose bridge, lips, jawline,
natural skin tone and eye colour. Do not change her ethnicity or eye colour.

PRESERVE EXACTLY: the same [HAIR]. The same [GARMENTS + COLOURS]. The same [ACCESSORIES].
The same pose with [HANDS]. The same expression. The same crop and camera angle.

CHANGE ONLY: re-photograph this as a night-time direct-flash portrait. Harsh on-camera flash hitting
the face straight on — bright glossy highlights on the forehead, nose bridge and cheekbones, luminous
even skin, sharp defined features. Hard-edged shadow falling directly behind. The background falls
away into a dark moody underexposed night scene with only faint detail. High contrast, punchy
saturated colour, crisp sharpness, slight retro digital-camera grain. Glamorous editorial night-out look.

AVOID: do not smooth the skin into plastic, do not reshape the face, do not change eye colour or
skin tone, do not change the clothing or pose.
```
**Daytime/indoor variant:** replace the background line with `the background falls away into a dark underexposed room` — the dark surround is the whole point of the look.

## Sketch — ✅ tested v2 — ⚠️ IG's Sketch is IN COLOUR
> **v1 was wrong.** I described graphite because the effect is called "Sketch". Look at the tile in
> the app: it's a **coloured pencil** drawing that keeps the photo's original colours in the shading.

`CHANGE ONLY:` redraw as a COLOURED PENCIL drawing on visible off-white sketchbook paper. Keep the original colours of the scene rendered as layered coloured pencil strokes. Visible directional pencil hatching where colour is built up, slightly uneven imperfect linework, soft waxy pencil texture, paper grain showing through everywhere. Loose graphite under-drawing lines still visible at the edges. Background rendered loosely with bare paper showing in places; the face more finished than the background.
`AVOID:` **do not make it greyscale or monochrome — this must be in colour.** Do not make it a clean digital illustration; it must look hand-drawn on paper. Do not alter facial features, garment colours or pose.

**True greyscale version** (not what IG's Sketch does — use if you actually want graphite): swap in `monochrome graphite only, no colour` and drop the colour clause.

## Soft Focus
> Note: IG's Soft Focus is a **portrait-mode / diffusion** effect — it lifts the subject off a
> softened background, not just a global blur.

`CHANGE ONLY:` a strong dreamy soft-focus diffusion look. Heavy milky bloom glowing out of every highlight, washed lifted blacks, markedly lowered contrast, warm pastel grade, visible haze over the whole frame, fine grain, soft vignette. Push the background into deep creamy defocus. Keep the eyes as the one sharp anchor.
`AVOID:` do not alter facial features, garment colours or pose.

> ⚠️ **Tested failure:** v1 said "gentle bloom" then "keep pores visible, don't blur the eyes" — the
> AVOID cancelled the CHANGE and the result was nearly identical to the original. If an effect comes
> out too weak, check whether your AVOID list is contradicting the effect itself.

## Super HD
> Note: in-app this is a **Utilities** effect — an upscaler/enhancer. It's the one effect that
> should change *nothing* about the content. If your result looks restyled, the prompt failed.

```
Use the uploaded photo as the only identity reference. This is a TECHNICAL FINISHING PASS,
not a redesign.

PRESERVE: the subject, identity, anatomy, expression, clothing, composition, crop, camera angle,
colours, any text or logos, object positions, and background — all unchanged.

CHANGE ONLY: recover fine detail in hair strands, eyelashes, skin pores and fabric weave.
Increase micro-contrast and local sharpness. Fix softness and motion blur. Clean up compression
artifacts and noise. Rich HDR tonality — recovered highlights, opened shadows, deep grounded blacks.

AVOID: do not beautify, reshape, restyle or reposition anything. Do not over-sharpen into halos.
Keep natural skin texture.
DO NOT INVENT, ADD OR ALTER ANY TEXT, LOGOS OR WATERMARKS — leave small unreadable text
unreadable rather than resolving it into invented words.
```
> ⚠️ **Tested failure:** without that last line this added a fake "WAY UP" watermark bottom-right and
> turned the chest print into gibberish. Enhancers try to "resolve" illegible text into real words.

## Lofi Dusk vs Flash — don't confuse them
Both are dark-background flash looks, and people mix them up:
- **Flash** = bright glossy skin, *frontal* flash, glamorous, colour-punchy, sharp.
- **Lofi Dusk** = *backlit* WARM golden sunset rim light, hazier, nostalgic, grainier, emotional.

## Anime — ✅ tested, fixed in v2
```
Use the uploaded photo as the only identity reference. Treat identity preservation as the top
priority.

PRESERVE EXACTLY: the same facial structure, eye shape and spacing, nose bridge, lips, jawline,
skin tone and age. The same [HAIR]. The same [GARMENTS — STATE EVERY COLOUR EXPLICITLY].
The same [ACCESSORIES]. The same pose with [HANDS]. The same expression and eye-line.
The same crop and camera angle.

CHANGE ONLY: convert the rendering medium to a high-quality anime illustration — clean confident
linework, cel shading with two-tone shadows, hand-painted version of the same background, soft bloom.

AVOID: do not enlarge the eyes, do not round or slim the face, do not add a smile or blush, do not
recolour any garment, do not prettify or generify the features. She must remain identifiable as the
same specific person.
```
> ⚠️ Anime is the worst offender for recolouring clothes and prettifying faces. State every garment colour and forbid bigger eyes.

## Watercolour
`CHANGE ONLY:` repaint as loose watercolour on cold-press paper. Translucent bleeding pigment, wet-on-wet blooms, visible brush edges and water marks, bare white paper in the highlights. Muted palette with a few saturated accents. Background looser than the face.
`AVOID:` do not change the pose, garments or facial proportions.

## 8-bit — ✅ tested — ⚠️ it's 3D VOXEL, not flat pixel art
> Meta's own preset grid shows "8-bit" rendering as a blocky **Minecraft-style 3D voxel** scene,
> not 2D sprite art. My v1 was wrong.

`CHANGE ONLY:` convert the entire scene into a blocky 3D voxel render in a Minecraft-like game style. The person becomes a chunky voxel character built from large visible cubes — blocky head, cube arms, stair-stepped blocky hair, blocky torso in the original garment colours. Keep the recognisable pose. Flat-shaded cube textures, hard edges, no smoothing, pixel-grid texturing on each block face. Background becomes blocky voxel trees with cube foliage and flat blocky water. Bright clean daylight, soft ambient occlusion in the crevices, blue sky with blocky white clouds. 3D game render with real depth.
`AVOID:` do not make this flat 2D pixel art — it must be a three-dimensional blocky voxel scene with volume. No text or watermarks.

**True flat pixel-art version** (if you want actual 8-bit sprites): `convert to flat 2D 8-bit pixel art, large visible square pixels, 32-colour retro console palette, hard dithering, chunky outlines, no 3D depth`.

## Manga — ✅ tested
> Distinct from Anime: **black and white, screentone, printed page.** Anime is colour cel-shading.

`CHANGE ONLY:` redraw as a black and white Japanese manga panel. Crisp confident black ink linework with varying line weight, dense screentone dot patterns for all mid-grey shading, heavy solid black in the hair with sharp white highlight streaks, fine cross-hatching in the shadows. Background as screentone gradient and simplified ink shapes. Detailed realistic seinen manga style, high contrast, printed-page ink texture.
`AVOID:` no colour — pure black, white and screentone grey only. Do not enlarge the eyes or make it cute shoujo style. Do not change the pose or garments. No speech bubbles, no text.

## Mural — ✅ tested
`CHANGE ONLY:` repaint as a large hand-painted street mural on a textured concrete wall. Bold flat blocks of saturated colour, thick confident brush and spray-paint strokes, simplified graphic shapes, strong dark outlines around the figure. Garments become bold flat colour blocks with painted fold lines. Background becomes stylised painted foliage and decorative floral or leaf motifs filling the empty space. Visible wall texture, concrete grain and slight paint drips showing through.
`AVOID:` do not make it photorealistic. No text, tags, signatures or watermarks.

## Illustrated — ✅ tested
> The softest of the art presets — storybook, not anime, not mural.

`CHANGE ONLY:` redraw as a soft hand-painted digital illustration in a gentle storybook style. Delicate visible brush texture, soft gouache-like colour blending, gentle warm lighting, slightly muted desaturated palette, soft rounded edges with light linework. Background becomes loose painted impressionistic shapes with dappled light. Cosy, warm, calm — modern editorial illustration.
`AVOID:` do not make it photorealistic, do not make it anime, do not change garment colours or pose.

## Pink
`CHANGE ONLY:` restyle the whole image around a bold pink monochrome palette — hot pink, blush and magenta across the background and surfaces, pink-tinted lighting on the subject, glossy saturated finish. Playful, high-fashion, Y2K.
`AVOID:` keep the face, pose and garment shapes unchanged; recolour the world, not the person's identity.

# FILM EFFECTS

## Film Noir — ✅ tested, fixed in v2
```
Use the uploaded photo as the only identity reference. Treat identity and wardrobe preservation as
the top priority. This is a LIGHTING AND COLOUR GRADE change only, not a scene rebuild.

PRESERVE EXACTLY: the same facial structure, eye shape, nose, lips, jawline, skin texture and age.
The same hair. The same [GARMENTS] — the subject is NOT wearing a coat, hat or jacket.
The same [ACCESSORIES]. The same pose and hand position. The same crop, camera angle and framing.

CHANGE ONLY: the lighting and colour. High-contrast black and white. A single hard key light raking
across the face from the left, deep crushed blacks, venetian-blind slat shadows falling across the
face and the wall behind. Background darkened to near black with faint haze. Strong vignette,
coarse silver-halide film grain.

AVOID: do not change the clothing, do not add a trench coat or hat, do not restage the scene as an
alley, do not change the pose or facial features, do not move the camera.
```
> ⚠️ "Film noir" implies 1940s wardrobe. You **must** forbid the coat by name.

## Vintage / Retro Film
`CHANGE ONLY:` expired 1990s 35mm film look. Faded lifted blacks, warm yellow-orange cast, desaturated greens, halation around bright areas, heavy visible grain, corner softness, a light leak bleeding in from one edge, small orange date stamp bottom-right. Kodak Gold 200 character.
`AVOID:` do not change clothing, pose, background content or facial features. Grade only.

## Polaroid
`CHANGE ONLY:` render as an instant Polaroid. Place the image inside a thick white instant-film border with the wider bottom strip. Washed-out low-contrast colour, cyan-shifted shadows, warm creamy highlights, soft focus, uneven chemical blotches at the edges.
`AVOID:` do not crop out the subject or change the outfit — fit the existing framing inside the border.

## VHS
`CHANGE ONLY:` a frame from a worn VHS tape. Horizontal scanlines, red/blue chromatic bleeding, tracking distortion bands, softened detail, blown highlights, muddy shadows, faint blocky white timestamp in the corner, analogue interlacing noise.
`AVOID:` do not change the content, outfit or pose. Degradation only.

## Grain & Vignette
`CHANGE ONLY:` add heavy organic 35mm grain and a soft dark corner vignette. Slightly lift blacks for a filmic matte finish, gently roll off highlights, add a light warm cast.
`AVOID:` change nothing else at all — no content, colour-identity, or composition changes.

---

# LIGHTING
*(All of these should open with: "This is a LIGHTING change only, not a scene rebuild.")*

## Golden Hour
`CHANGE ONLY:` relight in golden hour sun. Low warm sun from the left at a shallow angle, glowing rim along hair and shoulders, long soft shadows. Warm amber highlights, blue-lifted shadows, atmospheric haze catching the light, subtle anamorphic flare. Teal-and-orange cinematic grade.
`AVOID:` do not change the clothing, pose, background geometry or facial features.

## Paparazzi Flash
`CHANGE ONLY:` a single hard paparazzi flash in a dark environment. Brutal direct frontal light, blown highlights on forehead and cheekbones, hard black shadow behind, background falling to near black, cool white flash temperature, slight edge motion blur.
`AVOID:` do not change the outfit, pose or setting — only the light.

## Neon Glow
`CHANGE ONLY:` relight with neon. Magenta from the left, cyan from the right, meeting across the face with strong colour separation. Reflective catchlights in the eyes, wet-looking sheen, atmospheric haze holding the colour, glowing signage bokeh in the darkened background.
`AVOID:` do not change the clothing or pose, do not add cyberpunk costume elements.

## Rim Light
`CHANGE ONLY:` add a strong backlight creating a bright separating rim along hair, shoulders and jawline. Front of the face in soft shadow with gentle fill. Darken and simplify the background so the rim reads. Slight lens bloom where the light wraps.
`AVOID:` do not change wardrobe, pose or facial features.

## Studio Light
`CHANGE ONLY:` relight as a studio portrait — large softbox key at 45° camera-left, soft fill right, hair light behind, seamless neutral grey backdrop with a gentle gradient. Soft shadow transitions, catchlights in both eyes.
`AVOID:` do not change the clothing into formalwear, do not retouch the face, do not slim or beautify.

## Moonlight
`CHANGE ONLY:` relight as a night scene lit only by moonlight. Cool blue-silver key from above, deep desaturated shadows, faint warm practicals far behind, soft ambient haze, low-key exposure with shadow detail retained.
`AVOID:` do not change the outfit, pose or location layout.

---

# SEASONAL / THEMED
*(These legitimately change the background, so PRESERVE the person harder.)*

## Halloween — Ghost Face
`CHANGE ONLY:` make the subject spectral — translucent desaturated skin with a faint inner glow, edges softly dissolving into mist, darkened hollow eyes. Cold blue-green light, thick fog, dark abandoned interior behind.
`AVOID:` keep the same face structure and outfit shape — a ghostly version of this exact person, not a different figure.

## Halloween — Haunted Mirror
`CHANGE ONLY:` add an antique mirror beside the subject. The reflection is distorted and sinister — different expression, shadowed features, faint figures behind it. Cracked ornate frame, dust, candlelight, cold fog.
`AVOID:` the real subject keeps their exact face, outfit and pose. Only the reflection is altered.

## Diwali — Diyas
`CHANGE ONLY:` place the subject in a warm Diwali setting — rows of glowing clay diyas in the foreground and around them, marigold garlands, rangoli on the floor. Relight the face with soft flickering warm orange candlelight.
`AVOID:` do not change the clothing into traditional wear unless asked. Keep face, pose and outfit.

## Diwali — Fireworks
`CHANGE ONLY:` place the subject on a night rooftop with fireworks bursting behind. Coloured light spilling onto face and clothes, a lit sparkler in the free hand with light trails, warm city lights below, atmospheric smoke.
`AVOID:` keep the same outfit, face and body position.

## Eid
`CHANGE ONLY:` place the subject in an Eid night scene — crescent moon and stars in deep indigo sky, glowing hanging lanterns casting warm gold light, soft bokeh string lights.
`AVOID:` keep the existing outfit and face unless a wardrobe change was requested.

## Snow
`CHANGE ONLY:` add heavy falling snow — flakes sharp near camera, soft blurred flakes behind. Settle snow on hair and shoulders, add visible cold breath. Cool blue-white grade with warm light sources cutting through, overcast diffused light.
`AVOID:` do not change the outfit, add a coat, or alter the pose.

---

# VIDEO EFFECT LOOKS (as stills)

## Underwater
`CHANGE ONLY:` submerge the subject. Caustic light ripples across face and body, rising air bubbles, hair and fabric floating upward, blue-green cast deepening with distance, sunlight shafts from above, soft particulate haze.
`AVOID:` keep the same face, outfit and pose — floating, not restaged.

## Porcelain
`CHANGE ONLY:` render the subject as a glazed porcelain figurine — glossy ceramic skin with subsurface glow, fine crackle glaze, delicate hand-painted blue detailing on the clothing, soft studio light with gentle speculars, plain backdrop.
`AVOID:` keep the exact pose, hairstyle silhouette and garment shapes.

## Fire & Flames
`CHANGE ONLY:` surround the subject with fire — flames and glowing embers rising around and behind, warm orange light flickering across the face from below, drifting ash and smoke, heat distortion, dark background.
`AVOID:` do not change the clothing or pose, do not add armour or costume.

## Biker Jacket
```
PRESERVE EXACTLY: the same face, hair, expression, pose, hands, background, lighting and crop.
CHANGE ONLY: the top garment becomes a worn black leather biker jacket with silver zips, studs and
a popped collar, over a plain dark tee. The jacket must follow the existing body position with
believable seams, folds and occlusion.
AVOID: do not change the face, body proportions, hands, hairstyle, background or lighting.
```

---


---

# 🔥 BENCHMARKED AGAINST REAL INSTAGRAM OUTPUT
Added after comparing my results side-by-side with the same photos run through IG's Restyle.

### The lesson: IG's presets are AESTHETICALLY AGGRESSIVE. Mine were too polite.
My prompts kept hedging toward realism and careful rendering. IG's art presets commit hard to the
medium. If your result looks like a tasteful version of the effect, push these words:
`bold` · `loose` · `scribbly` · `energetic` · `NOT photorealistic` · `strokes that do not stay inside the lines`
And put the hedge in AVOID: `do not make it muted, realistic or carefully rendered`.

### ⚠️ IG drifts identity more than this method does
In the side-by-side, IG's dark-backdrop portrait noticeably changed the subject's bone structure and
ethnicity. The PRESERVE-block approach here holds likeness better. **You are trading a little
aesthetic punch for a lot of identity accuracy — and the punch is recoverable with stronger wording.**

## Vibrant Coloured Pencil — ✅ tested, beats IG's version
> This is what IG's "Sketch" actually looks like at full strength. My earlier Sketch entry was too tight.

```
Use the uploaded photo as identity reference — keep [FACE], [HAIR], [POSE], [GARMENTS], [JEWELLERY].

CHANGE ONLY: redraw as a LOOSE, VIBRANT COLOURED PENCIL SKETCH on aged cream sketchbook paper.
Energetic, scribbly, rapid hatching strokes that do not stay inside the lines — visible individual
pencil strokes everywhere, layered and criss-crossing. Use a BOLD MULTICOLOURED palette: the
background scribbled in bright blues, greens and yellows; [MAIN GARMENT] in vivid reds, oranges and
warm pinks; [SECOND GARMENT] in golden yellow and ochre with green motifs; hair in warm browns with
visible stroke direction. Loose confident contour lines in coloured pencil rather than graphite.
Cream paper deliberately left showing through between strokes everywhere. Illustrative and
expressive, NOT photorealistic — flat stylised shading, simplified features, an artist's energetic
sketchbook study.

AVOID: do not make it muted, realistic or carefully rendered — it must be bold, colourful and loose.
Do not make it greyscale. No text or watermarks.
```

## Vintage Film (green-teal) — ✅ tested, matches IG
> IG's vintage look is **green-teal**, not warm orange. This is the one I kept getting wrong by
> reaching for golden tones.

```
This is a COLOUR GRADE AND FILM EMULATION pass only, not a scene rebuild.
PRESERVE EXACTLY: [full preserve list], the same crop, camera angle and background.

CHANGE ONLY: regrade as a photo shot on expired 35mm analogue film. A distinctive muted green-teal
colour cast washing over the whole image, especially in the whites and the shadows. Desaturated
dusty tones overall, but the lips stay deep and rich and the skin keeps a warm peachy tone against
the green surround. Lifted milky blacks, gently rolled-off highlights, low contrast. Heavy visible
organic film grain across the entire frame. Slight softness and halation around bright areas.
Nostalgic, melancholic, cinematic — like a still from a 90s art film on Fuji film stock.

AVOID: do not make it warm orange or golden — the cast must be green-teal. Do not change the
clothing, pose, jewellery or facial features.
```

## Film Strip / Burnt Negative — ✅ tested, beats IG's version
```
PRESERVE: [face, hair, pose, garments, jewellery].

CHANGE ONLY: present this photo as a single frame of physical 35mm colour film against a pure black
background. Show the full film strip: rows of square sprocket holes running down both left and right
edges, and small printed film-edge markings along the top and bottom in orange and white text reading
"S-400" and frame numbers "16" and "16A". The photograph sits in the central frame area. The strip
edges are physically damaged — burnt, melted and irregular, with the emulsion bubbling and curling,
and vivid chemical light leaks bleeding in from the edges in hot magenta, orange, red and cyan that
spill slightly over the corners of the image. The photo itself keeps warm natural colour with visible
film grain. Analogue, tactile, destroyed-film aesthetic.

AVOID: do not change the face, clothing or pose. Keep the black surround clean and empty.
```

## Dark Backdrop Portrait
```
This is a LIGHTING AND BACKGROUND change only.
PRESERVE EXACTLY: [full preserve list], the pose and crop.

CHANGE ONLY: place the subject against a completely plain matte black backdrop with no visible
detail. Light from behind and slightly above with a warm golden backlight that creates a bright
glowing rim along the hair, shoulders and arms, with visible light flare where it catches. Fill the
face softly with warm bounce so features stay clear. Rich warm golden tones on the skin and fabric
against pure black. Subtle film grain, editorial studio quality.

AVOID: do not change the clothing, jewellery, pose or facial features. Do not alter bone structure or
ethnicity. Keep the background pure black and empty.
```

# 📌 PINTEREST / REELS AESTHETIC STYLES (from your reference boards)

Nine styles reverse-engineered from the 13 references you sent. Duplicates were merged:
refs 2+9 → Golden Backlit Halo · refs 11+12+13 → Selective Colour Collage · refs 7+8 → Graphic Poster.

Every prompt below assumes your standard opening line and PRESERVE block. Paste your PRESERVE
list into the marked slot verbatim — that is what keeps your face, outfit and jewellery intact.

---

## ⭐ CANONICAL LAYERED-COMPOSITION RECIPE (derived from P7 — the approved result)

P7 is the approved reference. **Every layered / multi-panel / collage style must follow this exact
five-part recipe.** This is what made it work where the others failed.

1. **Identity line + "identical in every layer".** State up front that the face must be the same in
   all copies of it. Multi-layer prompts regenerate the face per region unless told not to.
2. **Name the base layer as a full-frame treatment.** "The base layer fills the whole frame:
   the photo converted to deep, grainy, high-contrast black and white… no colour left anywhere."
   Never say just "black and white background".
3. **Name the overlay's POSITION relative to her body, not the frame.** "Position the band so it
   crosses her face and upper body — her eyes, lips, earring and neckline must all fall inside it."
   Framing it by frame-thirds alone put the band on the background in v1.
4. **Enumerate the colours inside the overlay item by item.** "the kurta a rich warm cream with
   deep chocolate-brown motifs, the gold earring bright and metallic, the bangles gleaming, the
   lips a strong red." Saying "full saturation" is NOT enough when the source photo is muted.
5. **Describe the physical edge and the offset.** "torn like ripped paper, white fibrous ragged
   fibres, a soft drop shadow cast onto the layer beneath" + "shift the band sideways so it is
   visibly misaligned." This is what makes it read as a designed collage instead of a filter.

Apply all five to P6, P8 and P9 as well — they are layered styles and inherit this recipe.

---

## P1 · Golden Backlit Halo — v3
**v1 failed** (glowing rectangular panel). **v2 failed worse** — listing "no window, no doorway"
made the window STRONGER, because negatives raise salience and the source photo contains one.
**v3 fix: positive substitution + tighter crop.** Describe the replacement background as a real
place, and reduce how much background is left to argue about.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority. This is a LIGHTING, BACKGROUND-REPLACEMENT and GRADE change.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: she is now standing outdoors in an open field at sunset. Behind her stretches a wide open meadow of tall dry golden grass, with a distant treeline and a warm orange sky low on the horizon, all thrown far out of focus into a smooth wash of amber, honey and soft brown. Crop tighter than the original, framing her from mid-chest up so the outdoor field fills the entire background. The sun sits low behind her head, just out of frame, rimming her hair into glowing amber filaments and wrapping a bright warm edge along her cheek, shoulder and arms. Soft warm bounce fills her face — dewy skin, a natural sheen on the cheekbones and nose bridge, no harsh shadow. Thick golden atmospheric haze drifts diagonally across the whole frame with visible light rays and gentle lens flare. Strong bloom and halation. Shallow depth of field, 85mm f/1.8. Romantic, ethereal, cinematic.

AVOID: do not change the face, clothing, jewellery or pose. Do not make it cold or blue. Keep the background entirely out of focus. No text or watermarks.

## P2 · Warm Amber Firelight — v2
**v1 issue:** read as a person standing in a lit room — the wall and corner were still visible, and
the light was too even. Ref 1 is much tighter, hotter and more enveloping, with the glow *between*
the camera and her. **v2 fix:** crop in close, replace the wall with pure darkness by positive
substitution, and put glowing haze in the foreground.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority. This is a LIGHTING, BACKGROUND-REPLACEMENT and GRADE change.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: crop in close, framing her from the shoulders up so her face fills much of the frame. She is surrounded by open night air — the space behind her is pure deep black emptiness with a soft pool of orange glow floating in it, no walls, no corners, no furniture, no visible surfaces. A single warm flame just out of frame at one side throws intense saturated amber and burnt-orange light across one side of her face, catching the edge of her brow, cheekbone, lips, jaw and raised forearm, while the far side falls into rich warm shadow. Glowing warm skin with strong specular highlights. Drifting sparks and embers float through the air around her. A veil of warm orange haze passes between the camera and her face, blooming across part of the frame and softening it. Deep halation around every highlight, heavy warm film grain. The image is dominated by hot orange, bronze and black. Cinematic, intimate, candlelit.

AVOID: do not change her face, clothing, jewellery or pose. Do not make the light white or neutral — it must be deep amber. Keep the background pure darkness. No text or watermarks.

## P3 · Soft Blue Painterly Portrait — ref 3
The cool, smooth, almost-illustrated look: gentle blue-grey light, glassy skin, painterly softness
while staying photographic.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: regrade and relight as a soft cool-toned portrait with a painterly finish. A gentle diffused light from one side, cool blue-grey ambient fill, a soft warm highlight only on the cheekbone and the bridge of the nose so the face still glows against the cool surround. The background becomes a smooth graduated wash of dusty blue and warm sand, softly out of focus, with a subtle shadow shape cast across it. Skin rendered smooth and luminous with visible soft-brush texture in the shading, edges slightly softened as though lightly painted over. Muted, elegant, low-saturation palette apart from the warm skin. Dreamy and still.

AVOID: do not turn this into a cartoon or anime — it must remain photographic with a painted finish. Do not change the face, clothing, jewellery or pose. Do not oversaturate. No text or watermarks.

---

## P4 · Dreamy Diffusion Glow — ref 5
Heavy bloom, blown highlights, motion-blurred hand, everything soft except the eyes. IG's Soft
Focus taken much further.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: re-photograph with a heavy diffusion filter at night. A bright light source behind and to one side blooms strongly into the frame, glowing through her hair and washing a milky veil of light across one part of the image. Highlights blow out softly and bleed into the surrounding areas. The background is deep black with a few soft floating bokeh orbs. Skin is dewy and luminous with soft blush on the cheeks and nose. Her eyes stay the sharpest point in the image while everything else falls into gentle softness. Slight motion blur on the nearest hand and on stray hair, suggesting movement. Warm-neutral grade, gentle grain, glossy and ethereal.

AVOID: do not show the light source itself as a lamp, window or glowing rectangle — it stays out of frame. Keep the eyes sharp — do not blur the whole face uniformly. Do not change her face, clothing, jewellery or pose. Do not add a bright background. No text or watermarks.

---

## P5 · High-Contrast B&W Close-Up — v2 (ref 6)
**v1 issue:** asking for "natural texture and pores" overshot into visible blemishes and patchy skin.
**v2 fix:** remove the texture request; state clean even skin positively.
Dramatic monochrome, hair across the face, deep blacks. Distinct from Manga: this is photographic,
not illustrated.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority. This is a CONVERSION AND LIGHTING pass, not a scene rebuild.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: convert to a dramatic high-contrast black and white portrait. Deep true blacks, luminous bright highlights on the cheekbone, brow and lower lip, and a full range of silver mid-tones across the skin. Strong directional side light sculpting the face. Every individual strand of hair rendered sharp and separated, some strands falling loosely across the cheek and catching the light. The eyes are the focal point — crisp, wet-looking, with a bright catchlight and clearly defined lashes. Background falls to near black. Her skin is smooth, clean and even with a soft natural finish — flawless, no blemishes, spots, scarring or patchiness. Fine natural film grain, slight vignette, deep shadow detail retained. Editorial, moody, timeless.

AVOID: no colour anywhere. Do not smooth the skin — keep natural texture. Do not change the face, clothing, jewellery or pose. No text or watermarks.

---

## P6 · Graphic Poster with Text Strips — merged from refs 7 + 8
The designed-layout look: a large soft portrait behind, a crisp inset rectangle, and typographic
strips. Only style here that intentionally adds text.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority. The face must stay identical in every copy of it that appears in the layout.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: build a graphic poster composition from this photo. The background layer is the same portrait scaled up very large, heavily blurred and desaturated, filling the whole frame. Over it, place one crisp rectangular inset containing a sharp, well-exposed crop of her eyes and brows, aligned horizontally across the middle of the frame with a thin white border. Add one or two smaller narrow strips containing cropped details from the same photo. Add clean minimal typography: a thin white handwritten-script word and a small uppercase sans-serif line beneath it, placed in the empty negative space, never over her face. Muted desaturated palette with a single accent colour pulled from her outfit. Subtle paper grain over everything. Modern editorial poster design.

AVOID: only use words I would recognise as design placeholder text — no gibberish lettering, no misspellings, no fake logos or watermarks. Do not alter her facial features in any copy of the face. Do not cover the eyes in the main inset.

---

## P7 · Selective Colour Collage — ✅ APPROVED BY USER — the reference standard for all layered styles
Black-and-white base with a colour region. **v2 fixes:** name the garment colours inside the band
explicitly (saying "full saturation" is not enough when the source is already muted), force the
mono layer to be *deeply* desaturated for contrast, and keep the colour band centred on her, not
on the background.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority. The face must remain identical in both the colour and the black-and-white portions of the composition.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: build a torn-paper collage from this single photo. The base layer fills the whole frame: the photo converted to deep, grainy, high-contrast black and white with true blacks and bright whites, heavily desaturated with no colour left anywhere in it. Across the middle third, lay a horizontal band of the exact same photo in vivid, richly saturated colour. Position the band so it crosses her face and upper body — her eyes, lips, earring and the neckline of her kurta must all fall inside the colour band. Inside the band the colours are boosted and warm: the kurta a rich warm cream with deep chocolate-brown block-print motifs, the chevron dupatta in saturated brown and cream, the gold earring and chain bright and metallic, the silver bangles gleaming, the lips a strong red, the skin warm and golden. The band's top and bottom edges are torn like ripped paper, with white fibrous ragged fibres and a soft drop shadow cast onto the monochrome layer beneath. Shift the colour band slightly sideways so it is visibly misaligned with the black-and-white layer underneath. Fine paper texture and grain over the whole composition. Clean, graphic, high-contrast scrapbook aesthetic.

AVOID: do not let the monochrome layer retain any colour tint. Do not centre the colour band on the background instead of on her. Do not change her face, clothing, jewellery or pose in either layer. Do not add any text. Keep the torn edges deliberate and clean.

## P8 · Vintage Sepia Sunflower Overlay — ref 10
Faded aged-print grade with a graphic overlay strip and flat illustrated florals.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: regrade as a faded vintage print — warm sepia and dusty brown tones throughout, low contrast, lifted milky blacks, slightly bleached highlights, heavy paper grain and a few fine vertical scratches. Across the eyes lay a horizontal rectangular strip showing the same crop of her eyes but brighter, warmer and more saturated than the surrounding image, with a crisp straight edge. Add flat illustrated sunflowers in bright yellow and warm orange as a decorative overlay in two corners, drawn in a simple graphic sticker style so they read as pasted on rather than part of the photograph. Nostalgic, warm, analogue-scrapbook feel.

AVOID: do not change her face, clothing, jewellery or pose. Do not make the flowers photorealistic — they must look like flat illustrated stickers. Do not cover her eyes. No text or watermarks.

---

## P9 · Soft Pink Triptych — ref 4
Warm pink, close, three-panel layout with an eye-detail centre band.

Use the uploaded photo as the only identity reference. Treat identity preservation as the top priority. The face must be identical in all three panels.

PRESERVE EXACTLY: [your PRESERVE block]

CHANGE ONLY: build a vertical three-panel triptych from this photo. The top panel is a soft warm portrait crop from the chest up. The centre panel is a tight horizontal band showing only her eyes, sharp and detailed with visible lashes and a bright catchlight. The bottom panel repeats the portrait crop at a very slightly different scale. Panels sit flush with hairline white gaps between them. Grade everything with a warm soft-pink cast — blush tones in the skin, dusty rose in the shadows, a gentle pink glow overall, low contrast and slightly hazy. Soft diffused lighting, dewy luminous skin, a warm neutral background. Cohesive, romantic, soft-girl aesthetic.

AVOID: do not change her face, clothing, jewellery or pose in any panel. Do not let the panels show different expressions or lighting. Do not leave visible seams misaligned or panels at different colour temperatures. No text or watermarks.

---

### Which of these overlap with what you already have
- **P1 Golden Backlit Halo** is a stronger, hazier version of your existing **Golden Hour**. Use P1 when you want the blown-out halo; use Golden Hour for a natural relight.
- **P4 Dreamy Diffusion** supersedes **Soft Focus** — same idea, much further pushed.
- **P5 B&W Close-Up** is the photographic sibling of **Manga** and of **Film Noir**.
- **P2 Warm Amber Firelight** is close to **Diwali — Diyas** but with no diyas in shot.

## Debug table — match the symptom to the fix

| What went wrong | Add this |
|---|---|
| Face became a different person | Move identity to the very top; name jawline, eye spacing, nose bridge, skin tone |
| Garment changed colour | State the colour explicitly in PRESERVE **and** `do not recolour any garment` |
| Unwanted clothing appeared | Name it in AVOID: `do not add a trench coat / hat / armour` |
| Whole scene got restaged | Add `this is a lighting and colour grade change only, not a scene rebuild` |
| Face got prettified | `do not enlarge the eyes, do not slim or round the face, no beauty filter` |
| Plastic skin | `keep natural skin texture with visible pores, natural asymmetry` |
| Pose shifted | Describe the pose literally: `right hand raised into the hair` |
| Too many things drifted | Go back to the ORIGINAL photo and make one change — don't patch a bad output |
| Effect too strong | `subtle, understated, about 40% strength` |
| Result looks tasteful but weak vs IG | You hedged. Add `bold, loose, scribbly, NOT photorealistic` + AVOID `do not make it muted or carefully rendered` |
| Vintage grade looks orange not vintage | IG's vintage is **green-teal** — say so explicitly and forbid warm/golden |
| Result came out greyscale but IG's is colour | Say `this must be in colour` in AVOID — "sketch"/"film"/"noir" all bias toward monochrome |
| Eye colour or ethnicity shifted | `do not change eye colour, skin tone or ethnicity` — this is Flash's known failure |
| Effect looks weaker than IG's | You wrote it as a filter; IG regenerates. Say `re-photograph this as…` instead of `add…` |
| Barely any change at all | **Your AVOID is cancelling your CHANGE.** Asking for diffusion while forbidding softness = nothing happens. Remove the contradicting clause. |
| Invented text / fake watermark | `do not invent, add or alter any text, logos or watermarks — leave unreadable text unreadable` |

| Poster/collage style came out with garbled fake text | The model invents lettering | Say "no gibberish lettering, no misspellings, no fake logos" — or drop text entirely and add it yourself |
| Face differs between panels in a collage/triptych | Each panel regenerated independently | Add "the face must be identical in all panels" near the TOP of the prompt, not the end |
| Selective-colour collage came out fully colour or fully mono | Layer instruction too vague | Name both layers explicitly: "background layer = B&W", "band = full colour", plus the offset |

| Told it "no window / no doorway" and the window got STRONGER | **Negative prompts do not delete objects.** Naming a thing raises its salience, and if it exists in the source photo the model reinforces it | **Positive substitution:** describe what the background *is* — "an open outdoor field at sunset, distant blurred trees, warm sky" — instead of listing what it must not be. Also crop tighter so less background survives |
| Asked for "natural skin texture and pores" and got blemishes | Texture wording overshoots into skin flaws | Say "natural skin texture, clean and even — no blemishes, spots or patchiness" |
| Layered/collage style looks like a filter, not a design | Missing the physical-edge and offset description | Follow the CANONICAL LAYERED-COMPOSITION RECIPE — all five parts, especially the torn edge, drop shadow and deliberate misalignment |

## Workflow
1. Start from the highest-quality original — never a screenshot of a screenshot.
2. Write your PRESERVE list once for your photo; reuse it in every prompt.
3. One effect per run.
4. Reject drift immediately — don't try to repair a bad generation, re-run from the source.
5. Stack by re-uploading the *approved* output as the new source.


---

# 🎛️ THE STYLE PICKER

`style-picker.html` is the practical front-end for everything in this file. Open it in a browser:

- **Filter** by type (single-image / multi-panel / layered), quality tier, or mood
- **Search** by name or tag
- **Toggle Photo A / Photo B** — every prompt instantly rewrites with the right PRESERVE block
- **Copy** any prompt to the clipboard with one click

It is generated from `prompts/styles.json`, which is the machine-readable source of truth: 19 styles,
each with `prompt_A`, `prompt_B`, and for multi-panel styles a `multi_A` / `multi_B` array of panel
prompts. To add a style, add a JSON entry and regenerate the picker.

## The three production types

| Type | Meaning | How to run it |
|---|---|---|
| **A · single-image** | One photo, one prompt | Paste and go |
| **B · multi-panel** | Reference is 3–4 video stills stacked | Render each panel separately, stitch with Pillow |
| **C · layered/graphic** | Collage, torn bands, eye-band overlays | One prompt, but describe every layer explicitly |

Mistaking a Type B reference for a Type A style was the single biggest error in this project.

---

# 🧩 CODE RECIPES — when NOT to use an image model

Some styles are **deterministic image editing**, not generation. Running them through an AI model
is strictly worse: it costs credits, and every pass risks drifting the face. Code does them exactly,
free, with the identity mathematically untouched.

**Rule of thumb: if the style only rearranges, crops, grades or overlays pixels that already exist
in the photo, do it in code.** Only use the image model when new content must be *invented*
(new lighting, a new background, a new art medium).

| Style | Tool | Why code wins |
|---|---|---|
| Eye Band Poster | `tools/template9.py` logic | AI kept redirecting the gaze toward the camera and reshaping the face. Code copies the original pixels, so the face cannot change. |
| Sepia Sunflower (Template 9) | `tools/template9.py` | Needs flat vector-style stickers and hard-edged bands — AI renders both poorly. |
| Any multi-panel stack | `tools/panels.py` | Panels must align perfectly and share one grade. |

## The single-source multi-panel problem — SOLVED

**The problem:** Type B references (refs 2, 4, 5, 6, 11) are 3–4 stills from a *video*, so each panel
shows a different pose. With only one photo you cannot get different poses.

**The wrong fix:** asking an AI model to invent new poses. It drifts the face every time, and the
panels stop looking like the same moment.

**The right fix:** stop trying to fake poses. Real editors build these from **different crops of the
same frame**. Refs 2 and 6 are largely crop-variation, not pose-variation. `tools/panels.py` offers
three strategies:

| Strategy | Panels | Looks like | Use when |
|---|---|---|---|
| `zoom` | 3 | A push-in: wide → medium → tight | You want a cinematic sequence |
| `detail` | 4 | B&W macro study: eye, ear+earring, lips, jaw | Matches ref 2 |
| `mixed` | 3 | Portrait, eyes-only band, portrait | Matches ref 6 |

```bash
python3 tools/panels.py          # builds all three from Photo A
```

**The critical parameter is zoom SPREAD.** The first attempt used 1.35 → 2.05 → 3.10 and the panels
looked nearly identical — the stack read as a mistake. Widening to 1.05 → 2.10 → 4.20 made each
panel obviously distinct. For `detail`, zoom factors must reach 7–9.5 so each panel isolates a
genuinely different feature.

**When you DO have 3–4 real photos** (or can afford 3–4 generations), that is still better — real
pose variation beats crop variation. Use the `multi_A` / `multi_B` prompts in `prompts/styles.json`,
then stitch with the same script. Crop-variation is the fallback that makes the style available from
a single photo.
