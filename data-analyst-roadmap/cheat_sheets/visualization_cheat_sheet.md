# 📉 Plotly & Viz Cheat Sheet

## 📊 Plotly Express
```python
import plotly.express as px

# Scatter
fig = px.scatter(df, x='gdp', y='life', color='continent')

# Bar
fig = px.bar(df, x='category', y='sales', text_auto=True)

# Line
fig = px.line(df, x='date', y='value', title='Trend')

# Histogram
fig = px.histogram(df, x='age', nbins=20)

# Box
fig = px.box(df, y='score', points='all')
```

## 🎨 Matplotlib Basics
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Line')
plt.scatter(x, y, c='red')
plt.title('Title')
plt.xlabel('X Axis')
plt.legend()
plt.show()
```

## 🌈 Seaborn
```python
import seaborn as sns

sns.heatmap(df.corr(), annot=True)
sns.pairplot(df, hue='class')
sns.histplot(df['col'], kde=True)
```
