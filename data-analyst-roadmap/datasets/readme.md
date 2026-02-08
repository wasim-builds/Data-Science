# Dataset Sources and Information

This directory contains datasets used throughout the Data Analyst Roadmap.

## Dataset Categories

### 1. Practice Datasets (Built-in)
Many notebooks use synthetic data or built-in datasets from libraries:
- NumPy random data
- Scikit-learn sample datasets
- Seaborn built-in datasets

### 2. Real-World Datasets

For end-to-end projects, you can download datasets from:

#### Kaggle
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- Popular datasets:
  - Titanic Dataset
  - House Prices
  - COVID-19 Data
  - E-commerce Data

#### UCI Machine Learning Repository
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- Classic datasets for learning

#### Government Open Data
- [Data.gov](https://data.gov)
- [World Bank Data](https://data.worldbank.org)
- [WHO Data](https://www.who.int/data)

#### Other Sources
- [FiveThirtyEight Data](https://data.fivethirtyeight.com)
- [Google Dataset Search](https://datasetsearch.research.google.com)
- [AWS Open Data](https://registry.opendata.aws)

## Downloading Datasets

### Method 1: Manual Download
1. Visit the dataset source
2. Download CSV/Excel files
3. Place in this `datasets/` directory

### Method 2: Using Python
```python
import pandas as pd

# Load from URL
url = "https://example.com/data.csv"
df = pd.read_csv(url)

# Save locally
df.to_csv('datasets/my_data.csv', index=False)
```

### Method 3: Using Kaggle API
```bash
# Install Kaggle CLI
pip install kaggle

# Download dataset
kaggle datasets download -d username/dataset-name
```

## Dataset Organization

Organize your datasets by project:
```
datasets/
├── sales_analysis/
│   ├── sales_data.csv
│   └── customers.csv
├── covid_analysis/
│   └── covid_data.csv
└── ecommerce_analysis/
    ├── orders.csv
    └── products.csv
```

## Sample Datasets Included

The end-to-end projects will guide you to appropriate datasets or generate synthetic data for learning purposes.

## Data Ethics

When using real-world data:
- ✅ Check licensing and terms of use
- ✅ Respect privacy and anonymization
- ✅ Cite data sources properly
- ✅ Don't redistribute without permission

## Need Help?

If you can't find a dataset for a specific project, you can:
1. Use the synthetic data generators in the notebooks
2. Search Kaggle for similar datasets
3. Use built-in datasets from seaborn or sklearn

Happy analyzing! 📊
