# Power Query Basics

Automate data transformation in Excel.

## What is Power Query?

Power Query is Excel's ETL (Extract, Transform, Load) tool.

**Use Cases:**
- ✅ Import data from multiple sources
- ✅ Clean and transform data
- ✅ Combine multiple tables
- ✅ Automate repetitive tasks
- ✅ Create reusable data pipelines

---

## Accessing Power Query

### Excel 2016+
**Data** → **Get & Transform Data**

### Key Buttons
- **Get Data** - Import from sources
- **From Table/Range** - Use Excel data
- **Queries & Connections** - Manage queries

---

## Basic Workflow

### 1. Load Data
**Data** → **From Table/Range**

### 2. Transform
Power Query Editor opens

### 3. Apply Steps
Each action creates a step

### 4. Close & Load
Data loads to Excel

---

## Common Transformations

### 1. Remove Columns
**Home** → **Remove Columns**

**Use Case:** Delete unnecessary fields

### 2. Filter Rows
Click column header → **Filter**

**Use Case:** Remove blanks, filter by value

### 3. Change Data Type
Click column type icon

**Options:**
- Text
- Whole Number
- Decimal Number
- Date
- Date/Time

### 4. Replace Values
**Transform** → **Replace Values**

**Example:** Replace "N/A" with blank

### 5. Split Column
**Transform** → **Split Column**

**By Delimiter:**
- Comma
- Space
- Custom

**By Position:**
- Number of characters

**Use Case:** Split "Last, First" into two columns

### 6. Merge Columns
Select columns → **Transform** → **Merge Columns**

**Use Case:** Combine first and last name

---

## Unpivoting Data

Transform wide data to long format.

### Before (Wide):
| Product | Jan | Feb | Mar |
|---------|-----|-----|-----|
| Laptop  | 100 | 150 | 120 |
| Mouse   | 50  | 60  | 55  |

### After (Long):
| Product | Month | Sales |
|---------|-------|-------|
| Laptop  | Jan   | 100   |
| Laptop  | Feb   | 150   |
| Laptop  | Mar   | 120   |
| Mouse   | Jan   | 50    |
| Mouse   | Feb   | 60    |
| Mouse   | Mar   | 55    |

### How To
1. Select month columns
2. **Transform** → **Unpivot Columns**

---

## Merging Queries

Combine data from multiple tables (like SQL JOIN).

### Types of Merge
- **Left Outer** - All from left, matching from right
- **Right Outer** - All from right, matching from left
- **Full Outer** - All from both
- **Inner** - Only matching rows
- **Left Anti** - Left without matches
- **Right Anti** - Right without matches

### Steps
1. **Home** → **Merge Queries**
2. Select tables
3. Choose join columns
4. Select join type
5. Click **OK**
6. Expand merged column

---

## Appending Queries

Stack tables vertically (like SQL UNION).

### Use Case
Combine monthly sales files into one table.

### Steps
1. **Home** → **Append Queries**
2. Select tables to combine
3. Click **OK**

**Requirement:** Same column structure

---

## Custom Columns

Add calculated columns.

### Example 1: Full Name
```m
[First Name] & " " & [Last Name]
```

### Example 2: Profit Margin
```m
([Revenue] - [Cost]) / [Revenue]
```

### Example 3: Age from Birthdate
```m
Duration.Days(DateTime.LocalNow() - [Birthdate]) / 365
```

---

## Conditional Columns

Like IF statements.

### Example: Categorize Sales
**Add Column** → **Conditional Column**

**Logic:**
- If Sales > 1000 → "High"
- Else if Sales > 500 → "Medium"
- Else → "Low"

---

## Grouping Data

Aggregate data (like SQL GROUP BY).

### Example: Total Sales by Product
1. **Transform** → **Group By**
2. Group by: Product
3. New column: Total Sales
4. Operation: Sum
5. Column: Sales

---

## Data Sources

Power Query can import from:

### Files
- Excel
- CSV
- Text
- JSON
- XML

### Databases
- SQL Server
- MySQL
- PostgreSQL
- Oracle

### Web
- Web pages
- APIs
- SharePoint

### Cloud
- Azure
- Google Sheets
- Salesforce

---

## M Language Basics

Power Query uses M language.

### View Code
**View** → **Advanced Editor**

### Example Query
```m
let
    Source = Excel.CurrentWorkbook(){
        [Name="Sales"]}[Content],
    FilteredRows = Table.SelectRows(
        Source, 
        each [Amount] > 100
    ),
    ChangedType = Table.TransformColumnTypes(
        FilteredRows,
        {{"Amount", type number}}
    )
in
    ChangedType
```

---

## Best Practices

### 1. Data Preparation
✅ Use consistent headers  
✅ Remove extra rows above data  
✅ Ensure data types are correct  
✅ Handle nulls appropriately  

### 2. Query Design
✅ Name queries descriptively  
✅ Add comments to steps  
✅ Organize queries in groups  
✅ Disable load for intermediate queries  

### 3. Performance
✅ Filter early (reduce rows)  
✅ Remove unnecessary columns  
✅ Use query folding when possible  
✅ Avoid complex M code  

### 4. Maintenance
✅ Document transformations  
✅ Test with sample data  
✅ Version control queries  
✅ Refresh regularly  

---

## Common Use Cases

### 1. Combining Monthly Files
Append all CSV files from a folder.

**Steps:**
1. **Data** → **From Folder**
2. Select folder
3. **Combine & Transform**

### 2. Cleaning Messy Data
- Remove blank rows
- Trim whitespace
- Fix data types
- Replace errors

### 3. Creating Date Table
Generate calendar table for analysis.

```m
let
    StartDate = #date(2023, 1, 1),
    EndDate = #date(2023, 12, 31),
    NumberOfDays = Duration.Days(
        EndDate - StartDate
    ) + 1,
    Dates = List.Dates(
        StartDate, 
        NumberOfDays, 
        #duration(1,0,0,0)
    ),
    #"Converted to Table" = 
        Table.FromList(
            Dates, 
            Splitter.SplitByNothing()
        )
in
    #"Converted to Table"
```

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Query Editor | Alt+A+Q+E |
| Refresh All | Ctrl+Alt+F5 |
| Close & Load | Alt+H+C+L |
| Add Custom Column | Alt+A+C+C |
| Group By | Alt+T+G |

---

## Practice Exercises

### Exercise 1
Import CSV file and:
- Remove blank rows
- Change date column to Date type
- Filter for 2023 only

### Exercise 2
Unpivot monthly sales data from 
wide to long format.

### Exercise 3
Merge customer table with orders table 
on Customer ID.

---

## Tips for Success

1. **Start Simple** - Learn basic transforms first
2. **Use UI First** - Then learn M code
3. **Save Queries** - Reuse transformations
4. **Test Incrementally** - Check each step
5. **Document Steps** - Add descriptions

---

## Common Mistakes

❌ Not promoting headers  
❌ Wrong data types  
❌ Not handling nulls  
❌ Loading unnecessary queries  
❌ Not refreshing connections  

---

## Power Query vs Formulas

### Use Power Query When:
✅ Importing external data  
✅ Combining multiple files  
✅ Complex transformations  
✅ Repeatable processes  

### Use Formulas When:
✅ Simple calculations  
✅ Row-by-row logic  
✅ Dynamic updates  
✅ Quick one-off tasks  

---

## Next Steps

After mastering Power Query:
1. ✅ Learn DAX (Power Pivot)
2. ✅ Explore Power BI
3. ✅ Automate with VBA
4. ✅ Connect to databases
5. ✅ Build data pipelines

---

**Resources:**
- [Microsoft Power Query Docs](https://docs.microsoft.com/power-query/)
- [M Language Reference](https://docs.microsoft.com/powerquery-m/)

---

**Next:** [README](README.md) →
