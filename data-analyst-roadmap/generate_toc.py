import os
import yaml

# Define the order of modules
MODULE_ORDER = [
    "00_setup",
    "01_python_basics",
    "02_numpy",
    "03_pandas",
    "04_data_visualization",
    "05_statistics",
    "06_sql_for_analytics",
    "07_excel_for_analysts",
    "08_data_cleaning_projects",
    "09_end_to_end_projects",
    "10_machine_learning_basics"
]

def get_notebooks(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.ipynb') or f.endswith('.md')]
    # Sort files: README first, then standard sort
    files.sort(key=lambda x: (0 if x.lower() == 'readme.md' else 1, x))
    return files

toc_structure = {
    "format": "jb-book",
    "root": "intro",  # We need to create an intro.md
    "parts": []
}

for module in MODULE_ORDER:
    if not os.path.exists(module):
        continue
        
    chapter = {
        "caption": module.replace("_", " ").title(),
        "chapters": []
    }
    
    files = get_notebooks(module)
    for file in files:
        if file.lower() == "readme.md":
            # Use README as the intro for the chapter if preferred, 
            # but JupyterBook structure usually likes explicit chapters.
            # We'll map README to the first item (Introduction)
            chapter["chapters"].append({"file": f"{module}/{file}"})
        else:
            chapter["chapters"].append({"file": f"{module}/{file}"})
    
    if chapter["chapters"]:
        toc_structure["parts"].append(chapter)

# Create intro.md if it doesn't exist
if not os.path.exists("intro.md"):
    with open("intro.md", "w") as f:
        f.write("# Welcome to the Data Analyst Roadmap 🚀\n\nYour journey from zero to hero in Data Science starts here.")

# Save _toc.yml
with open("_toc.yml", "w") as f:
    yaml.dump(toc_structure, f, default_flow_style=False, sort_keys=False)

print("_toc.yml generated successfully!")
