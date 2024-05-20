import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


ALLOWED_TYPE = ("number")
age = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")
gender = dcc.RadioItems(["Female", "Male"], inline=True, id="memory-gender")
tenure = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")
subscription = dcc.Dropdown(["Basic", "Standard", "Premium"], id="memory-subscription")
contract = dcc.Dropdown(["Monthly", "Quarterly", "Annual"], id="memory-contract")
spent = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")
delayed_payment = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")
usage = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")
last_interaction = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")
support = dcc.Input(id="input_{}.format(ALLOWED_TYPE)")


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("The Model", className="align-center")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Random Forest with XBoost Optimization")
        ]),
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown(
                '''<Insert information about the model here. Maybe.>'''
            )
        ]),
    ]),
    dbc.Row([
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Try it!")
        ]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown("""
                Input single-user data in the fields below for a case-by-case analysis, 
                or upload a CSV or Excel file with the information formatted as described 
                below for multi-user analysis. 
            """)
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H6("Age:")
        ]),
        dbc.Col([
            age
        ]),
        dbc.Col([
            html.H6("Gender:")
        ]),
        dbc.Col([
            gender
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H6("Tenure:")
        ]),
        dbc.Col([
            tenure
        ]),
        dbc.Col([
            html.H6("Subscription Type:")
        ]),
        dbc.Col([
            subscription
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H6("Contract Type:")
        ]),
        dbc.Col([
            contract
        ]),
        dbc.Col([
            html.H6("Total Spent:")
        ]),
        dbc.Col([
            spent
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H6("Payment Delayed (days):")
        ]),
        dbc.Col([
            delayed_payment
        ]),
        dbc.Col([
            html.H6("Usage Frequency:")
        ]),
        dbc.Col([
            usage
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H6("Last Interation:")
        ]),
        dbc.Col([
            last_interaction
        ]),
        dbc.Col([
            html.H6("Number of Supoort Calls:")
        ]),
        dbc.Col([
            support
        ])
    ]),
    dbc.Row([
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([])
    ])
])


dash.register_page(__name__)