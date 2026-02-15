# CLAUDE.md

This file provides guidance for AI assistants working with the ChiChin Liu personal tutor website repository.

## Project Overview

A static personal tutor website for ChiChin Liu, a professional instructor offering online teaching services in Taiwan. All user-facing content is written in **Traditional Chinese (zh-TW)**.

## Repository Structure

```
├── index.html          # Single-page HTML (all sections: hero, about, courses, testimonials, contact)
├── styles.css          # All styles, CSS variables, responsive breakpoints
├── script.js           # Vanilla JS: navigation, form handling, scroll animations
├── README.md           # Project documentation (Traditional Chinese)
├── examples/
│   └── course-proposal-example.md   # Sample output from course-proposal skill
└── .claude/
    └── skills/
        ├── README.md               # Skills documentation
        └── course-proposal.md      # Course proposal generator skill
```

## Tech Stack

- **HTML5** — Semantic markup, single-page layout
- **CSS3** — CSS variables, Flexbox, Grid, media queries
- **Vanilla JavaScript** — No frameworks or libraries
- **Google Fonts** — `Noto Sans TC` (weights: 300, 400, 500, 700)

There is **no build system**, no package.json, no bundler, no test framework, and no linter. The site runs by opening `index.html` directly in a browser.

## Key Conventions

### Language

- All content, comments, console messages, and error text are in **Traditional Chinese**
- Technical identifiers (CSS classes, JS variables) use **English**

### CSS

- **CSS variables** defined in `:root` for theming — change colors in `styles.css` lines 2–16
- **Class naming**: kebab-case, BEM-like (e.g., `.course-card`, `.hero-title`, `.section-title`, `.nav-brand`)
- **Responsive breakpoints**: 768px (tablet), 480px (mobile)
- **Shadow system**: `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl`
- **Color palette**: `--primary-color: #2563eb`, `--secondary-color: #3b82f6`, `--accent-color: #60a5fa`

### JavaScript

- All code runs inside a single `DOMContentLoaded` listener in `script.js`
- **camelCase** for variables and functions
- Uses `IntersectionObserver` for scroll-triggered animations
- Form validation uses inline error messages appended to the DOM
- No external dependencies — everything is vanilla JS

### HTML

- Sections use `id` attributes for navigation anchoring: `#home`, `#about`, `#courses`, `#testimonials`, `#contact`
- Semantic elements: `<section>`, `<nav>`, `<footer>`
- Course cards follow a repeatable `.course-card` template inside `.courses-grid`

## Page Sections

| Section       | ID               | Purpose                                |
|---------------|------------------|----------------------------------------|
| Navigation    | `navMenu`        | Fixed navbar with mobile hamburger     |
| Hero          | `#home`          | Landing area with CTA buttons          |
| About         | `#about`         | Bio, experience stats, expertise       |
| Courses       | `#courses`       | Grid of 4 course cards                 |
| Testimonials  | `#testimonials`  | 3 student review cards                 |
| Contact       | `#contact`       | Contact form + info (currently logs to console) |
| Footer        | `.footer`        | Links and social media                 |

## Common Tasks

### Adding a new course

Add a `.course-card` div inside `.courses-grid` in `index.html`:

```html
<div class="course-card">
    <div class="course-icon">🎓</div>
    <h3>課程名稱</h3>
    <p>課程描述</p>
    <ul class="course-features">
        <li>特色一</li>
    </ul>
    <div class="course-price">價格</div>
</div>
```

### Changing the color theme

Edit the CSS variables in `styles.css` `:root` block (lines 2–16).

### Modifying contact info

Update the `#contact` section in `index.html`.

## Development

- **Preview**: Open `index.html` in any modern browser — no build step required
- **No tests**: There are no automated tests
- **No linting**: There are no linting or formatting tools configured
- **Deployment**: Static hosting — GitHub Pages, Netlify, Vercel, Firebase Hosting, or AWS S3

## Claude Skills

The `.claude/skills/course-proposal.md` skill is an interactive course proposal generator. It guides users through collecting course information and outputs a structured markdown curriculum document following SMART principles. See `examples/course-proposal-example.md` for sample output.

## Important Notes

- The contact form (`#contactForm`) currently only logs data to `console.log` and shows an alert — it does not send data to any backend
- Testimonial carousel rotation is defined but **commented out** (`script.js` line 150)
- The back-to-top button is dynamically created in JS, not in the HTML
- All scroll animations use `fadeInUp` keyframe defined in `styles.css`
