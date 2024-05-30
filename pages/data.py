import pandas as pd
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

dataset_info = "Our model uses the Customer Churn Dataset found on Kaggle, modified from two datasets (one testing, one training) to create a single dataset."

dataset_link = dcc.Link("Click to view Source", href="https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset")

feature_info = "The dataset we used for our modal contains the follow features:"

feature1 = "Age: the numeric age of the customer"

feature2 = "Gender: whether the customer is male or female"

feature3 = "Tenure: the length of time, in months, the customer has used the company's services"

feature4 = "Subscription Type: the type of subscription (Basic, Standard, or Premium) the customer chose"

feature5 = "Contract Type: the type of contract (Monthly, Quarterly, or Annual) the customer chose"

feature6 = "Total Spent: the total amount of money the customer has invested in the company's products or services"

feature7 = "Delayed Payment: how long, in days, the customer went past due on their payment in the last month"

feature8 = "Usage Frequency: the number of times the customer has use the company's servies in the last month"

feature9 = "Last Interaction: the number of days since the customer last had contact with any aspect of the company"

feature10 = "Support Calls: the number of calls the customer made to customer support in the last month"

feature_df = pd.DataFrame(
    {
        "Feature": ["Age", "Gender", "Tenure", "Subscription Type", "Contract Type", "Total Spent", "Delayed Payment", 
                    "Usage Frequency", "Last Interaction", "Support Calls"],
        "Feature Description": ["the numeric age of the customer", "whether the customer is male or female", 
                                "the length of time, in months, the customer has used the company's services",
                               "the type of subscription (Basic, Standard, or Premium) the customer chose", 
                               "the type of contract (Monthly, Quarterly, or Annual) the customer chose",
                               "the total amount of money the customer has invested in the company's products or services",
                               "how long, in days, the customer went past due on their payment in the last month",
                               "the number of times the customer has use the company's servies in the last month",
                               "the number of days since the customer last had contact with any aspect of the company",
                               "the number of calls the customer made to customer support in the last month"]
    }
)

feature_table = dbc.Table.from_dataframe(feature_df, striped=True, bordered=True, hover=True, responsive=True)

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

image_features = "assets/features-importances.png"


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("The Data")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Source Information")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.P(dataset_info),
            dataset_link
        ], className="fs-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Dataset Features")
        ], className="mt-3")
    ]),
    dbc.Row([
        dbc.Col([
            feature_table
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Features by Importance")
        ], className="mt-3")
    ]),
    dbc.Row([
        dbc.Col([
            html.Img(src=image_features)
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Algorthm Investigation Results")
        ], className="mt-3")
    ]),
    dbc.Row([
        dbc.Col([
            table
        ], width=8)
    ]),
])


dash.register_page(__name__)