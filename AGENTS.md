# AGENTS.md

## Cursor Cloud specific instructions

This is a **static HTML/CSS/JS personal website** with zero build tools, no package manager, and no dependencies to install.

### Running the site locally

```bash
python3 -m http.server 8080
```

All HTML files are served as-is from the repository root. No build step is required.

### Pages

Bilingual pairs and locale mapping are maintained in `i18n/manifest.json` (`defaultLocale`: `en`).

**Site**

| Path | Description |
|------|-------------|
| `index.html` | English homepage (default) with hero banner |
| `index.zh.html` | Traditional Chinese homepage |
| `index.en.html` | Redirect to `index.html` (legacy URL) |
| `about.en.html` | About / CV (English) |
| `about.html` | About / CV (Traditional Chinese) |
| `notes/index.en.html` | Maritime notes listing (English) |
| `notes/index.html` | Maritime notes listing (Traditional Chinese) |
| `research/index.en.html` | Management notes listing (English) |
| `research/index.html` | Management notes listing (Traditional Chinese) |

**Maritime notes** (`notes/maritime/`) — order matches `notes/index.en.html`

| Slug | English | Traditional Chinese |
|------|---------|---------------------|
| Can drones replace ship surveyors (RIT) | `can-drones-replace-ship-surveyors.en.html` | `can-drones-replace-ship-surveyors.html` |
| Ammonia fuel | `ammonia-fuel-surveyor-notes.en.html` | `ammonia-fuel-surveyor-notes.html` |
| Future IMO/ILO container ships (2026) | `future-imo-ilo-container-ships-2026.en.html` | `future-imo-ilo-container-ships-2026.html` |
| Container ship Wind Shield | `container-ship-wind-shield-notes.en.html` | `container-ship-wind-shield-notes.html` |
| Electronic certificates (joint guidelines) | `electronic-certificates-joint-guidelines-notes.en.html` | `electronic-certificates-joint-guidelines-notes.html` |
| Onboard certificates | `onboard-certificates.en.html` | `onboard-certificates.html` |
| Engine FAT / shipboard trial (LR-RU-001) | `engine-fat-shipboard-note.en.html` | `engine-fat-shipboard-note.html` |
| LRPF (LR-RU-012) | `lfpf-note.en.html` | `lfpf-note.html` |
| Tailshaft survey | `tailshaft-survey-notes.en.html` | `tailshaft-survey-notes.html` |
| Steering gear | `steering-gear-notes.en.html` | `steering-gear-notes.html` |
| LR BWTS | `lr-bwts-notes.en.html` | `lr-bwts-notes.html` |
| Maritime cyber resilience | `maritime-cyber-resilience-notes.en.html` | `maritime-cyber-resilience-notes.html` |
| LR Advisory | `lr-advisory-notes.en.html` | `lr-advisory-notes.html` |
| MARPOL framework | `marpol-structure-notes.en.html` | `marpol-structure-notes.html` |
| SOLAS framework | `solas-structure-notes.en.html` | `solas-structure-notes.html` |
| Explosion protection | `explosion-protection-notes.en.html` | `explosion-protection-notes.html` |
| LPG fuel | `lpg-fuel-notes.en.html` | `lpg-fuel-notes.html` |
| New construction PM | `new-construction-pm-notes.en.html` | `new-construction-pm-notes.html` |
| Surveyor 6S / lean | `surveyor-6s-lean-management-notes.en.html` | `surveyor-6s-lean-management-notes.html` |
| IMO MSC 111 | `msc-111-visual-notes.en.html` | `msc-111-visual-notes.html` |
| GMDSS | `gmdss-radiocommunications-notes.en.html` | `gmdss-radiocommunications-notes.html` |
| LNG fuel | `lng-fuel-notes.en.html` | `lng-fuel-notes.html` |
| Methanol fuel | `methanol-fuel-notes.en.html` | `methanol-fuel-notes.html` |
| MEPC 83 / 84 | `mepc-83-84-visual-notes.en.html` | `mepc-83-84-visual-notes.html` |

**Korean supplementary pages** (`notes/maritime/`) — standalone; not on listing pages or in `i18n/manifest.json`

| Slug | Korean |
|------|--------|
| SOLAS framework | `solas-structure-notes.ko.html` |
| MARPOL framework | `marpol-structure-notes.ko.html` |

These pages include `hreflang` links to EN / 繁中 / ko and use `data-back-to-top-label="맨 위로"` on `<html>`.

**Management notes** (`research/`) — order matches `research/index.en.html`

| Slug | English | Traditional Chinese |
|------|---------|---------------------|
| Digital ship management report | `digital-ship-management-report.en.html` | `digital-ship-management-report.html` |
| Owned vs chartered container ships | `owned-vs-chartered-container-ships.en.html` | `owned-vs-chartered-container-ships.html` |
| Fleet spares thesis | `fleet-spares-thesis-notes.en.html` | `fleet-spares-thesis-notes.html` |
| 5S study | `5s-study-notes.en.html` | `5s-study-notes.html` |
| Business statistics | `stats-business-application.en.html` | `stats-business-application.html` |
| SBC demand classification | `sbc-demand-classification.en.html` | `sbc-demand-classification.html` |

Link preview images for listing/homepage cards live in `assets/images/research/` — e.g. `digital-ship-management-linkedin-preview-1200.png` (繁中) and `digital-ship-management-linkedin-preview.en-1200.png` (EN). Hero backgrounds for standalone research articles use optimized `.webp` / `.jpg` pairs (plus `-mobile` variants for narrow viewports), e.g. `hero-digital-ship-management.jpg`, `hero-owned-vs-chartered-fleet-strategy.webp`.

### Internationalization

**English-primary site** — English is the default language; Traditional Chinese is secondary.

- **Default language**: English (`index.html` at site root).
- **Traditional Chinese**: `index.zh.html` for homepage; other pages use the base filename (e.g. `about.html`, `notes/index.html`).
- **English content pages**: use the `.en.html` suffix (e.g. `about.en.html`, `notes/index.en.html`).
- **Korean (optional)**: use the `.ko.html` suffix for standalone article translations; not tracked in `i18n/manifest.json` unless added explicitly.
- **`x-default` hreflang**: always points to the English version of each page pair.
- **Language switch**: EN link appears before 繁中 in the header on every page.
- **Adding content**: create the English page first, add it to the `*.en.html` listing, then add Traditional Chinese if needed. Update `i18n/manifest.json` with the new EN/zh pair.

See `README.md` for file naming and listing conventions. For machine-readable locale pairs, see `i18n/manifest.json`.

### Lint / Test / Build

- **Lint**: No linter configured. HTML can be validated with any W3C HTML validator if needed.
- **Test**: No automated tests. Manual verification by loading pages in a browser.
- **Build**: None required — pure static files.

### Adding content

Copy an existing English HTML file as a template, add a card link on the relevant English listing page (`notes/index.en.html` or `research/index.en.html`), then add a Traditional Chinese version and listing link if needed. Add the EN/zh paths to `i18n/manifest.json`. See `README.md` for details.

For recent articles, use `card card--preview` on listing pages and the homepage “Latest content” section, with a `card__preview` `<img>` pointing at the locale-specific LinkedIn preview PNG (see Management notes asset naming above).

### Article page scripts (`</body>`)

Standalone note/article pages under `notes/maritime/` and `research/` also load (after `note-standalone.css` in `<head>`):

1. **`article-share.js`** — LinkedIn / Facebook / copy link / email share buttons (`[data-article-share]`)
2. **`back-to-top.js`** — fixed “back to top” button; label from `<html lang>` or `data-back-to-top-label`

Listing pages (`notes/index.*`, `research/index.*`) and the site root use **`main.js`** (mobile nav toggle) instead.

### Optional maintainer scripts (`scripts/`)

Not required to run the site. Used occasionally to regenerate assets:

| Script | Purpose |
|--------|---------|
| `scripts/generate-homepage-og.py` | Homepage Open Graph preview image |
| `scripts/generate-explosion-protection-og.py` | Explosion protection note OG image |
| `scripts/build-onboard-certificates-en.py` | Regenerate English onboard certificates page content |

### Deployment

Production: **Netlify** at `https://reayhuang.com` (static files, no build step). HSTS enabled.

### Site-wide scripts (`<head>`)

Every HTML page must include the following at the start of `<head>` (copy the three `<script>` lines from a sibling page in the same directory when adding new pages):

1. **Google tag (gtag.js)** — async loader for `G-YJDKH6WYT1`
2. **`gtag-config.js`**
3. **`copy-source-attribution.js`** — immediately after `gtag-config.js`; appends source attribution when users copy selections longer than 100 characters (skips `input`, `textarea`, `[contenteditable]`, `pre`, and `code`)

Relative path to `assets/js/` by page depth:

| Depth | Example path | Script `src` prefix |
|-------|--------------|---------------------|
| 0 | `index.html`, `about.en.html` | `assets/js/` |
| 1 | `notes/index.en.html`, `research/index.html` | `../assets/js/` |
| 2 | `notes/maritime/*.en.html` | `../../assets/js/` |

To verify all pages include the copy script: `grep -L "copy-source-attribution" **/*.html` (no output means every file is covered).
