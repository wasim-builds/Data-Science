# Advanced Excel Formulas

Master powerful Excel formulas for data analysis.

## 1. INDEX-MATCH

**Better than VLOOKUP!** More flexible and faster.

### Syntax
```excel
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```

### Example: Find Price by Product Name
```excel
=INDEX(B2:B10, MATCH("Laptop", A2:A10, 0))
```

**Advantages over VLOOKUP:**
- ✅ Can look left (VLOOKUP can't)
- ✅ Faster for large datasets
- ✅ Column changes don't break formula

### Two-Way Lookup
```excel
=INDEX(B2:E10, 
       MATCH("Product A", A2:A10, 0),
       MATCH("Q2", B1:E1, 0))
```

---

## 2. SUMIFS / COUNTIFS / AVERAGEIFS

Multiple criteria aggregation.

### SUMIFS
Sum with multiple conditions.

**Syntax:**
```excel
=SUMIFS(sum_range, criteria_range1, criteria1, 
        criteria_range2, criteria2, ...)
```

**Example:** Total sales for "Laptop" in "East" region
```excel
=SUMIFS(D2:D100, A2:A100, "Laptop", 
        B2:B100, "East")
```

### COUNTIFS
Count with multiple conditions.

**Example:** Count orders > $500 from "West"
```excel
=COUNTIFS(C2:C100, ">500", B2:B100, "West")
```

### AVERAGEIFS
Average with conditions.

**Example:** Average salary in Engineering dept
```excel
=AVERAGEIFS(C2:C50, B2:B50, "Engineering")
```

---

## 3. Array Formulas

Perform multiple calculations at once.

### SUM + IF (Array Formula)
**Old way (Ctrl+Shift+Enter):**
```excel
{=SUM(IF(A2:A10="East", B2:B10, 0))}
```

**New way (Excel 365):**
```excel
=SUM(IF(A2:A10="East", B2:B10, 0))
```

### SUMPRODUCT
Multiply arrays and sum results.

**Example:** Total revenue (price × quantity)
```excel
=SUMPRODUCT(B2:B10, C2:C10)
```

**With condition:**
```excel
=SUMPRODUCT((A2:A10="Laptop")*(B2:B10)*(C2:C10))
```

---

## 4. Error Handling

### IFERROR
Handle errors gracefully.

**Syntax:**
```excel
=IFERROR(formula, value_if_error)
```

**Example:**
```excel
=IFERROR(VLOOKUP(A2, Table1, 2, 0), 
         "Not Found")
```

### IFNA
Specifically for #N/A errors.

```excel
=IFNA(VLOOKUP(A2, Table1, 2, 0), 0)
```

---

## 5. Text Functions

### CONCATENATE / TEXTJOIN

**Old way:**
```excel
=CONCATENATE(A2, " ", B2)
```

**Better way:**
```excel
=A2 & " " & B2
```

**Best way (Excel 365):**
```excel
=TEXTJOIN(" ", TRUE, A2:C2)
```

### LEFT, MID, RIGHT
Extract parts of text.

```excel
=LEFT(A2, 5)          // First 5 characters
=MID(A2, 3, 4)        // 4 chars starting at position 3
=RIGHT(A2, 3)         // Last 3 characters
```

### TRIM
Remove extra spaces.

```excel
=TRIM(A2)
```

### UPPER / LOWER / PROPER
Change case.

```excel
=UPPER(A2)            // ALL CAPS
=LOWER(A2)            // all lowercase
=PROPER(A2)           // Title Case
```

---

## 6. Date Functions

### TODAY / NOW
```excel
=TODAY()              // Current date
=NOW()                // Current date and time
```

### DATE / YEAR / MONTH / DAY
```excel
=DATE(2023, 12, 25)   // Create date
=YEAR(A2)             // Extract year
=MONTH(A2)            // Extract month
=DAY(A2)              // Extract day
```

### DATEDIF
Calculate date differences.

```excel
=DATEDIF(A2, B2, "D")    // Days
=DATEDIF(A2, B2, "M")    // Months
=DATEDIF(A2, B2, "Y")    // Years
```

### EOMONTH
End of month.

```excel
=EOMONTH(A2, 0)       // End of current month
=EOMONTH(A2, 1)       // End of next month
```

---

## 7. Logical Functions

### IF with AND/OR
```excel
=IF(AND(A2>100, B2="Yes"), "Approved", "Rejected")
=IF(OR(A2>1000, B2="VIP"), "Priority", "Normal")
```

### Nested IF
```excel
=IF(A2>=90, "A",
   IF(A2>=80, "B",
      IF(A2>=70, "C", "F")))
```

### IFS (Excel 365)
Cleaner than nested IF.

```excel
=IFS(A2>=90, "A",
     A2>=80, "B",
     A2>=70, "C",
     TRUE, "F")
```

---

## 8. Lookup Functions

### XLOOKUP (Excel 365)
Modern replacement for VLOOKUP.

**Syntax:**
```excel
=XLOOKUP(lookup_value, lookup_array, 
         return_array, [if_not_found])
```

**Example:**
```excel
=XLOOKUP(A2, Products, Prices, "Not Found")
```

**Advantages:**
- ✅ Can look left or right
- ✅ Default exact match
- ✅ Built-in error handling
- ✅ Can return multiple columns

---

## 9. Statistical Functions

### RANK
```excel
=RANK(A2, $A$2:$A$10, 0)  // 0 = descending
```

### PERCENTILE
```excel
=PERCENTILE(A2:A100, 0.75)  // 75th percentile
```

### QUARTILE
```excel
=QUARTILE(A2:A100, 1)  // Q1
=QUARTILE(A2:A100, 3)  // Q3
```

---

## 10. Real-World Examples

### Example 1: Sales Commission
```excel
=IF(B2>10000, B2*0.15,
   IF(B2>5000, B2*0.10, B2*0.05))
```

### Example 2: Age from Birthdate
```excel
=DATEDIF(A2, TODAY(), "Y")
```

### Example 3: Extract Domain from Email
```excel
=MID(A2, FIND("@", A2)+1, LEN(A2))
```

### Example 4: Conditional Sum with Multiple Criteria
```excel
=SUMIFS(Sales, Region, "East", 
        Product, "Laptop", 
        Date, ">=1/1/2023")
```

---

## Practice Exercises

### Exercise 1
Create a formula to categorize sales:
- "High" if > $1000
- "Medium" if $500-$1000
- "Low" if < $500

### Exercise 2
Use INDEX-MATCH to find employee salary 
by employee ID.

### Exercise 3
Calculate total revenue for products 
sold in Q1 2023 in the "West" region.

---

## Tips for Success

1. **Use Named Ranges** - Easier to read
2. **Avoid Volatile Functions** - NOW(), TODAY() slow down sheets
3. **Use Tables** - Structured references are cleaner
4. **Test with Small Data** - Before applying to large datasets
5. **Document Complex Formulas** - Add comments

---

## Common Mistakes to Avoid

❌ Using VLOOKUP instead of INDEX-MATCH  
❌ Not locking references with $  
❌ Nested IFs instead of IFS  
❌ Not handling errors  
❌ Hard-coding values instead of cell references  

---

**Next:** [Pivot Tables Deep Dive](03_pivot_tables_deep_dive.md) →
