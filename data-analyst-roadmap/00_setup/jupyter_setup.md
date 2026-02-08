# Jupyter Notebook Setup & Usage Guide

## What is Jupyter Notebook?

Jupyter Notebook is an interactive computing environment that allows you to:
- Write and execute Python code in cells
- Visualize data with inline plots
- Document your analysis with markdown
- Share reproducible research

**Perfect for data analysis!**

## Installation

Jupyter is already included in your Anaconda installation. If you need to install it separately:

```bash
# Using conda
conda install jupyter jupyterlab

# Using pip
pip install jupyter jupyterlab
```

## Launching Jupyter

### Method 1: Jupyter Notebook (Classic Interface)

```bash
# Activate your environment
conda activate data-analyst

# Launch Jupyter Notebook
jupyter notebook
```

This will:
1. Start a local server
2. Open your browser at `http://localhost:8888`
3. Show your file system

### Method 2: JupyterLab (Modern Interface)

```bash
# Launch JupyterLab
jupyter lab
```

JupyterLab offers:
- Multiple tabs and panels
- File browser
- Terminal access
- Extension support

**Recommended for this roadmap!**

## Jupyter Notebook Basics

### Creating a New Notebook

1. Click "New" → "Python 3" (Notebook)
2. Or in JupyterLab: File → New → Notebook

### Understanding Cells

**Code Cells**: Execute Python code
```python
# This is a code cell
x = 5
print(x * 2)
```

**Markdown Cells**: Write formatted text
```markdown
# This is a heading
- Bullet point
**Bold text**
```

### Essential Keyboard Shortcuts

#### Command Mode (press `Esc`)
- `A`: Insert cell above
- `B`: Insert cell below
- `D, D`: Delete cell
- `M`: Convert to markdown
- `Y`: Convert to code
- `Shift + Enter`: Run cell and move to next
- `Ctrl + Enter`: Run cell and stay

#### Edit Mode (press `Enter`)
- `Tab`: Code completion
- `Shift + Tab`: Show documentation
- `Ctrl + /`: Comment/uncomment
- `Esc`: Exit to command mode

### Running Code

```python
# Run this cell with Shift + Enter
import numpy as np
import pandas as pd

print("Hello, Data Analysis!")
```

### Inline Visualizations

```python
import matplotlib.pyplot as plt

# Enable inline plotting
%matplotlib inline

# Create a simple plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("My First Plot")
plt.show()
```

## Magic Commands

Jupyter has special "magic" commands:

### Line Magics (single %)

```python
# Time execution
%timeit sum(range(1000))

# Run a Python script
%run my_script.py

# List variables
%who

# Show matplotlib plots inline
%matplotlib inline
```

### Cell Magics (double %%)

```python
# Time entire cell
%%time
total = 0
for i in range(1000000):
    total += i
print(total)
```

```python
# Write cell content to file
%%writefile my_script.py
def hello():
    print("Hello from file!")
```

```python
# Execute bash commands
%%bash
ls -la
pwd
```

## Best Practices

### 1. Organize Your Notebooks

```python
# Standard imports at the top
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
%matplotlib inline
sns.set_style('whitegrid')
pd.set_option('display.max_columns', None)
```

### 2. Use Markdown for Documentation

```markdown
# Analysis Title

## Objective
Analyze sales data to identify trends

## Steps
1. Load data
2. Clean data
3. Visualize trends
4. Draw conclusions
```

### 3. Clear Output Before Sharing

- Kernel → Restart & Clear Output
- Prevents large file sizes

### 4. Save Regularly

- `Ctrl + S` or `Cmd + S`
- Auto-save is enabled by default

## Useful Extensions

### Install Extensions

```bash
# Install nbextensions
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### Recommended Extensions

1. **Table of Contents**: Navigate large notebooks
2. **Variable Inspector**: See all variables
3. **ExecuteTime**: Show cell execution time
4. **Code Folding**: Collapse code blocks

## Working with Data

### Loading Data

```python
# CSV files
df = pd.read_csv('data.csv')

# Excel files
df = pd.read_excel('data.xlsx')

# Display first rows
df.head()
```

### Quick Data Exploration

```python
# Dataset info
df.info()

# Statistical summary
df.describe()

# Check missing values
df.isnull().sum()
```

### Inline Visualizations

```python
# Quick plot
df['column'].plot(kind='hist')
plt.show()

# Seaborn plot
sns.boxplot(data=df, x='category', y='value')
plt.show()
```

## Exporting Notebooks

### To HTML

```bash
jupyter nbconvert --to html notebook.ipynb
```

### To PDF

```bash
# Requires LaTeX
jupyter nbconvert --to pdf notebook.ipynb
```

### To Python Script

```bash
jupyter nbconvert --to script notebook.ipynb
```

## Troubleshooting

### Issue: Kernel keeps dying

**Solution**: Restart kernel
- Kernel → Restart
- Or restart Jupyter server

### Issue: Can't import modules

**Solution**: Check environment
```python
import sys
print(sys.executable)
# Should point to your conda environment
```

### Issue: Plots not showing

**Solution**: Add magic command
```python
%matplotlib inline
```

### Issue: Notebook won't open

**Solution**: Clear browser cache or try different browser

## JupyterLab vs Jupyter Notebook

| Feature | Notebook | Lab |
|---------|----------|-----|
| Interface | Simple | Modern |
| Multiple tabs | No | Yes |
| File browser | Basic | Advanced |
| Extensions | Limited | Many |
| Terminal | No | Yes |

**Recommendation**: Use JupyterLab for this roadmap

## Configuration

### Custom Startup

Create `~/.ipython/profile_default/startup/00-startup.py`:

```python
# Auto-import common libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("📊 Data science libraries loaded!")
```

### Themes

```bash
# Install themes
pip install jupyterthemes

# List themes
jt -l

# Apply dark theme
jt -t onedork -fs 11 -altp -tfs 11 -nfs 115 -cellw 88% -T
```

## Productivity Tips

1. **Use Tab Completion**: Type `df.` then press Tab
2. **View Documentation**: `?function_name` or `Shift + Tab`
3. **Run All Cells**: Kernel → Restart & Run All
4. **Split View**: Right-click cell → "New View for Output"
5. **Collapsible Headings**: Use markdown headers

## Next Steps

Now that Jupyter is set up:
1. ✅ Create a test notebook
2. ✅ Practice keyboard shortcuts
3. ✅ Start Module 01: Python Basics

## Resources

- [Jupyter Documentation](https://jupyter.org/documentation)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Jupyter Notebook Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)

---

**Happy coding in Jupyter! 📓✨**
