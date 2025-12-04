# Savings Prediction Model

## Overview
A **machine learning regression model** that predicts an individual's **monthly savings** based on key financial and personal features. Designed to provide insights for budgeting and financial planning.

## Features
- `income_type` – Type of income (salary, freelance, business)  
- `financial_scenario` – Financial context  
- `credit_score` – Credit score  
- `emergency_fund` – Available emergency fund  
- `investment_amount` – Monthly investment  
- `loan_payment` – Monthly loan payment  
- `monthly_expense_total` – Total monthly expenses  
- `monthly_income` – Total monthly income  
- `rent_or_mortgage` – Rent or mortgage payment  
- `subscription_services` – Total subscription costs  

## Model Details
- **Type**: Regression (predicts `monthly_savings`)  
- **Libraries**: Python, scikit-learn, pandas, numpy  
- **Status**: Hyperparameter tuned; deployment as interactive demo planned  

## Quick Start
1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
````

2. Install dependencies:

```bash
pip install pandas numpy scikit-learn
```

3. Train the model (example):

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

data = pd.read_csv('data/savings_data.csv')
X = data[['income_type','financial_scenario','credit_score','emergency_fund',
          'investment_amount','loan_payment','monthly_expense_total',
          'monthly_income','rent_or_mortgage','subscription_services']]
y = data['monthly_savings']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Lasso()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)
```

## Evaluation

Use metrics like **MSE** or **R²** to evaluate model performance.

## Future Improvements

* Deploy Streamlit interactive demo
* Add more financial indicators for accuracy
* Improve model interpretability

## Author

**Ezechukwu Princewill** – [GitHub Profile](https://github.com/princewillezechukwu3-lang)
