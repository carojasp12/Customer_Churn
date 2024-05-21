import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

image_path = 'assets/churn-image.jpg'

home_content = '''
## What is churn?
This is where we define/describe churn.
Churn, also known as customer attrition, refers to the phenomenon where customers stop doing business with a company or cease using its services over a specific period or permanently. 
## What does churn mean for my business?
This is where we tell them why churn is important for them to consider.
It is a critical metric in industries like telecommunications, subscription-based services, and financial services because retaining existing customers is often more cost-effective than acquiring new ones.

## These are the top 3 reasons why customers churn or not churn?

The top three reasons according to our model that will likely cause a customer to churn are as follows

1. Higher call rate to the support department
2. Customer is paying past the payment due date on a consistent basis
3. The customer has a high total spend overtime 

The top 3 reasons that do not affect if a customer is going or churn or not churn

1. Gender
2. The type of subcription (Basic, Standard, Premium)
3. Usage frequency

Hypothesis - We infer that a customer will not churn 

1. The product is excellent meaning that there will be less support calls
2. The customer pays on a consistent basis meaning they enjoy and use the product
3. The customer has a low spend overtime


'''

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("To Churn or Not to Churn")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Img(src=image_path)
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("A Machine Learning Project by: Perfectionists-Under_pressure+")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown(home_content)
        ])
    ])
])

# layout = dbc.Container([
#     html.H1("To Churn or Not to Churn"),
#     html.H3("A Machine Learning Project by: Perfectionists-Under-Pressure+"),html.Br(),
#     dcc.Markdown(home_content),
# ])

dash.register_page(__name__, path="/")
