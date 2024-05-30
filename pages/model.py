import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
from data_processing import math

# Define the variable inputs for the model
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

# describe the model
about_random_forest = """
Random Forest is an ensemble learning method used for classification and regression tasks. 
It operates by constructing a multitude of decision trees during training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. 
Key aspects of the Random Forest model that suited our objective include: """
random_aspect1 = "1. effective management of datasets with a large number of features by selecting subsets for each split, reducing the risk of overfitting"
random_aspect2 = "2. ability to combine the outputs of multiple decision trees, which reduces model variance and prevents overfitting"
random_aspect3 = "3. capability of capturing complex, non-linear relationships between features and the target variable"
random_aspect4 = "4. robustness to noisy data and outliers, as the ensemble approach averages out their effects, leading to more stable and reliable predictions"

single_user_input = """
Input single-user data in the fields below for a case-by-case analysis, or upload a CSV or Excel file with the information formatted as described 
below for multi-user analysis. 
            """

# define the layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("The Model")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Random Forest")
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            html.P(about_random_forest),
            html.Ol(random_aspect1),
            html.Ol(random_aspect2),
            html.Ol(random_aspect3),
            html.Ol(random_aspect4)
        ], className="fs-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Try It!")
        ], className="mt-4")
    ]),
    dbc.Row([
        dbc.Col([
            html.P(single_user_input)
        ], className="fs-5 mb-2")
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Age:")
        ]),
        dbc.Col([
            age
        ]),
        dbc.Col([
            html.H5("Gender:")
        ]),
        dbc.Col([
            gender
        ])
     ]),
    dbc.Row([
        dbc.Col([
            html.H5("Tenure:")
        ]),
        dbc.Col([
            tenure
        ]),
        dbc.Col([
            html.H5("Subscription Type:")
        ]),
        dbc.Col([
            subscription
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Contract Type:")
        ]),
        dbc.Col([
            contract
        ]),
        dbc.Col([
            html.H5("Total Spent:")
        ]),
        dbc.Col([
            spent
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Payment Delayed (days):")
        ]),
        dbc.Col([
            delayed_payment
        ]),
        dbc.Col([
            html.H5("Usage Frequency:")
        ]),
        dbc.Col([
            usage
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Last Interaction:")
        ]),
        dbc.Col([
            last_interaction
        ]),
        dbc.Col([
            html.H5("Number of Supoort Calls:")
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