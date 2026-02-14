# 📊 Statistics for Data Analysis

Master statistical concepts for data-driven decisions.

## 📚 Module Overview

Learn essential statistics for analyzing data, testing hypotheses, and making informed business decisions.

### Prerequisites
- Python basics
- Pandas proficiency
- Basic math knowledge

### Estimated Time
**12-15 hours**

---

## 📖 Content

### [01_descriptive_statistics.ipynb](01_descriptive_statistics.ipynb)
**Difficulty:** 🟢 Beginner  
**Time:** 2-3 hours

**Topics:**
- Mean, median, mode
- Variance and standard deviation
- Percentiles and quartiles
- Data distributions

---

### [02_probability_distributions.ipynb](02_probability_distributions.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 3 hours

**Topics:**
- Normal distribution
- Binomial distribution
- Poisson distribution
- Central Limit Theorem

---

### [03_hypothesis_testing.ipynb](03_hypothesis_testing.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 4 hours

**Topics:**
- One-sample t-test
- Two-sample t-test
- Paired t-test
- Chi-square test
- ANOVA
- p-values and significance

**Key Concepts:**
- **Null Hypothesis (H₀):** No effect
- **Alternative Hypothesis (H₁):** Effect exists
- **p-value:** Probability under H₀
- **α (alpha):** Significance level (0.05)

---

### [04_correlation_analysis.ipynb](04_correlation_analysis.ipynb)
**Difficulty:** 🟡 Intermediate  
**Time:** 3 hours

**Topics:**
- Pearson correlation
- Spearman correlation
- Correlation matrices
- Heatmaps
- Causation vs correlation

**Use Cases:**
- Feature selection
- Multicollinearity detection
- Relationship discovery

---

### [05_ab_testing.ipynb](05_ab_testing.ipynb)
**Difficulty:** 🔴 Advanced  
**Time:** 3-4 hours

**Topics:**
- A/B test design
- Conversion rate testing
- Sample size calculation
- Confidence intervals
- Sequential testing
- Common pitfalls

**Real-World Applications:**
- Website optimization
- Email campaigns
- Product features
- Pricing strategies

---

## 🎯 Learning Path

### Week 1: Foundations
1. Review descriptive statistics
2. Understand distributions
3. Practice with real data

### Week 2: Inference
4. Master hypothesis testing
5. Learn t-tests and chi-square
6. Interpret p-values correctly

### Week 3: Relationships
7. Analyze correlations
8. Create correlation matrices
9. Understand causation

### Week 4: Experiments
10. Design A/B tests
11. Calculate sample sizes
12. Run your own test

---

## 💡 Key Takeaways

After this module, you'll be able to:

✅ Summarize data with statistics  
✅ Test hypotheses rigorously  
✅ Measure relationships  
✅ Design A/B tests  
✅ Make data-driven decisions  
✅ Avoid statistical pitfalls  
✅ Communicate findings clearly  

---

## 🚀 Real-World Applications

### Business
- A/B testing features
- Customer segmentation
- Sales forecasting
- Quality control

### Marketing
- Campaign effectiveness
- Conversion optimization
- Customer behavior analysis
- Pricing experiments

### Product
- Feature prioritization
- User experience testing
- Performance metrics
- Engagement analysis

### Operations
- Process improvement
- Defect detection
- Resource optimization
- Risk assessment

---

## 🔧 Tools & Libraries

### Core Libraries
```bash
pip install scipy statsmodels
```

### Key Functions
```python
from scipy import stats

# t-test
stats.ttest_ind(group_a, group_b)

# Correlation
stats.pearsonr(x, y)

# Chi-square
stats.chi2_contingency(table)
```

---

## 📊 Statistical Tests Quick Reference

| Test | Use Case | Data Type |
|------|----------|-----------|
| One-sample t-test | Compare to known value | Continuous |
| Two-sample t-test | Compare 2 groups | Continuous |
| Paired t-test | Before/after | Continuous |
| Chi-square | Independence | Categorical |
| ANOVA | Compare 3+ groups | Continuous |
| Correlation | Relationship | Continuous |

---

## 🤝 Best Practices

### Hypothesis Testing
✅ Define hypothesis before collecting data  
✅ Use appropriate test for data type  
✅ Check assumptions (normality, etc.)  
✅ Report effect size, not just p-value  

### A/B Testing
✅ Calculate sample size upfront  
✅ Randomize assignment  
✅ Run test to completion  
✅ Avoid peeking at results  

### Interpretation
✅ Consider practical significance  
✅ Report confidence intervals  
✅ Acknowledge limitations  
✅ Avoid p-hacking  

---

## ⚠️ Common Mistakes

❌ Confusing correlation with causation  
❌ Using wrong statistical test  
❌ Ignoring assumptions  
❌ Multiple testing without correction  
❌ Stopping A/B test too early  
❌ Cherry-picking significant results  
❌ Misinterpreting p-values  

---

## 📚 Additional Resources

### Books
- "Statistics Done Wrong" by Alex Reinhart
- "Naked Statistics" by Charles Wheelan
- "The Art of Statistics" by David Spiegelhalter

### Online
- [Khan Academy: Statistics](https://www.khanacademy.org/math/statistics-probability)
- [Seeing Theory](https://seeing-theory.brown.edu/)
- [StatQuest YouTube](https://www.youtube.com/c/joshstarmer)

### Tools
- [Evan's Awesome A/B Tools](https://www.evanmiller.org/ab-testing/)
- [Sample Size Calculator](https://www.optimizely.com/sample-size-calculator/)

---

## 🎓 Practice Projects

### Project 1: Customer Analysis
Analyze customer data:
- Segment customers
- Test differences between segments
- Find correlations with revenue

### Project 2: A/B Test
Design and analyze A/B test:
- Choose metric
- Calculate sample size
- Run simulation
- Interpret results

### Project 3: Survey Analysis
Analyze survey responses:
- Descriptive statistics
- Chi-square tests
- Correlation analysis
- Report findings

---

## 📈 Statistical Significance

### Understanding p-values:
- **p < 0.001:** Very strong evidence
- **p < 0.01:** Strong evidence
- **p < 0.05:** Moderate evidence
- **p ≥ 0.05:** Insufficient evidence

### Effect Size Matters:
Statistical significance ≠ Practical significance

Always consider:
- Magnitude of effect
- Business impact
- Cost vs benefit

---

## 🔄 Descriptive vs Inferential

### Descriptive Statistics
- Summarize data
- Mean, median, std
- Visualizations
- No generalizations

### Inferential Statistics
- Make predictions
- Test hypotheses
- Generalize to population
- Quantify uncertainty

---

## 🚀 Next Steps

After mastering statistics:
1. ✅ Apply to real datasets
2. ✅ Run actual A/B tests
3. ✅ Learn Bayesian statistics
4. ✅ Explore causal inference
5. ✅ Study experimental design

---

**Happy analyzing! 📊**
