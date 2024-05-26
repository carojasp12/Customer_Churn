import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
from data_processing import math

# Define the layout of the app
age = dcc.Input(id='input_box1', type='number')
gender = dcc.RadioItems(["Female", "Male"], inline=True, id="memory-gender")
tenure = dcc.Input(id='input_box2', type='number')
subscription = dcc.Dropdown(["Basic", "Standard", "Premium"], id="memory-subscription",style={'color': 'black'})
contract = dcc.Dropdown(["Monthly", "Quarterly", "Annual"], id="memory-contract",style={'color': 'black'})
spent = dcc.Input(id='input_box3', type='number')
delayed_payment = dcc.Input(id='input_box4', type='number')
usage = dcc.Input(id='input_box5', type='number')
last_interaction = dcc.Input(id='input_box6', type='number')
support = dcc.Input(id='input_box7', type='number')


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("The Model", className="align-center")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Random Forest ")
        ]),
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
        dbc.Col([
            dbc.Button("Submit", id="submit-button", color="primary"),
            dcc.Store(id='store-data')
        ])
    ]),
    dbc.Row([
        dbc.Col([html.Div(id='output_div')
        ])
    ]),
    dbc.Row([
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([])
    ]),
    # dbc.Row([
    #     dbc.Col([
    #         html.H3("Try it!")
    #     ]),
    #     dbc.Col([]),
    #     dbc.Col([]),
    #     dbc.Col([])
    # ])

])

# Define callback to update output based on inputs
@callback(
    Output('store-data', 'data'),
    Input('submit-button', 'n_clicks'),
    [
        State('input_box1', 'value'),
        State('memory-gender', 'value'),
        State('input_box2', 'value'),
        State('memory-subscription', 'value'),
        State('memory-contract', 'value'),
        State('input_box3', 'value'),
        State('input_box4', 'value'),
        State('input_box5', 'value'),
        State('input_box6', 'value'),
        State('input_box7', 'value'),
        
    ]
 )

def update_output(n_clicks, input1, dropdown_value1, input2, dropdown_value2, dropdown_value3, input3, input4, input5, input6, input7 ):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    if dropdown_value1 == 'Female':
        female = 1,
        male = 0,
    else:
        female = 0,
        male = 1,
    if  dropdown_value2 == 'Basic':
        basic = 1,
        standard = 0,
        premium =0  
    elif dropdown_value2 == 'Standard':
        basic = 0,
        standard = 1,
        premium = 0,
    else:
        basic = 0,
        standard = 0,
        premium = 1, 
    if  dropdown_value3 == 'Monthly':
        monthly = 1,
        quarterly = 0,
        annual =0  
    elif dropdown_value3 == 'Quarterly':
        monthly = 0,
        quarterly = 1,
        annual = 0,
    else:
        monthly = 0,
        quarterly = 0,
        annual = 1,     
          

    # Create a dictionary with the input values
    data = {
        
        'age':input1,
        'female': female,
        'male':male,
        'tenure':input2,
        'basic_subscription':basic,
        'standard_subscription':standard,
        'premium_subscription':premium,
        'monthly_contract':monthly,
        'quarterly_contract':quarterly,
        'annual_contract':annual,
        'total_spend': input3,
        'payment_delay':input4,
        'usage_frequency':input5,
        'last_interaction':input6,
        'support_calls':input7
    }
    
    return data
    


# Callback to create DataFrame from stored data and display it
@callback(
    Output('output_div', 'children'),
    Input('store-data', 'data')
)
def display_data(data):
   
    df = pd.DataFrame(data)
    df = df.astype(float)
    prediction = math(df)
    df['churn'] = prediction
    # Convert DataFrame to HTML table
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)  


dash.register_page(__name__)