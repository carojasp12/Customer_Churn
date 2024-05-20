import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


home_content = '''
## What is churn?
This is where we define/describe churn.


## What does churn mean for my business?
This is where we tell them why churn is important for them to consider.


## What can I do to stop churn?
This is where we tell them how we can help.
'''



layout = dbc.Container([
    html.H1("To Churn or Not to Churn"),
    html.H3("A Machine Learning Project by: Perfectionists-Under-Pressure+"),html.Br(),
    dcc.Markdown(home_content),
])

dash.register_page(__name__, path="/")