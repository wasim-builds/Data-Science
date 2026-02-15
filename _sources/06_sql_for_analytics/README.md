# 📊 SQL for Analytics

Master SQL for data analysis with hands-on examples and practice exercises.

## 📚 Module Overview

This module teaches you SQL from basics to advanced analytics techniques. All examples use Python's `sqlite3` library for easy practice.

### Prerequisites
- Basic Python knowledge
- Pandas basics (helpful but not required)

### Estimated Time
**12-15 hours** (including practice)

---

## 📖 Notebooks

### [01_sql_basics.ipynb](01_sql_basics.ipynb)
**Difficulty:** 🟢 Beginner  
**Time:** 2-3 hours

**Topics:**
- Creating tables
- Inserting data
- SELECT queries
- WHERE filtering
- GROUP BY aggregation
- Basic JOINs

**Key Concepts:**
- SQL syntax fundamentals
- Data types
- Primary keys
- Simple aggregations

---

### [02_advanced_queries.ipynb](02_advanced_queries.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 3-4 hours

**Topics:**
- Subqueries (scalar, column, correlated)
- CASE statements
- COALESCE and NULL handling
- String functions (UPPER, LOWER, CONCAT, SUBSTR)
- Date/time functions
- HAVING clause
- DISTINCT

**Key Concepts:**
- Conditional logic in SQL
- NULL value handling
- Text manipulation
- Advanced filtering

---

### [03_window_functions.ipynb](03_window_functions.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 3-4 hours

**Topics:**
- ROW_NUMBER, RANK, DENSE_RANK
- LAG and LEAD
- Running totals
- Moving averages
- PARTITION BY
- Percentage of total

**Key Concepts:**
- Window function syntax
- OVER clause
- Frame specifications
- Real-world analytics

**Use Cases:**
- Sales rankings
- Time series analysis
- Cohort analysis
- Growth calculations

---

### [04_ctes_and_complex_joins.ipynb](04_ctes_and_complex_joins.ipynb)
**Difficulty:** 🔴 Advanced  
**Time:** 3-4 hours

**Topics:**
- Common Table Expressions (CTEs)
- Recursive CTEs
- Self joins
- INNER vs OUTER joins
- Multiple table joins
- Cross joins

**Key Concepts:**
- Query organization with CTEs
- Hierarchical data
- Complex join patterns
- Join performance

**Use Cases:**
- Organizational charts
- Multi-table analytics
- Data quality checks

---

### [05_sql_practice_exercises.ipynb](05_sql_practice_exercises.ipynb)
**Difficulty:** 🟢🟡🔴 Mixed  
**Time:** 2-3 hours

**Content:**
- 10+ practice problems
- Beginner to advanced
- E-commerce database
- Solutions included
- Real-world scenarios

**Topics Covered:**
- Customer analytics
- Revenue analysis
- Product affinity
- Cohort analysis
- RFM segmentation

---

## 🎯 Learning Path

### Week 1: Foundations
1. Complete `01_sql_basics.ipynb`
2. Practice basic queries
3. Start `02_advanced_queries.ipynb`

### Week 2: Analytics
4. Finish `02_advanced_queries.ipynb`
5. Complete `03_window_functions.ipynb`
6. Try beginner exercises

### Week 3: Advanced
7. Complete `04_ctes_and_complex_joins.ipynb`
8. Finish all practice exercises
9. Build your own analytics queries

---

## 💡 Key Takeaways

After completing this module, you'll be able to:

✅ Write complex SQL queries  
✅ Perform window function analytics  
✅ Use CTEs for clean code  
✅ Join multiple tables effectively  
✅ Handle NULL values properly  
✅ Calculate running totals and moving averages  
✅ Rank and segment data  
✅ Solve real-world analytics problems  

---

## 🔧 Setup

All notebooks use SQLite (in-memory), so no installation needed!

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
```

---

## 📊 Real-World Applications

### Business Analytics
- Sales performance tracking
- Customer segmentation
- Revenue forecasting
- Inventory analysis

### Marketing
- Campaign effectiveness
- Customer lifetime value
- Cohort analysis
- Funnel analysis

### Operations
- Process optimization
- Resource allocation
- Trend identification
- KPI dashboards

---

## 🚀 Next Steps

After mastering SQL:
1. ✅ Practice on real databases (PostgreSQL, MySQL)
2. ✅ Combine SQL with Python (pandas + SQL)
3. ✅ Build dashboards (Streamlit, Dash)
4. ✅ Learn database design
5. ✅ Explore data warehousing

---

## 📚 Additional Resources

### Online Practice
- [LeetCode SQL](https://leetcode.com/problemset/database/)
- [HackerRank SQL](https://www.hackerrank.com/domains/sql)
- [SQLZoo](https://sqlzoo.net/)

### Documentation
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [MySQL Reference](https://dev.mysql.com/doc/)

### Books
- "SQL for Data Analysis" by Cathy Tanimura
- "Learning SQL" by Alan Beaulieu

---

## 🤝 Tips for Success

1. **Practice Daily** - Write queries every day
2. **Start Simple** - Master basics before advanced
3. **Use Real Data** - Practice with actual datasets
4. **Optimize Queries** - Learn about performance
5. **Read Others' Code** - Learn from examples

---

**Happy querying! 🎉**
