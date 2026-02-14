import pandas as pd
import numpy as np
import seaborn as sns
import os

# Create datasets directory
DATA_DIR = 'datasets'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

print(f"Generating datasets in {DATA_DIR}...")

# 1. Titanic (Classification)
try:
    print("Saving titanic.csv...")
    titanic = sns.load_dataset('titanic')
    titanic.to_csv(f'{DATA_DIR}/titanic.csv', index=False)
except Exception as e:
    print(f"Error saving titanic: {e}")

# 2. Iris (Classification)
try:
    print("Saving iris.csv...")
    iris = sns.load_dataset('iris')
    iris.to_csv(f'{DATA_DIR}/iris.csv', index=False)
except Exception as e:
    print(f"Error saving iris: {e}")

# 3. Tips (Regression/Viz)
try:
    print("Saving tips.csv...")
    tips = sns.load_dataset('tips')
    tips.to_csv(f'{DATA_DIR}/tips.csv', index=False)
except Exception as e:
    print(f"Error saving tips: {e}")

# 4. Global Superstore Sales (Synthetic)
try:
    print("Generating sales_data.csv...")
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=365)
    sales_data = pd.DataFrame({
        'Date': dates,
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 365),
        'Product': np.random.choice(['Electronics', 'Furniture', 'Clothing'], 365),
        'Sales': np.random.normal(1000, 200, 365),
        'Profit': np.random.normal(200, 50, 365)
    })
    sales_data.to_csv(f'{DATA_DIR}/sales_data.csv', index=False)
except Exception as e:
    print(f"Error generating sales: {e}")

print("Dataset generation complete!")
