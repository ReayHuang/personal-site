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

- **Default language**: English (`index.html` at site root).
- **Traditional Chinese**: `index.zh.html` for homepage; other pages use the base filename (e.g. `about.html`, `notes/index.html`).
- **English content pages**: use the `.en.html` suffix (e.g. `about.en.html`, `notes/index.en.html`).
- Language switch links appear in the site header on each page.

### Lint / Test / Build

- **Lint**: No linter configured. HTML can be validated with any W3C HTML validator if needed.
- **Test**: No automated tests. Manual verification by loading pages in a browser.
- **Build**: None required — pure static files.

### Adding content

Copy an existing HTML file as a template, then add a card link on the relevant listing page (`notes/index.html` or `research/index.html`). See `README.md` for details.
