import dash
from dash import Dash, html
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ], use_pages=True)

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("About", active="exact", href="/about")),
        dbc.NavItem(dbc.NavLink("The Data", active="exact", href="/data")),
        dbc.NavItem(dbc.NavLink("Dashboard", active="exact", href="/dashboard")),
        dbc.NavItem(dbc.NavLink("The Model", active="exact", href="/model")),
        
    ],
    pills=True
)

app.layout = dbc.Container([
    nav,
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)