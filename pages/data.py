import pandas as pd
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc





layout = dbc.Container([
    hmtl.H1("The Data"),
    html.H3("Source Information"),
    html.H3("Dataset Features"),
])

dash.register_page(__name__)