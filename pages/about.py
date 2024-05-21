import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Find Cesar on Github", color="secondary", href="https://github.com/carojasp12"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Find Harsh on Github", color="secondary", href="https://github.com/10H-K"),
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(
    dbc.CardBody([
        html.P("This is card 3. Don't shoot", className="card=text"),
        dbc.Button("Find Meagan on Github", color="secondary", href="https://github.com/m-coldewe"),
    ]),
    className="mt-3",
)

tab4_content = dbc.Card(
    dbc.CardBody([
        html.P("This is card 4. Don't shoot, please.", className="card=text"),
        dbc.Button("Find Pablo on Github", color="secondary", href="https://github.com/fortichpablo"),
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

# layout = dbc.Container([
#     dbc.Row([]),
#     dbc.Row([
#         dbc.Col([
#             html.H1("About Perfections-Under-Pressure+")
#         ])
#     ]),
#     dbc.Row([]),
#     dbc.Row([
#         dbc.Col([
#             tabs
#         ])
#     ]),
#     dbc.Row
# ])

layout = dbc.Container([
    html.Br(), html.H1("About Perfections-Under-Pressure+"),
    tabs,
])

dash.register_page(__name__)