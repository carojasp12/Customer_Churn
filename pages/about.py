import dash
from dash import html, dcc
import dash_bootstrap_components as dbc



tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(
    dbc.CardBody([
        html.P("This is card 3. Don't shoot", className="card=text"),
        dbc.Button("Click here", color="success"),
    ]),
    className="mt-3",
)

tab4_content = dbc.Card(
    dbc.CardBody([
        html.P("Pablo Fortich. Graduate from Universitty of Central Florida class of 2024. Soon to attend Georgia Tech to earn my masters in Analytics.", className="card=text"),
        dbc.Button("Click here", color="success"),
    ]),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Cesar"),
        dbc.Tab(tab2_content, label="Harsh"),
        dbc.Tab(tab3_content, label="Meagan"),
        dbc.Tab(tab4_content, label="Pablo"),
    ]
)

layout = dbc.Container([
    html.H1("About Perfections-Under-Pressure+"),
    tabs,
])
dash.register_page(__name__)
