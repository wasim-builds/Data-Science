# Python & Anaconda Setup Guide

## Why Python for Data Analysis?

Python is the most popular language for data analysis because:
- **Easy to learn**: Clean, readable syntax
- **Rich ecosystem**: Thousands of data science libraries
- **Community support**: Large, active community
- **Versatile**: From data cleaning to machine learning
- **Industry standard**: Used by top companies worldwide

## Installation Steps

### Step 1: Install Anaconda

Anaconda is a Python distribution that includes:
- Python interpreter
- Popular data science packages
- Conda package manager
- Jupyter Notebook/Lab

#### For Linux:

1. **Download Anaconda**
```bash
cd ~/Downloads
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
```

2. **Run the installer**
```bash
bash Anaconda3-2024.02-1-Linux-x86_64.sh
```

3. **Follow the prompts**
   - Press Enter to review the license
   - Type `yes` to accept
   - Press Enter to confirm installation location
   - Type `yes` to initialize Anaconda

4. **Restart your terminal**
```bash
source ~/.bashrc
```

#### For Windows:

1. Download from: https://www.anaconda.com/download
2. Run the `.exe` installer
3. Follow the installation wizard
4. Check "Add Anaconda to PATH" (optional but recommended)

#### For macOS:

1. Download from: https://www.anaconda.com/download
2. Run the `.pkg` installer
3. Follow the installation wizard

### Step 2: Verify Installation

```bash
# Check Python version
python --version

# Check conda version
conda --version

# List installed packages
conda list
```

Expected output:
```
Python 3.10.x
conda 24.x.x
```

### Step 3: Create Data Analyst Environment

```bash
# Navigate to the roadmap directory
cd data-analyst-roadmap

# Create environment from file
conda env create -f 00_setup/environment.yml

# Activate the environment
conda activate data-analyst
```

### Step 4: Install Additional Packages

```bash
# Install packages from requirements.txt
pip install -r requirements.txt
```

## Essential Conda Commands

### Environment Management
```bash
# List all environments
conda env list

# Activate environment
conda activate data-analyst

# Deactivate environment
conda deactivate

# Remove environment
conda env remove -n data-analyst
```

### Package Management
```bash
# Install a package
conda install package-name

# Install specific version
conda install package-name=1.2.3

# Update a package
conda update package-name

# Remove a package
conda remove package-name

# List installed packages
conda list
```

### Updating Conda
```bash
# Update conda itself
conda update conda

# Update all packages
conda update --all
```

## Alternative: Using pip and venv

If you prefer not to use Anaconda:

```bash
# Create virtual environment
python -m venv data-analyst-env

# Activate (Linux/Mac)
source data-analyst-env/bin/activate

# Activate (Windows)
data-analyst-env\Scripts\activate

# Install packages
pip install -r requirements.txt
```

## Troubleshooting

### Issue: Command 'conda' not found

**Solution**: Add Anaconda to PATH
```bash
# Linux/Mac
export PATH="$HOME/anaconda3/bin:$PATH"
source ~/.bashrc

# Or reinstall and select "Add to PATH"
```

### Issue: Package conflicts

**Solution**: Create a fresh environment
```bash
conda create -n data-analyst-new python=3.10
conda activate data-analyst-new
pip install -r requirements.txt
```

### Issue: Slow package installation

**Solution**: Use mamba (faster conda alternative)
```bash
conda install mamba -c conda-forge
mamba install package-name
```

## Verifying Your Setup

Create a test script to verify everything works:

```python
# test_setup.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

print("✅ NumPy version:", np.__version__)
print("✅ Pandas version:", pd.__version__)
print("✅ Matplotlib version:", plt.matplotlib.__version__)
print("✅ Seaborn version:", sns.__version__)
print("✅ Scikit-learn version:", datasets.__version__)
print("\n🎉 All packages installed successfully!")
```

Run it:
```bash
python test_setup.py
```

## Next Steps

Once your environment is set up:
1. ✅ Read `jupyter_setup.md` to learn about Jupyter Notebooks
2. ✅ Start with Module 01: Python Basics
3. ✅ Join the data science community

## Resources

- [Anaconda Documentation](https://docs.anaconda.com/)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)

---

**Ready to start your data analysis journey! 🚀**
