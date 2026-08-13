# QA & Polish Checksheet — Pearl Salon Website
**Purpose:** Pre-launch audit checklist to catch what AI-generated / rushed websites usually miss.
**Use:** Go through every box before calling the site "done." Nothing ships with unchecked critical items.

---

## 1. Typography, Spelling & Spacing (the stuff people notice first)

- [ ] No spelling errors — run every page through a spellchecker (Grammarly/LanguageTool), not just eyeballing
- [ ] Consistent spelling of the shop name everywhere: "Pearl Salon" — decide once, use identically in every instance (not "Pearl Saloon" in one place and "Pearl Salon" in another)
- [ ] Consistent capitalization style across headings (either Title Case everywhere or Sentence case everywhere — never mixed)
- [ ] No double spaces between words (common copy-paste artifact)
- [ ] No trailing spaces at line/paragraph ends
- [ ] Consistent punctuation on list items (either all end with periods or none do)
- [ ] Smart/curly quotes (" " ' ') used consistently, not mixed with straight quotes (" ')
- [ ] Em dash (—) vs hyphen (-) vs en dash (–) used correctly and consistently
- [ ] No orphan words (single word alone on last line of paragraph, looks broken on mobile)
- [ ] Consistent number formatting (e.g. always "10 AM" not sometimes "10am", "10:00 AM", "10 a.m.")
- [ ] Phone numbers formatted consistently everywhere (+91 63990 08007 — same format in header, footer, contact section)
- [ ] Line-height and paragraph spacing consistent across all sections (no cramped text in one section, loose in another)
- [ ] Adequate letter-spacing on all-caps headings (all-caps text needs more tracking or it looks cramped)
- [ ] Consistent font pairing — max 2 font families (one for headings, one for body), not 3+
- [ ] Font sizes follow a clear hierarchy (H1 > H2 > H3 > body — no heading smaller than body text by mistake)
- [ ] No text overflowing its container/card on any screen size
- [ ] No unintended line breaks mid-sentence on mobile (test at 320px width)
- [ ] Consistent button label casing (either "Book Now" or "BOOK NOW" everywhere, not both)

---

## 2. Content Accuracy

- [ ] Every phone number on the site is clickable (`tel:` link) and dials the correct number
- [ ] Every WhatsApp button opens the correct number with a pre-filled sensible message
- [ ] Email link uses `mailto:` and correct address
- [ ] Address matches exactly across header, footer, contact section, and Google Map pin (no variation)
- [ ] Google Map pin actually points to the real location, not a default/wrong pin
- [ ] Business hours (once confirmed) are consistent everywhere they appear
- [ ] No leftover placeholder text (`[PLACEHOLDER]`, "Lorem ipsum", "Your text here") shipped to production
- [ ] No leftover template branding from reference sites (Naturals/Hair Raiserz names, logos, or copy accidentally left in code comments or hidden text)
- [ ] Copyright year in footer is current and set to auto-update (`© 2026` hardcoded will look outdated next year — use dynamic year via JS)
- [ ] All service names match what's actually offered — nothing invented, nothing missing
- [ ] No broken/mismatched claims (e.g. don't say "in business since 2010" unless confirmed)

---

## 3. Links & Navigation

- [ ] Every nav link scrolls/routes to the correct section — test each one individually
- [ ] No dead links (href="#" left unbound, or 404s)
- [ ] External links (Instagram, Facebook, Google Maps) open in a new tab (`target="_blank"`) with `rel="noopener noreferrer"`
- [ ] Logo in header links back to top of page/home
- [ ] Sticky "Book Now" button remains visible/functional while scrolling on all pages, doesn't overlap content
- [ ] Smooth scroll behavior for anchor links (not an abrupt jump)
- [ ] Back-to-top button on long pages (optional but professional touch)
- [ ] Skip-to-content link for keyboard/screen-reader users (accessibility)

---

## 4. Images & Media

- [ ] Every image has descriptive `alt` text (not empty, not "image1.jpg") — critical for accessibility and SEO
- [ ] No missing/broken images (check every image tag actually loads)
- [ ] Images compressed/optimized (WebP format where possible, no multi-MB unoptimized JPEGs)
- [ ] Consistent aspect ratios within each grid/gallery (no jarring size mismatches)
- [ ] Images have proper `loading="lazy"` for below-the-fold content (performance)
- [ ] No images with visible watermarks from stock/directory sources
- [ ] No copyright-infringing images (scraped from Justdial/Google without permission)
- [ ] Logo displays correctly on both light and dark backgrounds (may need light + dark logo variants)
- [ ] Favicon set (browser tab icon) — easy to forget, looks unfinished without it
- [ ] Open Graph image set for social share previews (when link is shared on WhatsApp/Facebook, a proper image + title should preview, not blank)

---

## 5. Responsive & Cross-Device

- [ ] Tested on actual mobile width (375px, 390px) not just resized desktop browser
- [ ] Tested on tablet width (768px)
- [ ] Tested on small laptop (1280px) and large desktop (1920px)
- [ ] No horizontal scroll on any screen size (common bug — always check)
- [ ] Tap targets (buttons/links) are large enough on mobile (minimum ~44x44px) — not too small/close together
- [ ] Text remains readable without zooming on mobile (minimum ~16px body text)
- [ ] Forms are usable on mobile keyboard (correct input types: `tel` for phone, `email` for email — triggers right mobile keyboard)
- [ ] Gallery/carousel swipes properly on touch devices
- [ ] Sticky header/CTA doesn't cover content when keyboard opens on mobile forms

---

## 6. Performance

- [ ] Page loads in under ~3 seconds on average connection (test with Google PageSpeed Insights / Lighthouse)
- [ ] No render-blocking scripts slowing first paint
- [ ] Fonts loaded efficiently (not too many weights/styles pulled in)
- [ ] Unused CSS/JS libraries removed (don't ship the entire Hair Raiserz plugin stack if only using 4 of them)
- [ ] Images sized appropriately for their display size (don't serve a 4000px image into a 400px container)
- [ ] Lighthouse score checked for Performance, Accessibility, Best Practices, SEO — aim for 90+ where feasible

---

## 7. SEO & Discoverability

- [ ] Unique, descriptive `<title>` tag (e.g. "Pearl Salon Modinagar | Hair, Makeup & Bridal Salon")
- [ ] Meta description written (150–160 characters, compelling, includes location + services)
- [ ] Proper heading hierarchy (only one `<h1>` per page, logical `<h2>`/`<h3>` nesting — not skipped levels)
- [ ] `schema.org` LocalBusiness structured data added with confirmed NAP (Name, Address, Phone) — helps Google Maps/local search
- [ ] `sitemap.xml` generated
- [ ] `robots.txt` present and correctly configured (not accidentally blocking the whole site)
- [ ] Canonical URL tag set (avoids duplicate-content issues)
- [ ] Location + service keywords naturally present in copy ("salon in Modinagar," "bridal makeup Modinagar") — not stuffed unnaturally
- [ ] Google Business Profile linked/matches website NAP exactly (consistency helps local ranking)

---

## 8. Accessibility (often skipped entirely)

- [ ] Sufficient color contrast between text and background (WCAG AA minimum — check with a contrast checker)
- [ ] All interactive elements reachable and usable via keyboard (Tab key navigation works logically)
- [ ] Form fields have associated `<label>` tags, not just placeholder text (placeholders disappear on focus — bad for usability)
- [ ] Buttons/links have descriptive text (not just "Click Here" repeated everywhere)
- [ ] Video/audio (if any) has captions or transcript
- [ ] Site usable/readable with browser zoom at 200%

---

## 9. Forms & Interactivity

- [ ] Contact/booking form has clear validation messages (not just a silent failure)
- [ ] Required fields clearly marked
- [ ] Success message/confirmation shown after form submission (user shouldn't wonder if it worked)
- [ ] Form actually delivers submissions somewhere real (email/WhatsApp) — test end-to-end before launch, not just visually
- [ ] Spam protection on form (honeypot field or simple CAPTCHA — a public contact form with no protection will get spammed)
- [ ] No console errors when interacting with any button/form (open browser dev tools and check)

---

## 10. Trust & Professionalism Signals

- [ ] Real testimonials with names (with permission), not obviously fake-sounding placeholder quotes
- [ ] Consistent, professional photography style throughout (not a mix of phone snapshots + stock photos with visibly different quality)
- [ ] Working social proof links (Instagram/Facebook buttons that go to real, active profiles)
- [ ] A visible privacy note near the contact form if collecting personal data (even a simple one-liner: "Your information is used only to respond to your enquiry")
- [ ] No fake urgency/countdown timers unless there's a genuinely real, current offer (fake scarcity damages trust and looks amateurish once noticed)
- [ ] Consistent brand voice/tone across all copy (not formal in one section, casual slang in another)

---

## 11. Legal & Basic Compliance

- [ ] Footer includes business name and year
- [ ] If collecting any personal data via form, a short privacy statement is present
- [ ] No misleading claims (unverified "#1 salon," fabricated statistics, etc.)

---

## 12. Browser & Device Testing

- [ ] Tested in Chrome, Safari, and at least one more (Firefox/Edge)
- [ ] Tested on an actual iPhone and an actual Android device if possible, not just emulators
- [ ] Check that WhatsApp click-to-chat buttons work correctly on both iOS and Android (behavior can differ)

---

## 13. Final Pre-Launch Pass

- [ ] Full read-through of every single line of visible text, out loud, top to bottom
- [ ] Click every single button and link on the live site once, in order
- [ ] Submit the contact form yourself and confirm you receive it
- [ ] View the site on your own phone, outdoors in sunlight (real-world screen glare/contrast test)
- [ ] Ask one person unfamiliar with the project to try booking/finding info without guidance — watch where they hesitate or get confused
- [ ] Confirm HTTPS is active (padlock icon, not "Not Secure" warning)
- [ ] Set up basic analytics (Google Analytics/Search Console) before launch, not after, so you don't lose early data

---

## Why this list matters
Most "AI-made" or rushed sites fail not on big structural decisions but on exactly this kind of detail: inconsistent phone number formatting, missing alt text, a form that silently fails, a favicon nobody added, or copy that still says "Lorem ipsum" somewhere nobody scrolled to. This checklist exists specifically to catch those.
