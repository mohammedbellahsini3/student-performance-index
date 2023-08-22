import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Load the dataset
data = pd.read_csv(r'C:\Users\moham\OneDrive\Bureau\projects\regression\multiple linear regression\Student_Performance.csv')

# Identify categorical columns
categorical_columns = ['Extracurricular Activities']

# Perform one-hot encoding
data_encoded = pd.get_dummies(data, columns=categorical_columns, drop_first=True, dtype=int)

# Splitting data into Independent and Dependent Variable
x = data_encoded.drop("Performance Index", axis=1)  # Use data_encoded here
y = data_encoded["Performance Index"]

# Splitting data into Train and Test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Training a Linear Regression Model
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting Test Set Results
y_pred = regressor.predict(x_test)

# Calculate metrics
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print('R Square:', r2)
print('Mean Squared Error:', mse)

# Save the trained model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(regressor, model_file)
