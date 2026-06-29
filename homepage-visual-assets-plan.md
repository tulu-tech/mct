# Homepage Visual Assets Plan — MassageChairsTested.com

**Page:** https://massagechairstested.com/ (`content/home.html` → `index.html` via `build.py`)
**Date:** 2026-06-28
**Scope chosen:** Full set — **10 photographs** (within the 8–12 brief), plus 2 optional extras.

## Note on approach
The homepage already ships 8 bespoke inline-SVG diagrams (hero board, trailhead, interactive checklist, Fit Map, Trust Ledger, Honest Spread, Two Doors, California map, Field Index chips). The 10 photos below are **complementary**: each adds human warmth / real-world / tactile texture the diagram in that section can't, and motifs are varied down the page to avoid a repetitive "stock gallery" feel.

## Style spine (every prompt)
Warm matte editorial photograph, 16:9, ~1600×900. Calm, considered, premium, consumer-guide mood. Soft natural window light. Real textures (paper, linen, pale oak, stoneware, matte fabric). Shallow depth of field. Muted earthy palette: cream, warm sand, soft pine green, muted terracotta. Natural film-like grain, no gloss, no heavy drop shadows. **No faces** (or soft/cropped — never a staged smile).

**Hard negatives (every image):** no logos, no brand names, no readable text on documents, no prices, no badges, no star ratings, no awards, no sales-floor/storefront signage, no medical or clinical objects, no doctors, no before/after, no ecommerce product grids, no discount banners, no recognizable real chairs.

## File + folder convention
Save to `assets/photos/<file-name>` — under `assets/` as instructed, in a `photos/` subfolder matching the codebase convention. Generate and save **one at a time, in order**, preserving whatever extension ChatGPT returns.

---

### 1 — `home-considered-decision.webp`  ·  motif: atmospheric mood
**Section:** "The Short Answer" (text-only, below hero) · **Placement:** full-width `.page-photo` band after the Short Answer paragraph.
**Alt:** *Calm moment of a buyer pausing to consider a major purchase before shopping*
**Prompt:**
> Warm matte editorial photograph, 16:9, calm and considered mood. Close atmospheric interior detail in soft natural morning window light: a person's relaxed hand resting on a closed cloth-bound notebook on a pale oak surface near a window, a stoneware mug and a single dried eucalyptus sprig beside it, a softly blurred warm room behind. The feeling of quietly slowing down before an important, unhurried decision. No face in frame. Shallow depth of field, real paper and linen texture, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural film-like grain, no gloss. Strictly no logos, no brand names, no readable text, no prices, no badges, no screens, no massage chair, no product, no medical or clinical objects, no sales floor.

### 2 — `home-choosing-a-path.webp`  ·  motif: human moment
**Section:** "Start Here: Choose Your Buying Path" (has Trailhead fork SVG) · **Placement:** after the buyer-path `.card-grid`, before "Last updated."
**Alt:** *A buyer leafing through a plain printed guide while deciding where to begin*
**Prompt:**
> Warm matte editorial photograph, 16:9, calm and curious mood. A person's hands gently leafing through a single plain, unbranded printed booklet at a sunlit pale-oak table; one or two more plain sheets rest nearby as if choosing where to start. Soft natural side light, warm neutrals, real paper texture, a stoneware mug just in frame. No face, no readable text on the pages, no logos. Shallow depth of field, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural grain, no gloss. Strictly no brand names, no prices, no badges, no screens, no product chairs, no medical objects, no sales floor.

### 3 — `home-buying-checklist.webp`  ·  motif: paper / checklist
**Section:** "What's on a Buying Checklist?" (has interactive checklist tool) · **Placement:** beside/after the `theme-list` checklist tool, or after the feature block.
**Alt:** *A handwritten massage chair buying checklist with several items ticked off*
**Prompt:**
> Overhead flat-lay, warm matte natural side light across a sheet of cream laid paper on a pale oak desk. On the paper, a real handwritten checklist in dark fountain-pen ink with several small hand-drawn tick marks in the left margin; a few rows still blank. A capped fountain pen lies at a relaxed angle beside the sheet, next to a plain brass paperclip and a folded linen swatch in muted sage. Shallow depth of field, soft shadows, calm considered mood, no screens, no faces. Real paper grain and ink texture. Strictly no logos, no brand names, no readable words, no chair, no prices, no badges, no medical objects. Muted palette of cream, oak, pine-green, terracotta. 16:9.

### 4 — `home-try-in-person.webp`  ·  motif: tactile chair
**Section:** "Should You Try… Before Buying?" (has Fit Map SVG) · **Placement:** after the "What comfort testing…" H3, near the Fit Map.
**Alt:** *A hand resting on the padded armrest of an unbranded reclining chair, suggesting testing comfort in person*
**Prompt:**
> Warm matte editorial photograph, 16:9, calm and analytical mood. A person's relaxed hand and forearm resting on the broad upholstered armrest of a neutral, unbranded reclining chair, photographed at an angle that crops out any identifiable silhouette or logo. Soft natural side light, warm paper-toned neutrals, real textures: woven fabric or matte leather grain, a wooden side table edge, a folded linen throw. Shallow depth of field with the hand and armrest seam in focus, the rest gently soft. No face, no full chair model visible, no screens, no medical elements, no price tags or badges, no showroom signage. Documentary stillness, as if quietly testing how a seat feels. Palette of warm sand, soft pine green accents, muted terracotta. Natural grain, no gloss, no drop shadows.

### 5 — `home-legit-showroom-space.webp`  ·  motif: interior / space
**Section:** "What Makes a Showroom Legitimate?" (has Trust Ledger SVG) · **Placement:** after the section-head lead, before the Trust Ledger figure.
**Alt:** *A calm, uncluttered space with room to sit and test a chair unhurried*
**Prompt:**
> Warm matte editorial photograph, 16:9, calm and spacious mood. A quiet, well-lit, uncluttered neutral interior with warm natural light falling across a pale wood floor and a soft, unbranded single seat positioned out of focus in the background, plenty of open room around it. The feeling of a calm, legitimate place where you'd be free to sit and test something unhurried. No face, no signage, no logos, no price tags, no posters, no other products. Shallow depth of field, real textures, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural grain, no gloss. Strictly no brand names, no badges, no sales floor signage, no medical objects.

### 6 — `home-evaluate-seller.webp`  ·  motif: paper / terms
**Section:** "Choose a Retailer You Can Trust" (text + table, no diagram) · **Placement:** after the "A short retailer checklist" list.
**Alt:** *Evaluating a seller's written warranty and service terms against a checklist*
**Prompt:**
> Warm matte overhead editorial photograph, 16:9, of a person's hands resting over an open paper notebook on a warm oak desk in soft natural window light. The visible page holds a simple hand-ruled checklist with a few neat fountain-pen tick marks in dark green ink; a fountain pen lies diagonally beside it. Calm real props: a folded plain printed document (generic terms-style page, no readable brand text), a stoneware mug, reading glasses, a single dried eucalyptus sprig. Palette of warm paper cream, sand, soft pine green, muted terracotta. Shallow but honest depth of field, gentle shadows. Absolutely no logos, brand names, prices, badges, ratings, star icons, handshakes, clinical objects, screens, or product chairs. Quiet, analytical, trustworthy mood.

### 7 — `home-reading-reviews.webp`  ·  motif: reading / patterns
**Section:** "How Do You Read Reviews Without Being Misled?" (has Honest Spread SVG) · **Placement:** after the two intro paragraphs, before the Honest Spread figure.
**Alt:** *Reading reviews carefully and noting patterns rather than reacting to one comment*
**Prompt:**
> Warm matte editorial photograph, 16:9, calm and discerning mood. On a pale oak table in soft natural light: a tablet held in one hand showing only abstract neutral grey content blocks and lines (no readable text, no stars, no ratings, no interface logos), an open notebook beside it where a hand is jotting short marks as if noting patterns, a fountain pen and stoneware mug nearby. No face. The feeling of reading many opinions slowly and looking for patterns. Shallow depth of field, real textures, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural grain, no gloss. Strictly no logos, no brand names, no readable review text, no star icons, no prices, no badges, no medical objects, no product chairs.

### 8 — `home-online-or-showroom.webp`  ·  motif: objects / the choice
**Section:** "Buy Online or in a Showroom?" (has Two Doors SVG) · **Placement:** after the intro paragraph, before the Two Doors figure (or after the comparison table).
**Alt:** *Weighing two routes to buy: shopping from home versus going to test in person*
**Prompt:**
> Warm matte editorial still life, 16:9, calm and deliberative mood. On a pale oak surface in soft natural light: a slim closed laptop on the left and a set of car keys with a folded plain neutral paper map on the right, a stoneware mug between them — quietly suggesting two routes, deciding from home or going out to test in person. No face, no screen content, no logos, no readable map labels. Shallow depth of field, real textures, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural grain, no gloss. Strictly no brand names, no prices, no badges, no storefront, no medical objects, no product chairs.

### 9 — `home-reading-claims.webp`  ·  motif: close detail / caution
**Section:** "Interpret Health and Wellness Claims?" (claim-compare cards, no photo) · **Placement:** after the "Wellness vs medical-sounding claims" paragraph, before the claim-compare cards. Keep calm and serious.
**Alt:** *Reading product claim wording slowly and carefully before relying on it*
**Prompt:**
> Warm matte editorial close detail, 16:9, calm and careful mood. Soft natural light on a pale oak surface: a person's hand resting beside a plain, unbranded printed card or hang-tag with only faint, unreadable lines of text, as if pausing to read the wording carefully before relying on it. A fountain pen rests nearby. No face. Serious, unhurried, neutral tone — not clinical, not alarming. Shallow depth of field, real paper texture, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural grain, no gloss. Strictly no logos, no brand names, no readable claims, no medical or clinical objects, no doctors, no prices, no badges, no product chairs.

### 10 — `home-plan-local-visits.webp`  ·  motif: planning / objects
**Section:** "Find Local Showroom Guidance?" (has California map SVG) · **Placement:** after the California / Bay Area `.card-grid`, before the independence note.
**Alt:** *Planning questions to ask before visiting local massage chair showrooms*
**Prompt:**
> Warm matte overhead editorial photograph, 16:9, calm planning mood. On a pale oak table in soft natural light: an open notebook with a short handwritten list of questions (handwriting soft and not clearly legible), a fountain pen, a set of car keys, a pair of sunglasses, a stoneware mug of coffee. The feeling of planning a few in-person visits before heading out — organized and unhurried. No face. Shallow depth of field, real paper and metal textures, gentle shadows. Muted earthy palette of cream, warm sand, soft pine green, muted terracotta. Natural grain, no gloss. Strictly no logos, no brand names, no readable addresses, no map pins, no storefront, no real place names, no prices, no badges, no medical objects, no product chairs.

---

## Optional extras (green-light if wanted)
- **11 — `home-compare-brands.webp`** (Brands / Field Index): overhead of a few plain unlabeled spec cards laid in a neutral grid being compared side by side, no brand names — "compare every brand the same way."
- **12 — `home-decide-with-confidence.webp`** (Final CTA, dark block): a closed notebook with pen resting on top and a folded plain checklist beside it — preparation finished, ready to decide.

## Generation order (Chrome connected)
In the Growth OS ChatGPT project: send `1`, wait, save+rename to `assets/photos/home-considered-decision.webp`, then `2` … through `10`. One at a time.

## Placement order (after images exist)
Insert each `.page-photo` figure into `content/home.html` at the placement above with its alt text → `python3 build.py` → verify desktop + mobile.
