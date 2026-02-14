import os
import nbformat

def add_badge(file_path):
    # Construct Colab URL
    # Assuming standard GitHub structure: github.com/username/repo/blob/branch/path
    # Colab URL: colab.research.google.com/github/username/repo/blob/branch/path
    
    # Path relative to repo root
    rel_path = os.path.relpath(file_path, start=".")
    
    colab_url = f"https://colab.research.google.com/github/wasim/Data-Science/blob/main/data-analyst-roadmap/{rel_path}"
    badge_markdown = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    
    try:
        nb = nbformat.read(file_path, as_version=4)
        
        # Check if badge already exists in first cell
        if nb.cells and nb.cells[0].cell_type == 'markdown':
            if "colab-badge.svg" in nb.cells[0].source:
                print(f"Skipping {rel_path} (Badge exists)")
                return

        # Create new markdown cell with badge
        new_cell = nbformat.v4.new_markdown_cell(badge_markdown)
        
        # Insert as first cell
        nb.cells.insert(0, new_cell)
        
        nbformat.write(nb, file_path)
        print(f"Added badge to {rel_path}")
        
    except Exception as e:
        print(f"Error processing {rel_path}: {e}")

# Process all .ipynb files
for root, dirs, files in os.walk("."):
    # Skip hidden dirs
    if ".ipynb_checkpoints" in root:
        continue
        
    for file in files:
        if file.endswith(".ipynb"):
            add_badge(os.path.join(root, file))
