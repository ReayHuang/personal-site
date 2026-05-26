# AGENTS.md

## Cursor Cloud specific instructions

This is a **static HTML/CSS/JS personal website** with zero build tools, no package manager, and no dependencies to install.

### Running the site locally

```bash
python3 -m http.server 8080
```

All HTML files are served as-is from the repository root. No build step is required.

### Pages

| Path | Description |
|------|-------------|
| `index.html` | English homepage (default) with hero banner |
| `index.zh.html` | Traditional Chinese homepage |
| `index.en.html` | Redirect to `index.html` (legacy URL) |
| `about.html` | About / CV page (Traditional Chinese) |
| `about.en.html` | About / CV page (English) |
| `notes/index.html` | Maritime notes listing (Traditional Chinese) |
| `notes/index.en.html` | Maritime notes listing (English) |
| `notes/maritime/class-survey-basics.html` | Ship classification & regulations note |
| `research/index.html` | Management notes listing (Traditional Chinese) |
| `research/index.en.html` | Management notes listing (English) |
| `research/sbc-demand-classification.html` | SBC demand classification research |
| `research/sample-study.html` | Sample study template |

### Internationalization

**English-primary site** — English is the default language; Traditional Chinese is secondary.

- **Default language**: English (`index.html` at site root).
- **Traditional Chinese**: `index.zh.html` for homepage; other pages use the base filename (e.g. `about.html`, `notes/index.html`).
- **English content pages**: use the `.en.html` suffix (e.g. `about.en.html`, `notes/index.en.html`).
- **`x-default` hreflang**: always points to the English version of each page pair.
- **Language switch**: EN link appears before 繁中 in the header on every page.
- **Adding content**: create the English page first, add it to the `*.en.html` listing, then add Traditional Chinese if needed.

See `README.md` for file naming and listing conventions.

### Lint / Test / Build

- **Lint**: No linter configured. HTML can be validated with any W3C HTML validator if needed.
- **Test**: No automated tests. Manual verification by loading pages in a browser.
- **Build**: None required — pure static files.

### Adding content

Copy an existing English HTML file as a template, add a card link on the relevant English listing page (`notes/index.en.html` or `research/index.en.html`), then add a Traditional Chinese version and listing link if needed. See `README.md` for details.

### Google Analytics

Every HTML page must include **Google tag (gtag.js)** at the start of `<head>`: async loader for `G-YJDKH6WYT1` plus `gtag-config.js` (path: `assets/js/` at root, `../assets/js/` under `notes/` or `research/`, `../../assets/js/` under `notes/maritime/`). Copy the snippet from a sibling page in the same directory when adding new pages.
