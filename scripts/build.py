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
SCENARIOS_DIR = PROJECT_ROOT / "content" / "scenarios"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "scenarios"

# Scenario list
SCENARIOS = [
    {
        'id': '00_la_estrella_del_terror',
        'title': 'La Estrella del Terror',
        'number': '00'
    },
    {
        'id': '01_operacion_krakatoa',
        'title': 'Operación Krakatoa',
        'number': '01'
    },
    {
        'id': '02_la_cloaca',
        'title': 'La Cloaca',
        'number': '02'
    },
    {
        'id': '03_castillos_de_arena',
        'title': 'Castillos de Arena',
        'number': '03'
    },
    {
        'id': '04_el_tren_fantasma',
        'title': 'El Tren Fantasma',
        'number': '04'
    }
]

# HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Playa del Crimen</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="../index.html" style="color: white;">Playa del Crimen</a></h1>
            <p class="tagline">Escenario {number}: {title}</p>
        </div>
    </header>

    <main class="container">
        {content}
    </main>

    <footer>
        <div class="container">
            <p><a href="../index.html">← Volver al Inicio</a></p>
        </div>
    </footer>
</body>
</html>
"""

def read_markdown_file(filepath):
    """Read a Markdown file and return its content."""
    if not filepath.exists():
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def convert_markdown_to_html(md_content):
    """Convert Markdown content to HTML."""
    return markdown.markdown(md_content, extensions=['extra', 'codehilite'])

def build_scenario(scenario):
    """Build a scenario HTML file."""
    scenario_dir = SCENARIOS_DIR / scenario['id']
    
    # List of files to include in order
    files_to_include = [
        scenario_dir / "README.md",
        scenario_dir / "briefing.md",
        scenario_dir / "team_structure" / "roles.md",
    ]
    
    # Add phase files if they exist
    phases_dir = scenario_dir / "phases"
    if phases_dir.exists():
        for phase_file in sorted(phases_dir.glob("*.md")):
            files_to_include.append(phase_file)
    
    # Add exercise files if they exist
    exercises_dir = scenario_dir / "exercises"
    if exercises_dir.exists():
        for exercise_file in sorted(exercises_dir.glob("*.md")):
            if exercise_file.name != "solutions":
                files_to_include.append(exercise_file)
    
    # Add references if they exist
    references_file = scenario_dir / "references.md"
    if references_file.exists():
        files_to_include.append(references_file)
    
    # Combine all Markdown content
    combined_md = ""
    for filepath in files_to_include:
        content = read_markdown_file(filepath)
        if content:
            combined_md += content + "\n\n---\n\n"
    
    # Convert to HTML
    html_content = convert_markdown_to_html(combined_md)
    
    # Insert into template
    final_html = HTML_TEMPLATE.format(
        title=scenario['title'],
        number=scenario['number'],
        content=html_content
    )
    
    # Write to output file
    output_file = OUTPUT_DIR / f"{scenario['id']}.html"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✓ Built: {scenario['title']}")

if __name__ == "__main__":
    print("Building Playa del Crimen scenarios...")
    for scenario in SCENARIOS:
        build_scenario(scenario)
    print("\nBuild complete!")
