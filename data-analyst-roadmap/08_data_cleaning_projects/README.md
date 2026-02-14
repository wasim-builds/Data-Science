# 🧹 Data Cleaning Projects

80% of data analysis is cleaning. This module makes you a pro at it.

## 📚 Module Overview

Real-world data is never clean. It has missing values, duplicates, typos, and outliers. This module provides a toolkit to handle the messiest datasets with confidence.

### Prerequisites
- Python basics
- Pandas proficiency (Module 03)

### Estimated Time
**8-10 hours**

---

## 📖 Content

### [01_data_cleaning_basics.ipynb](01_data_cleaning_basics.ipynb)
**Difficulty:** 🟢 Beginner  
**Time:** 2 hours
**Topics:** 
- Renaming columns
- Changing data types
- Removing duplicates
- String stripping

### [02_handling_missing_data.ipynb](02_handling_missing_data.ipynb)
**(New)**
**Difficulty:** 🟡 Intermediate  
**Time:** 2 hours
**Topics:**
- Detecting nulls (`isnull`)
- Imputation (Mean, Median, Mode)
- Forward/Backward fill
- KNN Imputation (Advanced)

### [03_outlier_detection.ipynb](03_outlier_detection.ipynb)
**(New)**
**Difficulty:** 🟡 Intermediate  
**Time:** 2 hours
**Topics:**
- Box Plots & IQR Method
- Z-Score method
- Isolation Forest (Machine Learning)
- Capping and Winsorization

### [04_text_cleaning.ipynb](04_text_cleaning.ipynb)
**(New)**
**Difficulty:** 🔴 Advanced  
**Time:** 2-3 hours
**Topics:**
- Normalization (Lowercasing, stripping)
- Regex pattern matching
- Extracting emails/phones
- Fuzzy string matching

---

## 🎯 Learning Path

1. **Start Simple:** Master basic cleaning (01).
2. **Handle Gaps:** Learn strategies for missing data (02).
3. **Find Oddities:** Detect and handle outliers (03).
4. **Master Text:** Clean unstructured text data (04).

---

## 💡 Key Takeaways

✅ **Strategy:** Don't just delete data—fix it.  
✅ **Context:** Outliers might be errors or they might be insights.  
✅ **REGEX:** A superpower for text data.  
✅ **Automation:** Build reusable cleaning functions.  

---

## 🔧 Tools & Libraries
```bash
pip install pandas numpy seaborn scikit-learn
```

---

## ⚠️ Common Mistakes

❌ Dropping rows without checking how much data is lost  
❌ Replacing missing values with '0' blindly  
❌ Ignoring case sensitivity in text  
❌ Over-cleaning (removing real signals)  

---

## 🎓 Practice Projects

### Project 1: Wikipedia Scraper Cleanup
- Scrape a table from Wikipedia
- Fix date formats
- Remove citation markers [1]
- Convert population strings to numbers

### Project 2: Customer CRM Cleanup
- Merge duplicates based on Name/Email
- Standardize phone numbers
- Fill missing addresses

---

**Happy Cleaning! 🧹**
