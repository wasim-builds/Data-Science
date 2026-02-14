# Excel for Data Analysts

Excel remains one of the most widely used tools for data analysis. It's excellent for quick data inspection, ad-hoc analysis, and sharing small datasets.

## Key Concepts

### 1. Lookup Functions
These functions allow you to merge data from different tables based on a common key.

**VLOOKUP (Vertical Lookup)**
- **Syntax**: `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`
- **Use Case**: Finding the price of a product ID in a sales table by looking it up in a product master table.
- **Tip**: Always use `FALSE` (or 0) for exact match in `[range_lookup]`.

**XLOOKUP** (Newer, Better)
- **Syntax**: `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`
- **Why it's better**: Can look left, defaults to exact match, and handles errors gracefully.

### 2. Pivot Tables
Pivot Tables are the most powerful feature in Excel for summarizing data.
- **How to create**: Select your data -> Insert -> PivotTable by Dragging fields into:
    - **Rows**: Dimensions you want to group by (e.g., Region, Product Category)
    - **Columns**: Secondary grouping (e.g., Year, Quarter)
    - **Values**: Metrics you want to aggregate (e.g., Sum of Sales, Count of Orders)
    - **Filters**: Subset the data (e.g., specific country)

### 3. Conditional Formatting
Visually highlight important data points.
- **Top/Bottom Rules**: Highlight top 10 values.
- **Color Scales**: Create a heatmap effect (Green for high, Red for low).
- **Data Bars**: Mini bar charts inside cells.

### 4. Data Cleaning
Before analyzing, you must clean your data.
- **Remove Duplicates**: Data -> Remove Duplicates.
- **Text to Columns**: Split a column (e.g., "Lastname, Firstname") into two columns using a delimiter.
- **Trim**: `=TRIM(A1)` removes extra spaces.

## Practice Exercise
1. Create a CSV file with columns: `OrderID`, `Product`, `Category`, `Sales`, `Date`.
2. Open it in Excel.
3. Create a **Pivot Table** showing Total Sales by Category.
4. Use **Conditional Formatting** to highlight Sales > $500.
5. Create a new column `Year` using the `=YEAR(Date)` function.
