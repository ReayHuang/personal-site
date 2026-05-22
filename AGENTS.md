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
| `index.html` | Homepage with hero banner |
| `about.html` | About / CV page |
| `notes/index.html` | Professional notes listing |
| `notes/maritime/class-survey-basics.html` | Ship classification & regulations note |
| `research/index.html` | Research listing |
| `research/sbc-demand-classification.html` | SBC demand classification research |
| `research/sample-study.html` | Sample study template |

### Lint / Test / Build

- **Lint**: No linter configured. HTML can be validated with any W3C HTML validator if needed.
- **Test**: No automated tests. Manual verification by loading pages in a browser.
- **Build**: None required — pure static files.

### Adding content

Copy an existing HTML file as a template, then add a card link on the relevant listing page (`notes/index.html` or `research/index.html`). See `README.md` for details.
