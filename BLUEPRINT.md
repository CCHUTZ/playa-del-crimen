# Blueprint: Playa del Crimen - OSINT Training Scenarios

**Version:** 1.0

**Date:** 2026-02-21

## 1. Vision & Mission

**Vision:** To be the most engaging and effective educational resource for learning OSINT and sociotechnical security through immersive, narrative-driven scenarios.

**Mission:** To create a series of realistic, fictional training scenarios that teach students to think like threat actors in order to build better defenses, all presented within a unique and memorable "Caribbean vaporwave" aesthetic.

## 2. Core Identity

- **Name:** Playa del Crimen
- **Tagline:** OSINT Training Scenarios
- **Tone:** "Beach Noir" - a mix of serious, professional intelligence analysis with a relaxed, stylish, and slightly mysterious Caribbean vibe.
- **Keywords:** OSINT, Threat Intelligence, Social Engineering, Sociotechnical Risk, Red Teaming, Educational, Narrative-Driven.

## 3. Visual Identity

- **Palette:**
  - **Primary:** `#00BFFF` (Deep Sky Blue)
  - **Secondary:** `#FF69B4` (Hot Pink)
  - **Accent 1:** `#FF8C00` (Dark Orange)
  - **Accent 2:** `#8A2BE2` (Blue Violet)
  - **Background:** `#1E1E1E` (Dark Gray/Almost Black)
  - **Text:** `#FFFFFF` (White)
- **Inspiration:** The provided image (vaporwave sunset with palm trees).
- **Typography:**
  - **Headings:** A stylish, slightly retro font (e.g., `Lobster`, `Pacifico`, or a similar Google Font).
  - **Body:** A clean, modern, and highly readable sans-serif font (e.g., `Roboto`, `Lato`, `Montserrat`).

## 4. Target Audience

- Students of the "AI Strategic Intelligence Program".
- Cybersecurity professionals looking to improve their OSINT skills.
- Intelligence analysts (corporate and governmental).
- Red teamers and penetration testers.
- Security educators and trainers.

## 5. Content Strategy

- **Scenarios:** Each scenario is a self-contained module with a consistent structure.
- **Narrative:** Each scenario is presented as a "dossier" or after-action report.
- **Educational Focus:** The goal is always defensive learning, not offensive instruction.
- **Realism:** Scenarios are fictional but based on real-world TTPs (Tactics, Techniques, and Procedures).

## 6. Technical Implementation

- **Platform:** GitHub Pages.
- **Framework:** Minimalist. No complex frameworks like React or Vue. We will use plain HTML, CSS, and possibly a small amount of JavaScript for minor enhancements (e.g., theme toggling, navigation).
- **Build Process:** A simple assembly line approach. All content will be written in Markdown and then converted to HTML. A templating engine (like Jinja2 or a simple Python script) will be used to inject content into a base HTML template.
- **Deployment:** Automated deployment to GitHub Pages via GitHub Actions.

## 7. Repository Structure

(As defined in the previous interaction, and validated here)

```
playa-del-crimen/
├── README.md
├── BLUEPRINT.md
├── docs/  (This will be the root for GitHub Pages)
│   ├── index.html
│   ├── style.css
│   ├── scenarios/
│   │   └── 00_la_estrella_del_terror.html
│   └── resources/
│       └── osint_tools.html
├── content/
│   ├── scenarios/
│   │   └── 00_la_estrella_del_terror/
│   │       ├── README.md
│   │       ├── briefing.md
│   │       └── ... (all other markdown files)
│   └── resources/
│       └── osint_tools.md
└── scripts/
    └── build.py (Python script to convert Markdown to HTML)
```

## 8. Initial Scenario: "La Estrella del Terror"

- **Objective:** To teach students how to map and exploit the sociotechnical vulnerabilities of an informal organization.
- **Key Concepts:** Social attack surface, human-centric threats, pretexting, watering hole attacks, information warfare.
- **Deliverables:** A complete set of Markdown files as per the repository structure, ready for conversion to HTML.

## 9. Success Metrics

- **Engagement:** High traffic from the main course repository.
- **Completion:** Evidence that users are progressing through the scenarios.
- **Feedback:** Positive feedback from users on the educational value and engaging format.
- **Scalability:** The ability to easily add new scenarios in the future.
