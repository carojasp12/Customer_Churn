import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


about_harsh = """
Harsh brings a background in project management and microbiology to his work in data analytics. 
His commitment to exhaustive and detailed analysis ensures a robust data picture. 
He's proficient with Python and machine learning, and aspires to expand his knowledge and effectiveness within the field.
"""

about_cesar = """
Cesar brings an array of experiences, from roofing to hospitality to travel photography, to his love of mathematics and data analysis. 
Persistent and driven, Cesar leverages his studies in statistics to ensure complete and accurate results from any code he writes. 
He aspires to bring new technologies to fields that have largely been analog.
"""

about_meagan = """
Meagan combines her skills in HTML, Plotly Dash, Python, and data visualization with a steadfast persistence and eagerness to learn. 
With a background in English, she brings a unique perspective to data analysis, excelling in project management and effective communication. 
Megan is driven to transition into the data analysis field, where she aims to leverage her strong analytical capabilities and creative problem-solving skills to deliver insightful and impactful results. 
"""

about_pablo = """
Pablo leverages his drive and passion for sales to make decisions quickly with an eye for best customer result. 
He brings a background in political science, with specialties in Intelligence and National Security, to write code sensitive to the current data market, and seeks to enhance his knowledge and understanding of the field through his current enrollment in the Masters in Analytics program at Georgia Tech. 
He aspires to combine his passions in a data-driven role within the federal government.
"""

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P(about_cesar, className="card-text"),
            dbc.Button("Find Cesar on Github", color="secondary", href="https://github.com/carojasp12"),
            dbc.Button("Find Cesar on LinkedIn", color="success"),
        ]
    ),
    className="mt-3 fs-5 px-0",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P(about_harsh, className="card-text"),
            dbc.Button("Find Harsh on Github", color="secondary", href="https://github.com/10H-K"),
            dbc.Button("Find Harsh on LinkedIn", color="success"),
        ]
    ),
    className="mt-3 fs-5 px-0",
)

tab3_content = dbc.Card(
    dbc.CardBody([
        html.P(about_meagan, className="card=text"),
        dbc.Button("Find Meagan on Github", color="secondary", href="https://github.com/m-coldewe"),
        dbc.Button("Find Meagan on LinkedIn", color="success"),
    ]),
    className="mt-3 fs-5 px-0",
)

tab4_content = dbc.Card(
    dbc.CardBody([
        html.P(about_pablo, className="card=text"),
        dbc.Button("Find Pablo on Github", color="secondary", href="https://github.com/fortichpablo"),
        dbc.Button("Find Pablo on LinkedIn", color="success"),
    ]),
    className="mt-3 fs-5 px-0",
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
    html.Br(), html.H1("About Perfectionists-Under-Pressure+"),
    tabs,
])

dash.register_page(__name__)
