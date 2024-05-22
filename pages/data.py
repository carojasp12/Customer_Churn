import pandas as pd
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

dataset_info = "Our model uses the Customer Churn Dataset found on Kaggle, modified from two datasets (one testing, one training) to create a single dataset."

dataset_link = dbc.CardLink("Click to view Source", href="https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset")

feature_info = """
The dataset we used for our modal contains the follow features:
* Age: the numeric age of the customer
* Gender: whether the customer is male or female
* Tenure: the length of time, in months, the customer has used the company's services
* Subscription Type: the type of subscription (Basic, Standard, or Preium) the customer chose
* Contract Type: the type of contract (Monthly, Quarterly, or Annual) the customer chose
* Total Spent: the total amount of money the customer has invested in the company's products or services
* Delayed Payment: how long, in days, the customer went past due on their payment in the last month
* Usage Frequency: the number of times the company has use the company's servies in the last month
* Last Interaction: the number of days since the customer last had contact with any aspect of the company
* Support Calls: the number of calls the customer made to customer support in the last month
"""

df = pd.DataFrame(
    {
        "Model Name": ["Random Forest Classifier", "Extreme Gradient Boosting Classifier (XGBoost)", "Gradient Boosting Classifier", 
                       "K-Nearest_Neighbors Classifier", "Decision Tree Classifier", "Logistic Regression Classifier", 
                       "SVM Classifier (Radial Basis Function Kernel)", "SVM Classifier (Polynomial Kernel)", "SVM Classifier (Linear Kernel)",
                       "SVM Classifier (Sigmoid Kernel)"],
        "Accuracy SCore": ["93.54%", "93.45%", "92.22%", "90.11%", "88.32%", "84.78%", "91.20%", "89.02%", "85.30%", "73.87% "]
    }
)

table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, responsive=True)


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("The Data")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Source Information")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.P(dataset_info),
            dataset_link
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Dataset Features")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown(feature_info)
        ])
    ]),
    dbc.Row([
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Algorthm Investigation Results")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            table
        ], width=8)
    ])
])


dash.register_page(__name__)