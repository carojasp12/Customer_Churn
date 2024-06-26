import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# create variables for textual content for ease of editing and visualization
image_path = 'assets/churn-image.jpg'

churn_header = "So what is churn?"

churn_body = """
'Churn,' also know as customer attrition, describes the phenomenon where a customer ends their relationship with a company, frequently for a competing service.
The separation can be permanent or temporary, but it results in a complete termination of services for the duration.
"""

churn_business_header = "What does churn mean for my business?"

churn_business_body1 = """
Since churn describes the erosion of a business's customer base, it results in lost revenue.
When considering a single customer, that might not seem like much.
But what if you were looking at your entire customer base?
"""

churn_business_body2 = """
The metric generally used to look at churn is churn rate, which calculates the number of customers dropping a business's services within a given timeframe.
Churn rate is a critical metric, especially within the telecommunication and financial inductries, which rely on subscription services to maintain their revenue.
"""

churn_business_body3 = """
The purpose of this project isn't to identify how quickly you're losing customers, though.
It's to help you identify who you're losing so you can employ better-targeted marketing campaigns aimed at customer retention.
Or identify problems within your business that are pushing your customers to leave.
"""

help_header = "How can you help me determine which customers are leaving?"

help_body = """
Through machine learning and data analysis. 
You can learn more about how we can help, and even take advantage of our model, by checking out our other pages.
"""

help_body2 = "To learn more about the members of Perfectionists-Under-Pressure+, check out our About page."

more_header = "But I want to know more now!"

more_body1 = "Sure!"

more_body2 = "According to our data, the most important features related to churn are:"

more_body3 = "1. Support calls"

more_body4 = "2. Delayed payment, and"

more_body5 = "3. Total spend"

more_body6 = """
Very likely, without any additional information, those details are painting a picture for you.
Perhaps you, like me, imagine that a high number of support calls, and excessive or consistent tardiness making payments, makes a customer likely to churn.
Maybe we imagine that a customer who has invested a lot of money in the company is more likely to stay.
"""

more_body7 = "But what if it's not that simple?"

more_body8 = "Where before we looked at the most important features, let's look at the least:"

more_body9 = "3. Usage frequency"

more_body10 = "2. Type of subscription (Basic, Standard, Premium)"

more_body11 = "1. Gender"

more_body12 = "But does 'less important' mean 'not important at all'?"

more_body13 = "Upload some customer data to our model and let it tell you, or decide for yourself."

image_atrribution = """The above image rightfully belongs to Burlington Press. It is being used here for educational purposes.
"""

attribution_link = dcc.Link("Image Source", href="https://burlingtonpress.com/2023/12/11/understanding-customer-churn-why-do-customers-switch-to-competing-service-providers/")

# define layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("To Churn or Not to Churn")
        ], className="mt-4")
    ]),
    dbc.Row([
        dbc.Col([
            html.Img(src=image_path)
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1("A Machine Learning Project by: Perfectionists-Under-Pressure+")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2(churn_header)
        ], className="mt-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.P(churn_body)
        ], className="fs-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.H2(churn_business_header)
        ], className="mt-3")
    ]),
    dbc.Row([
        dbc.Col([
            html.P(churn_business_body1),
            html.Br(),
            html.P(churn_business_body2),
            html.Br(),
            html.P(churn_business_body3)
        ], className="fs-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.H2(help_header)
        ], className="mt-3")
    ]),
    dbc.Row([
        dbc.Col([
            html.P(help_body),
            html.Br(),
            html.P(help_body2)
        ], className="fs-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.H2(more_header)
        ], className="mt-3")
    ]),
    dbc.Row([
        dbc.Col([
            html.P(more_body1),
            html.Br(),
            html.P(more_body2),
            html.Ol(more_body3),
            html.Ol(more_body4),
            html.Ol(more_body5),
            html.Br(),
            html.P(more_body6),
            html.Br(),
            html.P(more_body7),
            html.Br(),
            html.P(more_body8),
            html.Ol(more_body9),
            html.Ol(more_body10),
            html.Ol(more_body11),
            html.Br(),
            html.P(more_body12),
            html.Br(),
            html.P(more_body13)
        ], className="fs-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.P([image_atrribution, attribution_link]),
        ], className="mt-2")
    ])
])

# register page to link to app initiation
dash.register_page(__name__, path="/")
