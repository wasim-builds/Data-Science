# 🤖 Machine Learning Basics

Introduction to machine learning for data analysts.

## 📚 Module Overview

Learn fundamental ML concepts and build your first predictive models. This module focuses on practical applications for data analysts.

### Prerequisites
- Python basics
- Pandas proficiency
- Statistics fundamentals
- Data visualization skills

### Estimated Time
**15-18 hours**

---

## 📖 Content

### [01_intro_to_ml.ipynb](01_intro_to_ml.ipynb)
**Difficulty:** 🟢 Beginner  
**Time:** 2 hours

**Topics:**
- What is machine learning?
- Supervised vs unsupervised
- Train/test split
- First model (scikit-learn)

---

### [02_linear_regression.ipynb](02_linear_regression.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 4 hours

**Topics:**
- Simple linear regression
- Multiple linear regression
- Model evaluation (R², RMSE, MAE)
- Residual analysis
- Feature importance
- Making predictions

**Dataset:** California Housing

**Key Concepts:**
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

### [03_logistic_regression.ipynb](03_logistic_regression.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 4 hours

**Topics:**
- Binary classification
- Probability predictions
- Confusion matrix
- Precision, recall, F1 score
- ROC curve and AUC
- Threshold tuning

**Dataset:** Breast Cancer

**Use Cases:**
- Customer churn prediction
- Fraud detection
- Disease diagnosis
- Email spam classification

---

### [04_model_evaluation.ipynb](04_model_evaluation.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 3-4 hours

**Topics:**
- Regression metrics (MAE, MSE, RMSE, R²)
- Classification metrics (Accuracy, Precision, Recall)
- Cross-validation
- Learning curves
- Model comparison
- Overfitting vs underfitting

**Key Metrics:**
- **Accuracy:** Overall correctness
- **Precision:** Positive prediction accuracy
- **Recall:** Finding all positives
- **F1 Score:** Balance of precision/recall
- **AUC:** Overall performance

---

### [05_feature_engineering.ipynb](05_feature_engineering.ipynb)
**Difficulty:** 🔴 Advanced  
**Time:** 3-4 hours

**Topics:**
- Handling missing values
- Encoding categorical variables
- Feature scaling (StandardScaler, MinMaxScaler)
- Creating new features
- Binning/discretization
- Date/time features
- Polynomial features

**Dataset:** Titanic

**Techniques:**
```python
# One-hot encoding
df = pd.get_dummies(df, columns=['Category'])

# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# New features
df['BMI'] = df['Weight'] / (df['Height'] ** 2)
```

---

## 🎯 Learning Path

### Week 1: Foundations
1. Complete `01_intro_to_ml.ipynb`
2. Understand train/test split
3. Start `02_linear_regression.ipynb`

### Week 2: Regression
4. Finish linear regression
5. Practice with different datasets
6. Learn evaluation metrics

### Week 3: Classification
7. Complete `03_logistic_regression.ipynb`
8. Master confusion matrix
9. Understand ROC/AUC

### Week 4: Advanced
10. Complete `04_model_evaluation.ipynb`
11. Finish `05_feature_engineering.ipynb`
12. Build end-to-end project

---

## 💡 Key Takeaways

After this module, you'll be able to:

✅ Build regression models  
✅ Create classification models  
✅ Evaluate model performance  
✅ Engineer effective features  
✅ Avoid overfitting  
✅ Make predictions on new data  
✅ Interpret model results  

---

## 🚀 Real-World Applications

### Business
- Sales forecasting
- Customer churn prediction
- Price optimization
- Demand prediction

### Marketing
- Customer segmentation
- Campaign effectiveness
- Lead scoring
- Recommendation systems

### Finance
- Credit risk assessment
- Fraud detection
- Stock price prediction
- Loan approval

### Healthcare
- Disease prediction
- Patient risk scoring
- Treatment effectiveness
- Resource allocation

---

## 🔧 Tools & Libraries

### Core Libraries
```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

### scikit-learn
- Models: `LinearRegression`, `LogisticRegression`
- Metrics: `accuracy_score`, `r2_score`
- Preprocessing: `StandardScaler`, `train_test_split`

---

## 📊 ML Workflow

```
1. Define Problem
   ↓
2. Collect Data
   ↓
3. Explore Data (EDA)
   ↓
4. Feature Engineering
   ↓
5. Train Model
   ↓
6. Evaluate Model
   ↓
7. Tune & Improve
   ↓
8. Deploy & Monitor
```

---

## 🤝 Best Practices

### Data Preparation
✅ Handle missing values  
✅ Remove duplicates  
✅ Scale features  
✅ Encode categories  

### Model Building
✅ Start simple  
✅ Use cross-validation  
✅ Check for overfitting  
✅ Compare multiple models  

### Evaluation
✅ Use appropriate metrics  
✅ Test on unseen data  
✅ Analyze errors  
✅ Document results  

---

## 📚 Additional Resources

### Online Courses
- [Coursera: Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)
- [Fast.ai: Practical Deep Learning](https://www.fast.ai/)

### Books
- "Hands-On Machine Learning" by Aurélien Géron
- "Introduction to Statistical Learning" (free PDF)

### Documentation
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Kaggle Learn](https://www.kaggle.com/learn)

---

## 🎓 Practice Projects

### Project 1: House Price Prediction
Build regression model to predict prices.
- Dataset: Boston Housing or California Housing
- Metrics: R², RMSE
- Features: Location, size, age

### Project 2: Customer Churn
Classify customers likely to leave.
- Dataset: Telco Customer Churn
- Metrics: Precision, Recall, AUC
- Features: Usage, tenure, support calls

### Project 3: Titanic Survival
Predict passenger survival.
- Dataset: Titanic (Kaggle)
- Metrics: Accuracy, F1 score
- Features: Age, class, family size

---

## ⚠️ Common Mistakes

❌ Not splitting data properly  
❌ Using test data for training  
❌ Ignoring feature scaling  
❌ Overfitting to training data  
❌ Wrong evaluation metric  
❌ Not handling missing values  
❌ Forgetting to encode categories  

---

## 🔄 Regression vs Classification

### Use Regression When:
✅ Predicting continuous values  
✅ Output is a number  
✅ Examples: price, temperature, sales  

### Use Classification When:
✅ Predicting categories  
✅ Output is a class  
✅ Examples: spam/not spam, disease/healthy  

---

## 🚀 Next Steps

After mastering ML basics:
1. ✅ Learn ensemble methods (Random Forest, XGBoost)
2. ✅ Explore deep learning
3. ✅ Practice on Kaggle competitions
4. ✅ Build portfolio projects
5. ✅ Deploy models to production

---

**Happy learning! 🤖**
