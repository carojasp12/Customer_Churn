# To Churn or Not to Churn

<img width="718" alt="Screenshot 2024-06-02 at 6 41 53 PM" src="https://github.com/carojasp12/Customer_Churn/assets/152929248/a8a80760-d6d5-4f18-93b1-96563c7d23be">

## Introduction 
In today's competitive business environment, understanding why customers churn is essential for maintaining a loyal customer base. Leveraging advanced machine learning tools, we have identified the top three main reasons behind customer churn, as well as the three least significant factors. By using these sophisticated analytical tools, businesses can predict customer behavior more accurately, allowing for the development of targeted strategies to enhance customer retention and reduce churn.

#### Churning
Churning refers to the phenomenon where customers or employees stop using a product or service, or leave a company. This is often seen as a negative metric, indicating dissatisfaction or better opportunities elsewhere. Churning is particularly significant in subscription-based businesses, where customer retention is crucial for revenue stability.

#### Non-Churning
Non-churning refers to customers or employees who remain loyal to a company or continue to use its products or services over time. Non-churning is indicative of satisfaction, value perception, and strong relationships.

## Tools 
To understand and predict customer churn, we employ a variety of advanced machine learning tools. Our application utilizes Pandas for data manipulation and analysis, SQLite3 to manage and query our database, and NumPy for numerical operations. We leverage Scikit-learn for essential functions such as data preprocessing with StandardScaler, data splitting with train_test_split, and modeling with SVC and RandomForestClassifier. Additionally, we incorporate XGBoost to implement gradient boosting algorithms for enhanced predictive accuracy. To evaluate our models, we use a range of metrics including confusion_matrix, accuracy_score, classification_report, and f1_score. By integrating these powerful tools, we can deliver precise insights into customer behavior, aiding businesses in developing effective retention strategies.

Under the folder resources, you will find the datasets we used and the database file (db file), providing all the necessary data for this project.

## Pages

<img width="397" alt="Screenshot 2024-06-02 at 6 50 54 PM" src="https://github.com/carojasp12/Customer_Churn/assets/152929248/86220a68-e959-4b97-8f05-924a86ed983e">


### Home

Welcome to our homepage! Here, we delve into the concept of churn and its implications for businesses. Utilizing Dash, a Python web framework for building analytical web applications, and Bootstrap, a popular CSS framework for responsive design, we've crafted an informative and visually engaging interface.

### About
Get to know the talented individuals driving this project forward.

### Data

Our model uses the Customer Churn Dataset found on Kaggle, modified from two datasets (one testing, one training) to create a single dataset. Refer to the resources folder. 

The dataset we used for our model contains the follow features:

* Age: the numeric age of the customer
* Gender: whether the customer is male or female
* Tenure: the length of time, in months, the customer has used the company's services
* Subscription Type: the type of subscription (Basic, Standard, or Premium) the customer chose
* Contract Type: the type of contract (Monthly, Quarterly, or Annual) the customer chose
* Total Spent: the total amount of money the customer has invested in the company's products or services
* Delayed Payment: how long, in days, the customer went past due on their payment in the last month
* Usage Frequency: the number of times the customer has use the company's servies in the last month
* Last Interaction: the number of days since the customer last had contact with any aspect of the company

### Dashboard
<img width="500" alt="Screenshot 2024-06-02 at 6 52 31 PM" src="https://github.com/carojasp12/Customer_Churn/assets/152929248/0d39026c-128e-47fe-aedb-cc64a00ff052">

On this page, we present an interactive dashboard designed to assist business owners in utilizing our machine learning model to predict whether a customer is likely to churn or remain loyal. This tool provides valuable insights by visualizing customer data through various interactive charts and graphs. By leveraging these predictive analytics, businesses can make informed decisions to improve customer retention strategies and address potential issues proactively.

## Results

### Complete Dataset Correlation Matrix

![complete_dataset_correlation_matrix](https://github.com/carojasp12/Customer_Churn/assets/152045367/aa9a3a04-d0e0-45e2-be72-fcaa6c35a171)

### Algorithm Testing Results

![investigation_results](https://github.com/carojasp12/Customer_Churn/assets/152045367/0ddeb6be-b1e9-4a11-b0c0-0fa4cd7ca8ae)

The above chart represents the highest accuracy scores achieved by each model following tuning. As you can see, the Random Forest Classifier achieved the highest accuracy.

### Random Forest Feature Importances
![Screenshot 2024-06-02 at 6 28 58 PM](https://github.com/carojasp12/Customer_Churn/assets/152929248/17ff8d60-5818-45aa-8952-135f5f9f8d4f)

The above Feature Importance chart identifies Support Calls, Total Spend, and Payment Delay as the features that contribute most to determining whether a customer will churn. Our machine learning model, with its impressive accuracy rate of 93%, can use data including these features to help identify at-risk customers. By leveraging this model, business owners can proactively address potential issues, implement targeted retention strategies, and ultimately reduce customer churn. This high level of predictive accuracy allows for more informed decision-making, helping businesses maintain a stable and loyal customer base.

<img width="472" alt="Screenshot 2024-06-02 at 6 54 19 PM" src="https://github.com/carojasp12/Customer_Churn/assets/152929248/03ece066-465a-47bd-b72c-1137da064d9d">


Importance of Our ML Model in Helping Business Owners Retain Clients

Our machine learning model plays a crucial role in helping business owners retain clients by:

Predictive Insights: The model analyzes various customer-related factors to predict which clients are at risk of churning. This allows businesses to identify and address potential issues before customers decide to leave.

Targeted Marketing: By understanding the likelihood of churn, businesses can create targeted marketing campaigns aimed at retaining high-risk customers, offering personalized incentives and solutions to keep them engaged.

Resource Optimization: With accurate churn predictions, businesses can allocate their resources more efficiently, focusing their efforts on the customers who need the most attention and support.

Data-Driven Decisions: The insights provided by our model enable business owners to make informed decisions based on data, rather than intuition, leading to more effective strategies for customer retention.

Identifying Patterns: The model helps in identifying common patterns and trends among customers who churn, providing valuable feedback that can be used to improve products, services, and customer interactions.

By leveraging our ML model, business owners can proactively manage customer relationships, reduce churn rates, and ultimately enhance their overall profitability and growth.



