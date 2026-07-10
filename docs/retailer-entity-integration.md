# Retailer Entity Integration — Internal Working Document

**Not a public page.** Lives in `docs/`, which the build (`build.py`) does not process. Internal planning, verified-fact ledger, templates, and per-page implementation tracker for the disclosed retailer-example integration.

- **Retailers referenced (public names only on the site):** Massage Chairs & More (internal code **MCM**) and House of Massage Chairs (internal code **HCM**). The abbreviations MCM/HCM are for this document only and must **never** appear on public pages.
- **Disclosure posture (UPDATED 2026-07-10 per owner):** NO business-relationship / commercial-benefit statement is published on the site. Retailer examples are presented as NEUTRAL editorial mentions ('public examples to verify, not rankings or endorsements'). Changing facts (inventory, price, hours, warranty, delivery, service) must be verified directly.
- **Link posture:** editorial, crawlable follow links (`rel="noopener"` for `target="_blank"`), paired with visible on-page disclosure + `/disclosure/`. If any placement becomes paid/affiliate/compensated per-click or per-sale, switch those links to `rel="sponsored noopener"` (one-line change — all retailer links share the `data-retailer` convention). See "Open items."

---

## 1. Verified retailer facts (checked live 2026-07-10)

### Massage Chairs & More — massagechairsandmore.com
All four showrooms publicly list the **same five brands** — OHCO, Panasonic, Positive Posture, D.Core, Koyo — and each page promotes try-before-buy, white-glove in-home delivery + professional setup, and financing.

| Location (public framing) | Region | Showroom page (verified live) |
|---|---|---|
| Santa Clara (flagship) — Westfield Valley Fair | South Bay | `/pages/massage-chairs-santa-clara-showroom` |
| Pleasanton — Stoneridge Mall | East Bay / Tri-Valley | `/pages/pleasanton-massage-chairs-showroom` |
| Daly City — Serramonte Center (closest to SF) | Peninsula / SF proximity | `/pages/massage-chairs-daly-city-showroom` |
| Sacramento region — Roseville / Galleria | Greater Sacramento | `/pages/massage-chairs-sacramento-showroom` |
| Contact & showrooms hub | Statewide | `/pages/contact` |

Brand collections (verified live, current models):
| Brand | Verified current models | Collection URL |
|---|---|---|
| Panasonic | MAN1, MAK1, MAF1 | `/collections/panasonic-massage-chairs` |
| OHCO | R6, M8 Neo, M8 Neo LE (no "outlet" program shown) | `/collections/ohco-massage-chairs` |
| D.Core | D.Core 2, Cirrus JP, Stratus JP | `/collections/d-core-massage-chairs` |
| Koyo | 303TS (Made-in-Japan positioning) | `/collections/koyo-massage-chairs` |
| Positive Posture | DualTech Pro AI 4D, DualTech 4D Dual, Brio Sport, Brio+, Solara | `/collections/positive-posture-massage-chairs` |

### House of Massage Chairs — houseofmassagechairs.com
Two showrooms; multi-brand floor of **9 global brands** (Osaki, Infinity, Fujiiryoki, Cozzia, Bodyfriend, Kyota, Ogawa, JP Medics + Daiwa mentions). Public pages promote trying 35+ chairs side by side, full manufacturer warranty coverage, and white-glove delivery + in-home setup.

| Location (public framing) | Region | Showroom page (verified live) |
|---|---|---|
| San Jose — Westfield Oakridge Mall, 925 Blossom Hill Rd (Silicon Valley flagship) | South Bay / Silicon Valley | `/pages/san-jose-showroom` |
| Pleasanton — Stoneridge Mall | East Bay / Tri-Valley | `/pages/pleasanton-showroom` |
| Store hub | Bay Area | `/pages/our-store` |
| Brands compared | Bay Area | `/pages/massage-chair-brands-compared` |

Brand collections (verified live 2026-07-10, current models — note several diverge from older model names in the brief; use these verified names):
| Brand | Verified current models | Collection URL |
|---|---|---|
| Osaki | Broad range (17+): OS-Pro 4D DuoMax, OP Kairos 4D LT, Grand Duo 4D | `/collections/osaki` |
| Infinity | Riage 4D, Smart Chair X3, Gen Max 4D, Luminary Syner-D (NOT older Riege X3 / IT-8500) | `/collections/infinity` |
| Kyota | Genki M380, Yugana M780, Hatsumei M900, Joubu M880, Nokori M980 | `/collections/kyota` |
| Ogawa | Master Drive Duo, Active XL 3D (only these two shown) | `/collections/ogawa` |
| Cozzia | Quantum (CZ-800), Qi SE, Qi XE Pro Duo, Zen 2, Zen Duo | `/collections/cozzia` |
| Bodyfriend | Falcon SV, Phantom Rovo, Pharaoh Q, Palace Neo (Rovo walking tech) | `/collections/bodyfriend` |
| Fujiiryoki | Cyber Relax Ai / Elite / Pro, MR-6000 Calm Plus | `/collections/fujiiryoki` |

**Fact-safety notes:**
- MCM "Sacramento" showroom is physically in **Roseville** → always frame as "Sacramento-region (Roseville)".
- Both retailers publish a Pleasanton showroom at **Stoneridge Mall**. Do **not** print identical suite numbers as if two independent stores; frame each as "in Pleasanton (Stoneridge Mall)" and tell readers to confirm which retailer's floor + exact suite.
- Never state exact counts of showrooms/models/brands/hours unless the live page supports it; prefer durable wording ("currently lists", "publishes showroom information for", "confirm before visiting").

---

## 2. Reusable copy blocks

**Full disclosure note** (disclosure page + major comparison modules):
> Retailer examples are included to help readers apply the same buying criteria to real public showroom information. Named retailers are public examples to verify, not rankings or endorsements. Verify current availability, pricing, warranty, service and delivery directly.

**Short disclosure note** (`.retail-note`, near any retailer module — single retailer variant):
```html
<p class="retail-note"><b>Note:</b> Massage Chairs &amp; More is included as a public showroom example to verify, not a ranking or endorsement — confirm current models, warranty, delivery and service directly.</p>
```
(Swap "Massage Chairs &amp; More" ⇄ "House of Massage Chairs"; use "and House of Massage Chairs" on pages that reference both.)

**Retailer link pattern** (the ONLY way retailer links are written — carries analytics data-attrs):
```html
<a href="https://massagechairsandmore.com/collections/panasonic-massage-chairs"
   class="rlink" data-retailer="mcm" data-intent="brand_availability"
   data-brand="Panasonic" data-location="California"
   target="_blank" rel="noopener">current Panasonic showroom availability at Massage Chairs &amp; More</a>
```
`data-retailer` = `mcm` | `hcm`. `data-intent` = one of the intent clusters below. `data-brand`/`data-location` optional but set where known.

**Retailer example card** (`.retailer-card`, informational — no logos/prices/ratings/CTAs like "shop"):
```html
<article class="retailer-card">
  <h3>Massage Chairs &amp; More</h3>
  <p class="rc-loc">Public California showroom example</p>
  <p>Publishes showroom pages for Santa Clara (South Bay), Pleasanton (East Bay), Daly City (Peninsula) and the Sacramento region, and currently lists Panasonic, OHCO, D.Core, Koyo and Positive Posture.</p>
  <p><b>Confirm before visiting:</b></p>
  <ul class="rc-verify">
    <li>Which exact models are on the floor today</li>
    <li>Warranty provider, parts and labor terms in writing</li>
    <li>Delivery level, installation and packaging removal</li>
    <li>Return window, restocking and cancellation terms</li>
  </ul>
  <a class="rc-cta rlink" data-retailer="mcm" data-intent="local_showroom" data-location="California"
     href="https://massagechairsandmore.com/pages/contact" target="_blank" rel="noopener">Review current showroom information <span class="arrow" aria-hidden="true">&rarr;</span></a>
</article>
```

**External-link CTA phrasings (allowed):** "Review current showroom information", "Check current brand availability", "Verify location and floor models", "Review the retailer's current brand page". **Banned CTAs:** buy now, shop now, book now, best dealer, top-rated, recommended dealer, #1/number-one showroom, click here.

---

## 3. Analytics — `retailer_outbound_click`
GA4 (`gtag`, id `G-18J1NXB880`) already site-wide. A delegated listener in `assets/app.js` fires on click of any `a[data-retailer]`. Parameters: `retailer`, `source_page`, `destination_url`, `intent_cluster`, `brand`, `location`, `anchor_text`. Retailer values `mcm`/`hcm`. Intent clusters: `local_showroom`, `where_to_buy`, `brand_availability`, `try_before_buy`, `retailer_verification`, `warranty_service_delivery`, `brand_comparison`.

---

## 4. Global rules
- **Max one retailer backlink per brand page.** Local guides may carry several *only if each serves a different location/task* (cap: 2 MCM + 2 HCM on Bay Area). Once linked in a section, later mentions stay unlinked.
- **No retailer links in header, footer, main nav, or on the homepage hero.** No retailer logos anywhere.
- **Never** say: best place to buy, recommended dealer, top-rated/number-one showroom, guaranteed authentic, every model available, lowest price, "100% independent".
- **Never** connect a retailer link to a medical-condition answer, or to a "problems/complaints" section.
- No Review/AggregateRating/Rating/LocalBusiness/Product/Offer schema for retailers. No fake stars/awards/badges.
- Answer blocks: question as H2/H3 → direct answer in sentence 1 → entity (retailer/location/brand) early → practical criteria → verification sentence → one external + optionally one internal link. 50–110 words. No duplicated paragraphs across pages.

---

## 5. Per-page implementation tracker

Status: ☐ pending · ◑ in progress · ☑ done

| # | Page (URL) | Search intent | Retailer(s) | Brand/Location | Outbound → anchor | Disclosure | Status |
|---|---|---|---|---|---|---|---|
| P1 | `/disclosure/` | trust | none (policy) | — | none | Full note + new H2 | ☑ |
| P2 | `/editorial-standards/` | trust | none | — | none | reference | ☑ |
| P3 | `/correction-policy/` | trust | none | — | none | reference | ☑ |
| P4 | `/` (home) | brand/nav | none (internal card only) | — | internal → where-to-buy | soften independence | ☑ |
| P5 | `/buying-guide/where-to-buy-a-massage-chair/` (NEW) | where to buy a massage chair | MCM + HCM | CA / Bay Area | 2 cards → `/pages/contact` (MCM), `/pages/our-store` (HCM) | Full + short notes | ☑ |
| P6 | `/local/california-massage-chair-showrooms/` | California showrooms | MCM + HCM | statewide | MCM `/pages/contact`, HCM `/pages/our-store` (1 each) | short note | ☑ |
| P7 | `/local/bay-area-massage-chair-showrooms/` | Bay Area showrooms | MCM + HCM | SJ/SC/Pleasanton/Daly City | ≤2 MCM (Santa Clara, Daly City) + ≤2 HCM (San Jose, Pleasanton) | short note | ☑ |
| P8 | `/showroom-guide/should-you-try-a-massage-chair-before-buying/` | try before buying | MCM + HCM | CA | 1 MCM + 1 HCM | short note | ☑ |
| P9 | `/showroom-guide/what-makes-a-massage-chair-showroom-legitimate/` | legit showroom | MCM + HCM | CA | 1 MCM + 1 HCM | short note | ☑ |
| P10 | `/retailer-checklist/how-to-choose-a-massage-chair-retailer/` | choose a retailer | MCM + HCM | CA | 1 MCM + 1 HCM | short note | ☑ |
| P11 | `/warranty-service-delivery/massage-chair-warranty-delivery-service-guide/` | warranty/service/delivery | MCM + HCM | CA | 1 MCM + 1 HCM | short note | ☑ |
| P12 | `/reviews-comparisons/best-massage-chair-brands-to-try-before-buying/` | brands to try | MCM + HCM | 12 brands | 1 MCM + 1 HCM (intro only) | note above matrix | ☑ |
| P13 | `/online-vs-showroom/should-you-buy-a-massage-chair-online-or-in-store/` | online vs store | none | — | internal → where-to-buy | reference | ☑ |
| P14 | `/reviews-comparisons/how-to-read-massage-chair-reviews/` | reading reviews | none | — | internal only | reference | ☑ |
| P15 | `/review-methodology/` | methodology | none | — | none | reference | ☑ |
| P16 | `/showroom-verification-methodology/` | methodology | none | — | none | principle added | ☑ |
| P17 | `/medical-claims/massage-chair-health-claims/` | health claims | none (forbidden) | — | none | reference | ☑ |
| P18 | `/medical-disclaimer/` | disclaimer | none | — | none | consistency | ☑ |
| B1 | `/brands/panasonic-massage-chairs/` | Panasonic | MCM | Panasonic / CA | `/collections/panasonic-massage-chairs` → "current Panasonic showroom availability at Massage Chairs & More" | short note | ☑ |
| B2 | `/brands/ohco-massage-chairs/` | OHCO | MCM | OHCO / CA | `/collections/ohco-massage-chairs` → "current OHCO models listed by Massage Chairs & More" | short note | ☑ |
| B3 | `/brands/dcore-massage-chairs/` | D.Core | MCM | D.Core / CA | `/collections/d-core-massage-chairs` → "current D.Core models listed by Massage Chairs & More" | short note | ☑ |
| B4 | `/brands/koyo-massage-chairs/` | Koyo | MCM | Koyo / CA | `/collections/koyo-massage-chairs` → "current Koyo showroom information from Massage Chairs & More" | short note | ☑ |
| B5 | `/brands/positive-posture-massage-chairs/` | Positive Posture | MCM | PP / CA | `/collections/positive-posture-massage-chairs` → "current Positive Posture models listed by Massage Chairs & More" | short note | ☑ |
| B6 | `/brands/osaki-massage-chairs/` | Osaki | HCM | Osaki / Bay Area | `/collections/osaki` → "current Osaki showroom information from House of Massage Chairs" | short note | ☑ |
| B7 | `/brands/infinity-massage-chairs/` | Infinity | HCM | Infinity / San Jose | `/collections/infinity` → "current Infinity showroom information from House of Massage Chairs" | short note | ☑ |
| B8 | `/brands/kyota-massage-chairs/` | Kyota | HCM | Kyota / Bay Area | `/collections/kyota` → "current Kyota showroom information from House of Massage Chairs" | short note | ☑ |
| B9 | `/brands/ogawa-massage-chairs/` | Ogawa | HCM | Ogawa / Bay Area | `/collections/ogawa` → "current Ogawa showroom information from House of Massage Chairs" | short note | ☑ |
| B10 | `/brands/cozzia-massage-chairs/` | Cozzia | HCM | Cozzia / Bay Area | `/collections/cozzia` → "current Cozzia models listed by House of Massage Chairs" | short note | ☑ |
| B11 | `/brands/bodyfriend-massage-chairs/` | Bodyfriend | HCM | Bodyfriend / Bay Area | `/collections/bodyfriend` → "current Bodyfriend showroom information from House of Massage Chairs" | short note | ☑ |
| B12 | `/brands/fujiiryoki-massage-chairs/` | Fujiiryoki | HCM | Fujiiryoki / Bay Area | `/collections/fujiiryoki` → "current Fujiiryoki models listed by House of Massage Chairs" | short note | ☑ |

*(Status column reflects final state after implementation.)*

## 6. Open items / facts to re-verify before each publish cycle
- RESOLVED 2026-07-11 (owner): do NOT publish any business-relationship / commercial-benefit statement on the site. Retailer examples are presented as neutral editorial mentions only ("public examples to verify, not rankings or endorsements"). Links stay plain editorial follow (`rel="noopener"`); no `rel="sponsored"`. Revisit only if a paid/affiliate arrangement is ever introduced.
- Re-verify showroom counts, hours, addresses, floor models, and warranty/delivery promises each cycle — all are first-party retailer claims and can change.
- MCM & HCM both list a Pleasanton/Stoneridge showroom — monitor whether these consolidate or change.
