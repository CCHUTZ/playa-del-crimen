#!/usr/bin/env python3
"""
Build script for Playa del Crimen
Converts Markdown content to HTML for GitHub Pages
"""

import os
import markdown
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
CONTENT_DIR = PROJECT_ROOT / "content" / "scenarios" / "00_la_estrella_del_terror"
OUTPUT_FILE = PROJECT_ROOT / "docs" / "scenarios" / "00_la_estrella_del_terror.html"

# HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Estrella del Terror | Playa del Crimen</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="../index.html" style="color: white;">Playa del Crimen</a></h1>
            <p class="tagline">Scenario 00: La Estrella del Terror</p>
        </div>
    </header>

    <main class="container">
        {content}
    </main>

    <footer>
        <div class="container">
            <p><a href="../index.html">← Back to Home</a></p>
        </div>
    </footer>
</body>
</html>
"""

def read_markdown_file(filepath):
    """Read a Markdown file and return its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def convert_markdown_to_html(md_content):
    """Convert Markdown content to HTML."""
    return markdown.markdown(md_content, extensions=['extra', 'codehilite'])

def build_scenario():
    """Build the scenario HTML file."""
    # List of files to include in order
    files_to_include = [
        CONTENT_DIR / "README.md",
        CONTENT_DIR / "briefing.md",
        CONTENT_DIR / "team_structure" / "roles.md",
        CONTENT_DIR / "phases" / "01_reconnaissance.md",
        CONTENT_DIR / "phases" / "02_attack_surface.md",
        CONTENT_DIR / "phases" / "03_relationship_mapping.md",
        CONTENT_DIR / "phases" / "04_risk_exposure.md",
        CONTENT_DIR / "phases" / "05_lessons_learned.md",
        CONTENT_DIR / "exercises" / "tabletop_exercise.md",
        CONTENT_DIR / "exercises" / "quiz.md",
        CONTENT_DIR / "exercises" / "practical_defense.md",
        CONTENT_DIR / "references.md",
    ]
    
    # Combine all Markdown content
    combined_md = ""
    for filepath in files_to_include:
        if filepath.exists():
            combined_md += read_markdown_file(filepath) + "\n\n---\n\n"
    
    # Convert to HTML
    html_content = convert_markdown_to_html(combined_md)
    
    # Insert into template
    final_html = HTML_TEMPLATE.format(content=html_content)
    
    # Write to output file
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✓ Built: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_scenario()
    print("Build complete!")
