# 🐼 Pandas for Data Analysis

The single most important library for data manipulation in Python.

## 📚 Module Overview

Mastering Pandas is non-negotiable for data analysts. This module takes you from basic DataFrames to advanced merging, time series analysis, and complex filtering.

### Prerequisites
- Python basics (Variables, Lists, Dictionaries)
- Basic understanding of tabular data (Excel/CSV)

### Estimated Time
**10-12 hours**

---

## 📖 Content

### [01_pandas_intro.ipynb](01_pandas_intro.ipynb)
**Difficulty:** 🟢 Beginner  
**Time:** 2 hours

**Topics:**
- Series vs DataFrames
- Loading data (CSV, Excel)
- Inspecting data (`head()`, `info()`, `describe()`)
- Basic selection (`loc`, `iloc`)

---

### [02_data_manipulation.ipynb](02_data_manipulation.ipynb)
**Difficulty:** 🟢 Beginner  
**Time:** 2 hours

**Topics:**
- Adding/Deleting columns
- Sorting and Ranking
- Renaming columns
- Applying functions (`apply()`, `map()`)

---

### [03_grouping_aggregation.ipynb](03_grouping_aggregation.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 2-3 hours

**Topics:**
- `groupby()` mechanics
- Aggregation functions (`sum`, `mean`, `count`)
- `agg()` for multiple statistics
- Pivot tables vs GroupBy

---

### [04_merging_joining.ipynb](04_merging_joining.ipynb)
**(New)**
**Difficulty:** 🟡 Intermediate  
**Time:** 2 hours

**Topics:**
- Concatenation (`pd.concat`)
- Merging (`pd.merge`) - Inner, Left, Right, Outer
- Joining on Index
- Handling duplicates

---

### [05_time_series.ipynb](05_time_series.ipynb)
**(New)**
**Difficulty:** 🟡 Intermediate  
**Time:** 2 hours

**Topics:**
- `datetime` conversion
- Resampling (Daily -> Monthly)
- Rolling windows (Moving Averages)
- Time-based indexing

---

### [06_advanced_filtering.ipynb](06_advanced_filtering.ipynb)
**(New)**
**Difficulty:** 🟡 Intermediate  
**Time:** 1-2 hours

**Topics:**
- Boolean indexing (`&`, `|`, `~`)
- `query()` method
- String methods (`.str.contains`)
- Handling missing data in filters

---

## 🎯 Learning Path

1. **Basics:** Start with 01 & 02 to get comfortable.
2. **Aggregation:** Master `groupby` (03) - this is your "Pivot Table" replacement.
3. **Combining:** Learn to merge multiple datasets (04).
4. **Specialized:** Dive into Time Series (05) and Advanced Filtering (06).

---

## 💡 Key Takeaways

✅ **Load & Save:** Read CSV, Excel, SQL, JSON  
✅ **Clean:** Handle missing values, duplicates, and wrong types  
✅ **Transform:** Group, pivot, melt, and reshape data  
✅ **Combine:** Merge multiple tables like SQL  
✅ **Analyze:** Time series and rolling statistics  

---

## 🔧 Tools & Libraries
```bash
pip install pandas numpy matplotlib openpyxl
```

---

## ⚠️ Common Mistakes

❌ Using loops instead of vectorized operations  
❌ Modifying a slice (SettingWithCopyWarning)  
❌ Forgetting to reset index after grouping  
❌ Merging without checking for duplicates  
❌ Treating dates as strings instead of datetime objects  

---

## 🎓 Practice Projects

### Project 1: Sales Analysis
- Load 12 months of sales data
- Merge into single DataFrame
- Calculate best month for sales
- Determine best time to display adds

### Project 2: Employee Churn
- Load HR data
- Filter for employees who left
- Group by department and salary range
- Visualize retention rates

---

**Happy Analyzing! 🐼**
