# import necessary libraries
import pandas as pd
import numpy as np
import sqlite3
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, f1_score

# Load 'customer_churn_complete' Into Pandas DataFrame
conn=sqlite3.connect('Resources/customer_churn_data.db')
query = "SELECT * FROM customer_churn_complete"
customer_churn_complete = pd.read_sql(query, conn)
conn.close()


# Define Features Set
X = customer_churn_complete.drop(columns=['churn'])

# Define Target
y = customer_churn_complete['churn']

# Split Into Train And Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5, stratify=y)

# Create StandardScaler Instance
scaler = StandardScaler()

# Fit Standard Scaler
X_scaler = scaler.fit(X_train)

# Scale Training And Testing Data
X_train_scaled = X_scaler.transform(X_train)

# Create Random Forest Classifier
rf_model = RandomForestClassifier(random_state=5)

# Fit The Model
rf_model = rf_model.fit(X_train_scaled, y_train)

# Function that gets the single input from user
# and use the above model to make a churn prediction
def manual_input(user):
   test = X_scaler.transform(user)
   X_test_scaled = test.reshape(1,-1)
   predictions_rf = rf_model.predict(X_test_scaled)
   return predictions_rf 

# Function that gets upload file
# and use the above model to make a churn predictions
def csv_input(file):
   X_test_scaled = X_scaler.transform(file)
   predictions_rf = rf_model.predict(X_test_scaled)
   return predictions_rf 


    