import json
import subprocess
import sys
import os

SOURCE_REPO = "/Users/abustamantev/Documents/github/rc-easy-matches-dl"
FILE_PATH_IN_REPO = "notebooks/classification_engine/rc_tree.json"

def get_json_from_main():
    """Reads the JSON file from the main branch of the source repository."""
    cmd = ["git", "-C", SOURCE_REPO, "show", f"main:{FILE_PATH_IN_REPO}"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching JSON from {SOURCE_REPO} main branch:")
        print(e.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:")
        print(e)
        sys.exit(1)

def generate_markdown(data):
    """Generates the Markdown representation of the tree."""
    md_lines = []
    
    dominios = data.get("dominios", {})
    
    for dom_id, dom_data in sorted(dominios.items(), key=lambda item: int(item[0])):
        md_lines.append(f"## {dom_data['nombre']}")
        
        categorias = dom_data.get("categorias", {})
        for cat_id, cat_data in sorted(categorias.items(), key=lambda item: int(item[0])):
            name = cat_data['nombre']
            is_canonical = cat_data.get('canonica', False)
            
            if is_canonical:
                md_lines.append(f"- **{name} ({cat_id})**")
            else:
                md_lines.append(f"- {name} ({cat_id})")
                
        md_lines.append("") # Empty line between domains
        
    return "\n".join(md_lines)

def update_readme(md_content):
    """Updates the readme.md file with the new categories."""
    readme_path = "readme.md"
    
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "# Árbol de Categorías\n\n## Categorías por Dominio\n"
        
    # We will replace everything after "## Categorías por Dominio"
    readme_md_lines = []
    for line in md_content.split('\n'):
        if line.startswith('## '):
            readme_md_lines.append(f"### {line[3:]}")
        else:
            readme_md_lines.append(line)
            
    final_readme_md = "\n".join(readme_md_lines)
    
    marker = "## Categorías por Dominio"
    if marker in content:
        prefix = content.split(marker)[0]
        new_content = prefix + marker + "\n\n" + final_readme_md
    else:
        new_content = content + "\n\n" + marker + "\n\n" + final_readme_md
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated readme.md")

def update_index_html(md_content):
    """Updates index.html with the new markdown tree."""
    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <title>Markmap - Árbol de Categorías</title>
  <style>
    * {{
      margin: 0;
      padding: 0;
    }}
    html {{
      font-family: ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji',
        'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
    }}
    .markmap {{
      display: block;
      width: 100vw;
      height: 100vh;
    }}
    .markmap > svg {{
      width: 100%;
      height: 100%;
    }}
    body {{
      background: #27272a;
      color: white;
    }}
    .markmap svg text {{
      fill: white !important;
    }}
  </style>
</head>
<body>
  <div class="markmap" id="mindmap">
    <script type="text/template">
---
markmap:
  initialExpandLevel: 2
---
# Árbol de Categorías

{md_content}
    </script>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@0.17.0"></script>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Updated index.html")

def main():
    print("Fetching JSON from main branch...")
    data = get_json_from_main()
    
    # Update local JSON
    with open("rc_tree.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Updated rc_tree.json")
    
    print("Generating Markdown...")
    md_content = generate_markdown(data)
    
    update_readme(md_content)
    update_index_html(md_content)
    
    print("Done! All files have been updated successfully.")

if __name__ == "__main__":
    main()
