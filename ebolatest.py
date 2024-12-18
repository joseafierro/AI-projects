import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error

# Load and preprocess your data (assuming it's already prepared as in previous steps)
# Sample preprocessing steps if 'features' is ready
# For instance: features = csv_data[['Country_encoded', 'Indicator_encoded', 'Year', 'Month', 'Day', 'value']]
# Uncomment the following line if you have the 'features' variable ready
# features = features  # Replace with actual processed data

# Splitting features and target
X = features.drop(columns=['value'])
y = features['value']

# Scaling the features for better neural network performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Building the neural network using scikit-learn's MLPRegressor
mlp = MLPRegressor(hidden_layer_sizes=(64, 32, 16), activation='relu',
                   solver='adam', learning_rate_init=0.001, max_iter=500, random_state=42)

# Training the model
mlp.fit(X_train, y_train)

# Evaluating the model o
