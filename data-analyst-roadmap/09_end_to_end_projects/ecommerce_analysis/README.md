# E-Commerce Analysis Project

A comprehensive analysis of customer behavior and retention.

## 📂 Project Structure

### 1. [Data Generation](01_data_generation.ipynb)
- Creates a synthetic dataset (`ecommerce_data.csv`) mimicking real-world transactions.
- Fields: InvoiceNo, StockCode, Quantity, Date, Price, CustomerID, Country.

### 2. [RFM Analysis](02_rfm_analysis.ipynb)
- **Recency:** Days since last purchase.
- **Frequency:** Total count of orders.
- **Monetary:** Total value spent.
- **Outcome:** Segments customers into "Champions", "Loyal", "At Risk", etc.

### 3. [Cohort Analysis](03_cohort_analysis.ipynb)
- Groups customers by their first purchase month.
- Tracks retention rates over time (Month 0 to Month 12).
- **Outcome:** Heatmap showing how well you keep customers.

## 🚀 How to Run
1. Run `01_data_generation.ipynb` to create the CSV file.
2. Run `02_rfm_analysis.ipynb` to segment customers.
3. Run `03_cohort_analysis.ipynb` to view retention.

## 📊 Key Skills
- Pandas Grouping & Aggregation
- Date/Time Manipulation
- Customer Segmentation Logic
- Heatmap Visualization
