# Import necessary libraries
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd
import base64
import datetime
import io
# Import 2 functions that run the Random Forest model
from data_processing import manual_input,csv_input

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

# Describe the model
about_random_forest = """
Random Forest is an ensemble learning method used for classification and regression tasks. 
It operates by constructing a multitude of decision trees during training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. 
Key aspects of the Random Forest model that suited our objective include: """
random_aspect1 = "1. Effective management of datasets with a large number of features by selecting subsets for each split, reducing the risk of overfitting"
random_aspect2 = "2. Ability to combine the outputs of multiple decision trees, which reduces model variance and prevents overfitting"
random_aspect3 = "3. Capability of capturing complex, non-linear relationships between features and the target variable"
random_aspect4 = "4. Robustness to noisy data and outliers, as the ensemble approach averages out their effects, leading to more stable and reliable predictions"

single_user_input = """
Input single-user data in the fields below for a case-by-case analysis, or upload a CSV or Excel file with the information formatted as described 
below for multi-user analysis. Results will show 1 if the customer is predicted to churn, and 0 if the customer is predicted to not-churn. 
            """

# Define the layout
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
            html.H5("Tenure (months):")
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
            html.H5("Usage Frequency (days):")
        ]),
        dbc.Col([
            usage
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H5("Last Interaction (days):")
        ]),
        dbc.Col([
            last_interaction
        ]),
        dbc.Col([
            html.H5("Number of Support Calls:")
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
        dbc.Col([
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '120px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),  
    dcc.Store(id='stored-data', storage_type='session'),
    dcc.Store(id='stored-data2', storage_type='session'),
    html.Div(id='output-data-upload'),
    html.Div(id='result-output'),
    dbc.Button("Download CSV", id="btn_csv", color="primary"),
    dcc.Download(id="download-dataframe-csv")

            ])
        ])
    ]),
    dbc.Col([
        dbc.Col([
            html.Br()
        ])
    ])    
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

# Function that gets the single input from user and transform categorical data to 0 and 1  
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

# Function that creates a data frame with customer's input and call manual_input from data_processing
# to run the Random Forest Model. 
def display_data(data):
   
    df = pd.DataFrame(data)
    df = df.astype(float)
    prediction = manual_input(df)
    df['churn'] = prediction
    df = df[['churn','age','female','male','tenure','basic_subscription',
            'standard_subscription','premium_subscription','monthly_contract',
            'quarterly_contract','annual_contract','total_spend','payment_delay',
            'usage_frequency','last_interaction','support_calls']]
    # Convert DataFrame to HTML table
    table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    return html.Div(table, style = {'overflowX': 'auto', 'maxHeight': '500px', 'overflowY': 'auto'})  

# Function to parse uploaded file contents and convert to DataFrame
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        return df    
    except Exception as e:
        print(e)
        return None
        
# Callback to handle file upload and process contents
@callback(Output('output-data-upload', 'children'),
              Output('stored-data', 'data'), 
              Input('upload-data', 'contents'),
              State('upload-data', 'filename')
              )
# Function to handle file upload and process contents
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        for contents, name in zip(list_of_contents, list_of_names):
            df = parse_contents(contents, name)
            if df is not None:
                return f"File {name} successfully uploaded.", df.to_dict('records')
        return "There was an error processing the file.", None
    return "No file uploaded yet.", None

# Callback to process uploaded data and create a DataFrame
@callback(
    Output('result-output', 'children'),
    Output('stored-data2', 'data'), 
    Input('stored-data', 'data')
)
# Function that creates a data frame with uploaded data,transform categorical data to 0 and 1
# and call csv_input from data_processing to run the Random Forest Model. 
def display_data_csv(stored_data):
    if stored_data is not None: 
        df = pd.DataFrame(stored_data)  
        df = pd.get_dummies(df,prefix='',prefix_sep='', columns=['gender','subscription','contract']).astype(int)
        df = df.rename(columns={
        'basic': 'basic_subscription', 'premium': 'premium_subscription', 'standard': 'standard_subscription',
        'annual': 'annual_contract', 'monthly': 'monthly_contract', 'quarterly': 'quarterly_contract'
        })
        df = df[['age','female','male','tenure','basic_subscription',
                 'standard_subscription','premium_subscription','monthly_contract',
                 'quarterly_contract','annual_contract','total_spend','payment_delay',
                 'usage_frequency','last_interaction','support_calls']]
        df = df.astype(float)
        prediction = csv_input(df)
        df['churn'] = prediction
        df = df[['churn','age','female','male','tenure','basic_subscription',
            'standard_subscription','premium_subscription','monthly_contract',
            'quarterly_contract','annual_contract','total_spend','payment_delay',
            'usage_frequency','last_interaction','support_calls']]
    # Convert DataFrame to HTML table
        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
        return html.Div(table, style = {'overflowX': 'auto', 'maxHeight': '500px', 'overflowY': 'auto'}),df.to_dict('records') 
    return "No data available.", None

# Callback to handle CSV download
@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    State('stored-data', 'data'),
    State('stored-data2', 'data'),
    prevent_initial_call=True
)
# Function that merge the original upload file data with the churn column created above

def download_csv(n_clicks,stored_data,stored_data2):
    if stored_data is None:
        return None
    if stored_data2 is None:
        return None
    df = pd.DataFrame(stored_data)
    df2 = pd.DataFrame(stored_data2)
    df['churn'] =  df2['churn']
    # Convert DataFrame to csv file for the user to download
    return dcc.send_data_frame(df.to_csv, "mydf.csv")

dash.register_page(__name__)
