# Image Production Briefs — MassageChairsTested.com

Each inner page already ships a custom **inline-SVG hero illustration** (no action needed).
These briefs are for the *optional* atmospheric photograph slot on each page.

## How to add a photo to a page
1. Generate the image from the prompt below (Midjourney / DALL·E / Firefly / a photographer).
2. Export to WebP, ~1600×900, and save as `assets/photos/<key>.webp` (key shown per page).
3. In that page’s content file under `content/`, paste this where you want it (usually after the first `<h2>`):

```html
<figure class="page-photo">
  <img src="/assets/photos/<key>.webp" alt="<ALT>" loading="lazy" decoding="async" width="1600" height="900">
  <figcaption>Editorial photograph</figcaption>
</figure>
```
4. Run `python3 build.py`.

---

## /buying-guide/massage-chair-buying-checklist/
`key`: **buying-guide__massage-chair-buying-checklist**

**Alt text:** Handwritten checklist on cream paper with a fountain pen, several items ticked and a few rows still blank.

**Prompt:**

> Overhead flat-lay, warm matte natural side light falling across a sheet of cream laid paper resting on a pale oak desk. On the paper, a real handwritten checklist in dark fountain-pen ink with several small hand-drawn tick marks in the left margin; a few rows still blank. A capped fountain pen lies at a relaxed angle beside the sheet, next to a plain brass paperclip and a folded linen swatch in muted sage. Shallow depth of field, soft shadows, calm and considered mood, no screens, no people's faces. Real paper grain and ink texture visible. Strictly no logos, no brand names, no chair, no prices, no badges, no medical or clinical objects. Muted earthy palette of cream, oak, pine-green, terracotta. Aspect ratio 16:9.

---

## /showroom-guide/should-you-try-a-massage-chair-before-buying/
`key`: **showroom-guide__should-you-try-a-massage-chair-before-buying**

**Alt text:** A hand resting on the padded armrest of an unbranded reclining chair in warm natural light, suggesting trying the seat in person.

**Prompt:**

> Warm matte editorial photograph, 16:9, calm and analytical mood. A person's relaxed hand and forearm resting on the broad upholstered armrest of a neutral, unbranded reclining chair photographed at an angle that crops out any identifiable silhouette or logo. Soft natural side light from a window, warm paper-toned neutrals, real textures: woven fabric or matte leather grain, a wooden side table edge, a folded linen throw. Shallow depth of field with the hand and armrest seam in focus, the rest gently soft. No faces, no full chair model visible, no screens, no medical or clinical elements, no price tags or badges, no sales-floor or showroom signage. Documentary stillness, as if quietly testing how a seat feels. Color palette of warm sand, soft pine green accents in the background, muted terracotta. Natural film-like grain, no gloss, no drop shadows.

---

## /retailer-checklist/how-to-choose-a-massage-chair-retailer/
`key`: **retailer-checklist__how-to-choose-a-massage-chair-retailer**

**Alt text:** Hands over a ruled paper checklist with green pen tick marks beside a folded terms document, used to evaluate a seller.

**Prompt:**

> Warm matte overhead editorial photograph, 16:9, of a person's hands resting over an open paper notebook on a warm oak desk in soft natural window light. The visible page holds a simple hand-ruled checklist with a few neat fountain-pen tick marks in dark green ink; a fountain pen lies diagonally beside it. Surrounding props are calm and real: a folded plain printed document (a generic warranty-style page with no readable brand text), a stoneware mug, a pair of reading glasses, and a single dried eucalyptus sprig for texture. Palette of warm paper cream, sand, soft pine green, and muted terracotta. Shallow but honest depth of field, gentle shadows, no harsh contrast. Absolutely no logos, brand names, prices, badges, ratings, star icons, sales office, handshakes, clinical or medical objects, screens, or product chairs in frame. Quiet, analytical, trustworthy mood — the feeling of carefully evaluating a seller's terms on paper.

---

## /showroom-guide/what-makes-a-massage-chair-showroom-legitimate/
`key`: **showroom-guide__what-makes-a-massage-chair-showroom-legitimate**

**Alt text:** Hands writing a short checklist in a notebook beside a fountain pen on a sunlit wooden table.

**Prompt:**

> Atmospheric editorial photograph for a buying-guide page about what makes a massage-chair showroom legitimate. Warm matte natural light from a large window, calm and unhurried mood. Subject: a person's hands resting on an open paper notebook on a plain light-wood table, a fountain pen mid-note beside a short hand-written checklist, a simple ceramic mug of tea slightly out of focus. Real materials and textures: kraft paper, linen, brushed metal pen. Soft daylight, gentle shadows, shallow depth of field, neutral warm palette (paper cream, soft sand, muted pine green). No screens, no logos, no brand-identifiable furniture, no chairs in frame, no signage, no medical or clinical objects, no price tags or sale badges, no posed smiles, no handshakes, no sales-office setting. Documentary stillness, premium editorial restraint. Aspect ratio 16:9.

---

## /medical-claims/massage-chair-health-claims/
`key`: **medical-claims__massage-chair-health-claims**

**Alt text:** Hands use a magnifier to read the printed wording on a small paper product tag.

**Prompt:**

> Warm matte editorial still life, 16:9, soft natural window light from the left, calm and analytical mood. A pair of hands (neutral, no jewelry, sleeves of a plain oatmeal knit) holds a small folded paper product hang-tag printed with several lines of generic body text over a warm recycled-paper surface; a simple brass-rimmed reading magnifier rests across one line of the wording, gently enlarging a single phrase. Beside the tag, two unbranded blank kraft tags lie on the table — one tinted soft pine-green, one tinted soft amber — suggesting words sorted into categories. Real materials: textured paper, faint pencil annotation in the margin, a fountain pen laid to one side. Shallow depth of field, focus on the magnified wording. Palette of warm sand, ink-charcoal, muted pine and calm amber. NO logos, NO brand names, NO massage chair, NO medical or clinical objects, NO before/after, NO prices or badges, NO stock smile, NO office or sales setting. Quiet, premium, field-guide feel.

---

## /warranty-service-delivery/massage-chair-warranty-delivery-service-guide/
`key`: **warranty-service-delivery__massage-chair-warranty-delivery-service-guide**

**Alt text:** Overhead desk scene: a sealed warranty document, a service wrench, and a plain delivery box arranged as an after-purchase sequence.

**Prompt:**

> Warm, matte editorial still life shot from directly overhead on a warm paper-toned desk in soft natural window light, 16:9. Composition: a calm flat-lay sequence reading left to right — a folded paper document with a clean embossed (blind) circular seal on the lower right, a single well-worn but cared-for metal adjustable wrench resting on a folded grey cloth, and a plain unbranded kraft cardboard box with one strip of paper tape. A pair of real adult hands, sleeves rolled, gently resting near the wrench mid-frame, unhurried. Muted palette of warm sand, ink-grey, pine-green cloth accent, terracotta thread on the seal ribbon. Real material textures: matte paper grain, brushed metal, corrugated kraft. Shallow depth of field, gentle falloff. NO logos, brand marks, model names, prices, stickers, badges, stars, screens, or text overlays; NO retail or office setting; NO medical or clinical objects; NO before/after; NO stock smiles or faces. Quiet, analytical, premium field-guide mood.

---

## /online-vs-showroom/should-you-buy-a-massage-chair-online-or-in-store/
`key`: **online-vs-showroom__should-you-buy-a-massage-chair-online-or-in-store**

**Alt text:** Closed laptop beside fabric swatches and an open notebook listing the same plain comparison questions for either buying path.

**Prompt:**

> Warm matte editorial still life, 16:9, natural window light from the left, calm and analytical mood. A real wooden tabletop in warm paper-toned tones holds two objects side by side that quietly echo "two paths to one decision": on the left, a closed laptop or tablet resting flat with a plain notebook beside it; on the right, a small set of physical fabric and material swatches (linen, leather alternative, mesh) fanned out, with a pair of hands resting near them mid-thought. A single open notebook between the two shows a short handwritten list of plain questions (legible but generic, e.g. "fit, support, return policy"). Shallow depth of field, soft shadows, no harsh contrast. Real textures: paper grain, wood, woven fabric. Neutral palette of warm sand, soft pine green accent, muted terracotta. STRICTLY AVOID: any massage chair (especially identifiable models), brand logos, screens showing branded sites, sales office or retail signage, handshakes, stock smiles, prices, badges, ratings, medical or clinical elements, before/after framing. The image should feel like a quiet field-guide page about making a careful comparison, not a sales scene.

---

## /reviews-comparisons/how-to-read-massage-chair-reviews/
`key`: **reviews-comparisons__how-to-read-massage-chair-reviews**

**Alt text:** Overhead view of a hand sketching a baseline with three spaced ink dots, showing how one rating averages several scores.

**Prompt:**

> Warm matte editorial still life, 16:9, shot from directly overhead on a sheet of soft cream paper in calm natural window light (gentle directional shadow, no harsh contrast). On the paper, a person's hand (relaxed, neutral, no jewelry or branding) rests beside an open dot-grid notebook where a fountain pen has sketched a single horizontal baseline with three small ink dots placed at different points along it, plus a tiny hand-printed star in the margin. A few loose index cards with faint handwritten column headings sit slightly fanned nearby, intentionally unbranded and unreadable as any product. Muted palette of warm paper, deep ink, and a single terracotta accent (a thin ribbon or pencil). Real paper texture and pen ink visible. Mood is quiet, analytical, unhurried — like a careful reader breaking an average back into its parts. No screens, no logos, no charts with brand names, no star-rating UI, no faces, no clinical or office setting.

---

## /local/california-massage-chair-showrooms/
`key`: **local__california-massage-chair-showrooms**

**Alt text:** Hands smoothing a folded regional paper map beside a compass and pen, used for planning showroom visits.

**Prompt:**

> Warm matte editorial still life, 16:9, soft natural window light from the left, calm and unhurried mood. A weathered folded paper road map of a coastal region rests on a warm paper or light oak surface, partially unfolded so the creases catch gentle shadow. A pair of relaxed hands (neutral, no jewelry branding) lightly smooths one corner of the map; nearby sit a small brass compass and a fountain pen, suggesting orientation and planning. Muted sand, pine-green, and terracotta tones echo a quiet field-guide aesthetic. Shallow depth of field, fine paper grain and ink texture visible. No screens, no store interiors, no signage or readable place names, no logos, no people's faces, no chairs. Documentary, tactile, premium. Photographed top-down at a slight angle, ample negative space at right for text overlay.

---

## /local/bay-area-massage-chair-showrooms/
`key`: **local__bay-area-massage-chair-showrooms**

**Alt text:** Hand with a fountain pen over a folded regional bay-area map, marking three separate areas to visit.

**Prompt:**

> Atmospheric editorial still life, warm matte natural light from a side window, 16:9. A calm overhead-angled view of a worn paper regional road map of a coastal bay area resting on a warm oak table, softly creased along the folds. A person's hand (natural skin, no jewelry branding) rests lightly at the edge, a fine fountain pen laid diagonally across the map as if mid-note. Three small plain brass map pins or pencil ticks mark separate inland areas near the water's edge. Muted palette of sand, paper cream, pine green, and terracotta; shallow depth of field, gentle grain, no harsh shadows. Real materials only — paper, ink, wood, metal pins. No screens, no signage, no logos, no chairs, no storefronts, no text legible enough to read as a brand, no clinical or medical objects, no people's faces. Quiet, considered, field-guide mood.

---

## /reviews-comparisons/best-massage-chair-brands-to-try-before-buying/
`key`: **reviews-comparisons__best-massage-chair-brands-to-try-before-buying**

**Alt text:** Hand squaring a column of blank index cards beside three labelled tabs for comparing fit, warranty and service.

**Prompt:**

> Warm matte editorial still life, 16:9, soft natural side light from a window on a warm overcast morning. A flat-lay on warm paper or unbleached linen: a small set of identical blank index cards or library catalogue cards arranged in a neat vertical column, each card plain and unbranded with a hand-inked dash and a single terracotta dot in the margin. Beside them, three small folded paper tabs or hand-lettered slips reading FIT, WARRANTY, SERVICE in calm muted ink. A real fountain pen rests at an angle, a person's hand (warm neutral skin tone, no jewelry, mid-gesture) lightly squaring the stack of cards. Visible paper grain, faint deckled edges, subtle natural shadow. Muted palette of sand, pine green and terracotta. No screens, no logos, no chairs, no brand marks, no stars or scores, no price tags, no office or clinical setting. Quiet, analytical, human. Shallow depth of field, honest textures, no gloss, no drop-shadow drama, no gradients.

---

## /editorial-standards/
`key`: **editorial-standards**

**Alt text:** Open brass compass with a steady needle resting beside a fountain pen on a ruled paper baseline.

**Prompt:**

> Atmospheric editorial still life, 16:9, warm matte natural light from a soft side window. On a sheet of warm cream paper sits a small worn brass field compass, lid open, needle settled and steady; beside it a fountain pen rests on a faint pencil baseline ruled straight across the page, with a folded linen tape measure and a single pinecone as quiet field-guide props. Real textures: aged brass patina, fibrous paper grain, ink sheen. A hand may rest lightly at the page edge, calm and unhurried, fingertips only. Muted palette of paper cream, pine green, and terracotta accents echoing the page. No screens, no chairs, no logos or text, no clinical or medical objects, no sales setting, no badges or prices. Shallow depth of field, gentle shadow, editorial and contemplative mood conveying careful, principled judgement.

---

## /review-methodology/
`key`: **review-methodology**

**Alt text:** Hands with a fountain pen annotating a notebook beside a folding ruler and calipers used to measure material attributes

**Prompt:**

> Overhead 16:9 editorial photograph on warm matte paper in soft natural daylight, calm and analytical. A person's hands (neutral, unbranded sleeves) hold a fine fountain pen poised over an open paper notebook on which a clean ruled measurement sketch and a few short handwritten annotations are visible. Beside the notebook lie a brass folding ruler and a small set of calipers resting on textured cream cardstock, plus a pale fabric swatch and a coil-spring sample as understated material references. Muted palette of warm paper, ink black, soft pine green and terracotta accents. Real textures: grain of paper, brushed metal, woven cloth. No screens, no charts with numbers ranked, no logos, no chairs, no clinical or medical objects, no price tags, no stock smile. Shallow depth of field, gentle shadow, honest documentary feel, like a quiet field guide being written.

---

## /showroom-verification-methodology/
`key`: **showroom-verification-methodology**

**Alt text:** Checklist on a wooden clipboard with a pen, in front of a softly blurred unbranded storefront window

**Prompt:**

> Warm matte editorial photograph, 16:9, natural window light falling across a calm wooden desk. A plain paper checklist on a simple wooden clipboard rests at a slight angle, a few handwritten ticks visible in dark ink, a fountain pen laid beside it. In soft focus behind, an out-of-focus shopfront window with neutral, unbranded glazing and warm interior light. Real textures: matte paper grain, pale oak grain, brushed metal clip. Muted palette of warm paper, sand, soft pine green and terracotta accents. No logos, no screens, no people's faces, no chairs, no signage text, no badges or prices. Quiet, analytical, premium, documentary feel. Shallow depth of field, gentle shadows, no harsh contrast.

---

## /disclosure/
`key`: **disclosure**

**Alt text:** Open notebook with handwritten ink notes and a fountain pen, a hand pausing at the page edge in warm light.

**Prompt:**

> Warm matte editorial still life, 16:9, natural window light raking from the left across a warm paper desk. Centre: an open hardback notebook with hand-written ink notes on cream pages, a fountain pen resting in the gutter, and a small folded paper card beside it. A second hand (real, relaxed, no jewellery, neutral skin tones) rests lightly at the page edge as if pausing mid-read. Muted palette of warm paper, pine-green cloth binding, and a single terracotta bookmark ribbon. Shallow depth of field, soft shadows, slight paper grain and pen-ink texture. Calm, honest, contemplative mood. NO screens, NO money or coins, NO logos or brand marks, NO massage chairs, NO clinical or medical objects, NO charts or badges, NO faces, NO sales setting. Quiet field-guide aesthetic: precise, human, unhurried.

---

## /medical-disclaimer/
`key`: **medical-disclaimer**

**Alt text:** Cream paper note with a fountain pen and a small green leaf on a warm wooden desk in soft daylight.

**Prompt:**

> Warm matte editorial still life shot in soft natural window light, 16:9. A single sheet of cream textured paper rests on a warm oak desk beside a closed fountain pen and a sprig of fresh eucalyptus or a small green leaf laid gently on the corner of the page. The paper carries faint handwritten lines (illegible, no readable text, no logos, no medical symbols). A person's relaxed hand rests lightly at the edge of the desk, unhurried and calm. Shallow depth of field, gentle shadows, muted sand-and-pine palette, no screens, no clinical or office setting, no branding, no charts or badges. Quiet, reassuring, contemplative mood — the feeling of pausing to read carefully before deciding. Authentic materials and texture, film-like grain.

---

## /correction-policy/
`key`: **correction-policy**

**Alt text:** Hands marking a correction on a printed text proof with a fountain pen on warm paper

**Prompt:**

> Warm matte editorial still life, 16:9, natural window light from the left, calm and quiet mood. A pair of hands at the edge of frame using a fine fountain pen to mark a small printed proof sheet of plain body text laid on a warm paper-toned desk; a faint pencil caret and a light terracotta-ink correction mark sit between two lines of text. Nearby: a folded clean galley page, a soft eraser, and a small ruler, all real tactile materials with visible paper grain. Shallow depth of field, soft shadows, no harsh contrast. Muted palette of warm sand, ink black, pine green and a touch of terracotta. No screens, no logos, no brand names, no charts or ratings, no clinical or medical objects, no people's faces, no smiles, no price tags. Documentary, understated, premium craft feel.

---

---

## SITE-WIDE: Default social share image (og:image)
`save as`: **assets/og/og-default.png** — exactly **1200 × 630 px**, PNG or JPG (NOT svg/webp; social platforms need raster).
Referenced by every page's `og:image` / `twitter:image`. Until this file exists, social previews fall back to no image.

**Prompt:**

> Clean editorial brand card, 1200×630, warm off-white paper background (#FBFAF6) with subtle paper grain. Centered: the wordmark "MassageChairsTested.com" in a refined serif, deep charcoal (#1C1F1D), with a small pine-green dot before it; below it a short mono-type tagline "An independent massage chair buying guide" in muted grey. A thin pine→terracotta hairline rule under the wordmark. Generous margins, calm, premium, magazine-like. No photo, no chair, no logos other than the wordmark, no people, no prices, no badges. Muted palette: cream, charcoal, pine green (#1E5A4C), terracotta (#B65F40). Flat, high-contrast for legibility as a thumbnail.
