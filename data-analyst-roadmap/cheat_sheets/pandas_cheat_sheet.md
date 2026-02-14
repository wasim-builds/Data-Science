# 🐼 Pandas Cheat Sheet

## 📥 Loading Data
```python
df = pd.read_csv('file.csv')
df = pd.read_excel('file.xlsx')
```

## 🔍 Inspecting
```python
df.head()          # First 5 rows
df.info()          # Types & Missing
df.describe()      # Statistics
df.shape           # (rows, cols)
df.columns         # Column names
```

## 🧹 Cleaning
```python
df.fillna(0)       # Fill NaN with 0
df.dropna()        # Drop rows with NaN
df.drop_duplicates()
df['col'].astype(int)
```

## ✂️ Selection
```python
df['col']          # Select column
df[['col1', 'col2']]
df.loc[0]          # Select row by Label
df.iloc[0]         # Select row by Index
df.query('col > 5')
```

## 📊 Aggregation
```python
df.groupby('col').mean()
df.groupby('col').agg(['min', 'max'])
df.pivot_table(index='col', values='val')
```

## 🔗 Combining
```python
pd.concat([df1, df2])      # Stack vertical
pd.merge(df1, df2, on='id') # Join
```

## 🕒 Time Series
```python
pd.to_datetime(df['date'])
df.resample('M').mean()    # Monthly avg
df.rolling(7).mean()       # 7-day avg
```
