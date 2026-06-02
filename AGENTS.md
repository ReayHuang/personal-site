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

**Maritime notes** (`notes/maritime/`)

| Slug | English | Traditional Chinese |
|------|---------|---------------------|
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

**Management notes** (`research/`)

| Slug | English | Traditional Chinese |
|------|---------|---------------------|
| 5S study | `5s-study-notes.en.html` | `5s-study-notes.html` |
| Business statistics | `stats-business-application.en.html` | `stats-business-application.html` |
| SBC demand classification | `sbc-demand-classification.en.html` | `sbc-demand-classification.html` |

### Internationalization

**English-primary site** — English is the default language; Traditional Chinese is secondary.

- **Default language**: English (`index.html` at site root).
- **Traditional Chinese**: `index.zh.html` for homepage; other pages use the base filename (e.g. `about.html`, `notes/index.html`).
- **English content pages**: use the `.en.html` suffix (e.g. `about.en.html`, `notes/index.en.html`).
- **`x-default` hreflang**: always points to the English version of each page pair.
- **Language switch**: EN link appears before 繁中 in the header on every page.
- **Adding content**: create the English page first, add it to the `*.en.html` listing, then add Traditional Chinese if needed.

See `README.md` for file naming and listing conventions. For machine-readable locale pairs, see `i18n/manifest.json`.

### Lint / Test / Build

- **Lint**: No linter configured. HTML can be validated with any W3C HTML validator if needed.
- **Test**: No automated tests. Manual verification by loading pages in a browser.
- **Build**: None required — pure static files.

### Adding content

Copy an existing English HTML file as a template, add a card link on the relevant English listing page (`notes/index.en.html` or `research/index.en.html`), then add a Traditional Chinese version and listing link if needed. See `README.md` for details.

### Google Analytics

Every HTML page must include **Google tag (gtag.js)** at the start of `<head>`: async loader for `G-YJDKH6WYT1` plus `gtag-config.js` (path: `assets/js/` at root, `../assets/js/` under `notes/` or `research/`, `../../assets/js/` under `notes/maritime/`). Copy the snippet from a sibling page in the same directory when adding new pages.
