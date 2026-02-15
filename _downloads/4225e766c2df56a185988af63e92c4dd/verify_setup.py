#!/usr/bin/env python3
"""
Setup Verification Script for Data Analyst Roadmap
This script verifies that all required packages are installed correctly.
"""

import sys
from importlib import import_module

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Core packages (required)
CORE_PACKAGES = {
    'numpy': 'NumPy',
    'pandas': 'Pandas',
    'matplotlib': 'Matplotlib',
    'seaborn': 'Seaborn',
    'sklearn': 'Scikit-learn',
    'scipy': 'SciPy',
    'statsmodels': 'Statsmodels',
}

# Jupyter packages
JUPYTER_PACKAGES = {
    'jupyter': 'Jupyter',
    'jupyterlab': 'JupyterLab',
    'ipywidgets': 'IPyWidgets',
}

# Data processing packages
DATA_PACKAGES = {
    'openpyxl': 'OpenPyXL',
    'sqlalchemy': 'SQLAlchemy',
    'requests': 'Requests',
    'bs4': 'BeautifulSoup4',
    'plotly': 'Plotly',
}

# Optional packages (nice to have)
OPTIONAL_PACKAGES = {
    'streamlit': 'Streamlit',
    'dash': 'Dash',
    'selenium': 'Selenium',
    'prophet': 'Prophet',
    'pandera': 'Pandera',
    'nbconvert': 'NBConvert',
    'wordcloud': 'WordCloud',
    'folium': 'Folium',
}


def check_package(package_name, display_name):
    """Check if a package is installed and return its version."""
    try:
        module = import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, None


def print_section(title):
    """Print a section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def verify_packages(packages, required=True):
    """Verify a dictionary of packages."""
    all_installed = True
    results = []
    
    for package, display_name in packages.items():
        installed, version = check_package(package, display_name)
        
        if installed:
            status = f"{GREEN}✓{RESET}"
            info = f"{display_name:20} {version:15}"
        else:
            status = f"{RED}✗{RESET}"
            info = f"{display_name:20} {'NOT INSTALLED':15}"
            if required:
                all_installed = False
        
        results.append((status, info))
    
    for status, info in results:
        print(f"{status} {info}")
    
    return all_installed


def main():
    """Main verification function."""
    print("\n" + "="*60)
    print("  📊 Data Analyst Roadmap - Setup Verification")
    print("="*60)
    
    print(f"\nPython Version: {sys.version.split()[0]}")
    print(f"Python Path: {sys.executable}")
    
    # Check core packages
    print_section("Core Data Science Packages (Required)")
    core_ok = verify_packages(CORE_PACKAGES, required=True)
    
    # Check Jupyter packages
    print_section("Jupyter Packages (Required)")
    jupyter_ok = verify_packages(JUPYTER_PACKAGES, required=True)
    
    # Check data processing packages
    print_section("Data Processing Packages (Required)")
    data_ok = verify_packages(DATA_PACKAGES, required=True)
    
    # Check optional packages
    print_section("Optional Packages (Recommended)")
    verify_packages(OPTIONAL_PACKAGES, required=False)
    
    # Final summary
    print("\n" + "="*60)
    if core_ok and jupyter_ok and data_ok:
        print(f"{GREEN}✓ All required packages are installed!{RESET}")
        print(f"\n{GREEN}🎉 Your environment is ready for data analysis!{RESET}")
        print("\nNext steps:")
        print("  1. Launch Jupyter: jupyter lab")
        print("  2. Start with Module 01: Python Basics")
        print("  3. Build amazing data projects!")
        return 0
    else:
        print(f"{RED}✗ Some required packages are missing!{RESET}")
        print(f"\n{YELLOW}To install missing packages:{RESET}")
        print("  pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
