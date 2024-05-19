import dash
from dash import html, dcc
import dash_bootstrap_components as dbc






layout = dbc.Container([
    html.H1("To Churn or Not to Churn"),
    html.H3("A Machine Learning Project by: Perfectionists-Under-Pressure+"),
])

dash.register_page(__name__, path="/")