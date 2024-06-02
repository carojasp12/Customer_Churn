# Why do customer Churn or not Churn? 

# Introduction 
In today's competitive business environment, understanding why customers churn is essential for maintaining a loyal customer base. Leveraging advanced machine learning tools, we have identified the top three main reasons behind customer churn, as well as the three least significant factors. By using these sophisticated analytical tools, businesses can predict customer behavior more accurately, allowing for the development of targeted strategies to enhance customer retention and reduce churn.

# Churning
Churning refers to the phenomenon where customers or employees stop using a product or service, or leave a company. This is often seen as a negative metric, indicating dissatisfaction or better opportunities elsewhere. Churning is particularly significant in subscription-based businesses, where customer retention is crucial for revenue stability.

# Non-Churning
Non-churning refers to customers or employees who remain loyal to a company or continue to use its products or services over time. Non-churning is indicative of satisfaction, value perception, and strong relationships.

# Tools 
To understand and predict customer churn, we employ a variety of advanced machine learning tools. Our application utilizes Pandas for data manipulation and analysis, SQLite3 to manage and query our database, and NumPy for numerical operations. We leverage Scikit-learn for essential functions such as data preprocessing with StandardScaler, data splitting with train_test_split, and modeling with SVC and RandomForestClassifier. Additionally, we incorporate XGBoost to implement gradient boosting algorithms for enhanced predictive accuracy. To evaluate our models, we use a range of metrics including confusion_matrix, accuracy_score, classification_report, and f1_score. By integrating these powerful tools, we can deliver precise insights into customer behavior, aiding businesses in developing effective retention strategies.

Under the folder resources, you will find the datasets we used and the database file (db file), providing all the necessary data for this project.

# Requirements

Data Model Implementation (25 points)
A Python script initializes, trains, and evaluates a model (10 points)

The data is cleaned, normalized, and standardized prior to modeling (5 points)

The model utilizes data retrieved from SQL or Spark (5 points)

The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared. (5 points)

Data Model Optimization (25 points)
The model optimization and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (15 points)

Overall model performance is printed or displayed at the end of the script (10 points)

GitHub Documentation (25 points)
GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)

The README is customized as a polished presentation of the content of the project (15 points)

Group Presentation (25 points)
All group members speak during the presentation. (5 points)

Content, transitions, and conclusions flow smoothly within any time restrictions. (5 points)

The content is relevant to the project. (10 points)

The presentation maintains audience interest. (5 points)


# Process

Home

About

Etc Below


# Results

# The top three reasons according to our model that will likely cause a customer to churn are as follows # 

1. Higher call rate to the support department
2. Customer is paying past the payment due date on a consistent basis
3. The customer has a high total spend overtime 

# The top 3 reasons that do not affect if a customer is going or churn or not churn #

1. Gender
2. The type of subcription (Basic, Standard, Premium)
3. Usage frequency

# Summary





# Extra information

# Hypothesis - We infer that a customer will not churn if

1. The product is excellent meaning that there will be less support calls
2. The customer pays on a consistent basis meaning they enjoy and use the product
3. The customer has a low spend overtime

Look at our HTML to see if our Hypothesis was correct.

In order to find if out if our hypothesis was correct we developed a Machine Learning model in order to predict if a customer was going to churn or not churn based on circumstances. Our model was 93% accurate overall. 

Refer to the file titled Algorithms.


