# 🗄️ SQL Cheat Sheet

## 🔍 Basics
```sql
SELECT col1, col2
FROM table
WHERE condition
ORDER BY col1 DESC
LIMIT 10;
```

## ➕ Aggregation
```sql
SELECT category, COUNT(*), AVG(price)
FROM sales
GROUP BY category
HAVING COUNT(*) > 5;
```

## 🔗 Joins
```sql
-- Inner Join (Matches only)
SELECT * 
FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id;

-- Left Join (All left, matches right)
SELECT * 
FROM table1 t1
LEFT JOIN table2 t2 ON t1.id = t2.id;
```

## 🪟 Window Functions
```sql
-- Ranking
RANK() OVER (PARTITION BY dept ORDER BY salary DESC)

-- Running Total
SUM(sales) OVER (ORDER BY date)

-- Previous Row
LAG(sales) OVER (ORDER BY date)
```

## 🏗️ CTEs
```sql
WITH regional_sales AS (
    SELECT region, SUM(amount) as total
    FROM sales
    GROUP BY region
)
SELECT * FROM regional_sales WHERE total > 10000;
```
