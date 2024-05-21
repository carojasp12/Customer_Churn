# Import Dependencies
import plotly.express as px
import sqlite3
import pandas as pd
import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Load 'customer_churn_visualization' Into Pandas DataFrame
conn=sqlite3.connect('Resources/customer_churn_data.db')
query = "SELECT * FROM customer_churn_visualization"
customer_churn_visualization = pd.read_sql(query, conn)
conn.close()

# Intialize Horizontal Age Bar Chart To Be Displayed
customer_churn_visualization['Age Bins'] = pd.cut(customer_churn_visualization['Age'], bins=10)
age_counts = customer_churn_visualization['Age Bins'].value_counts().reset_index()
age_counts.columns = ['Age Bins', 'Count']
age_counts['Age Bins'] = age_counts['Age Bins'].astype(str)
age_counts = age_counts.sort_values(by='Age Bins')
hbar_chart_age = px.bar(age_counts,
                        y='Age Bins',
                        x='Count',
                        orientation='h',
                        title='Customer Count by Age',
                        color_discrete_sequence=['mediumvioletred'])
hbar_chart_age.update_layout(paper_bgcolor='black',
                             plot_bgcolor='rgba(0, 0, 0, 0)',
                             font=dict(color='white'),
                             title_x=0.5,
                             yaxis_title="Age Categories",
                             xaxis_title="Customer Count",
                             title_font_size=26,
                             margin=dict(l=40, r=5, t=60, b=40))

# Intialize Horizontal Spending Bar Chart To Be Displayed
customer_churn_visualization['Rounded Spend'] = customer_churn_visualization['Total Spend'].round()
spend_counts = customer_churn_visualization['Rounded Spend'].value_counts().reset_index()
spend_counts.columns = ['Spend', 'Count']
spend_counts['Spend Bins'] = pd.cut(spend_counts['Spend'], bins=15)
spend_counts['Spend Bins'] = pd.Categorical(spend_counts['Spend Bins'], categories=sorted(spend_counts['Spend Bins'].cat.categories), ordered=True)
spend_counts = spend_counts.sort_values(by='Spend Bins')
binned_data = spend_counts.groupby('Spend Bins')['Count'].sum().reset_index()
binned_data['Spend Bins'] = binned_data['Spend Bins'].astype(str)
hbar_chart_spend = px.bar(binned_data,
                          y='Spend Bins',
                          x='Count',
                          orientation='h',
                          title='Customer Count by Spending',
                          color_discrete_sequence=['mediumvioletred'])
hbar_chart_spend.update_layout(paper_bgcolor='black',
                               plot_bgcolor='rgba(0, 0, 0, 0)',
                               font=dict(color='white'),
                               title_x=0.5,
                               yaxis_title="Spending Categories",
                               xaxis_title="Customer Count",
                               title_font_size=26,
                               margin=dict(l=40, r=5, t=60, b=40))

# Intialize Horizontal Tenure Bar Chart To Be Displayed
customer_churn_visualization['Tenure Bins'] = pd.cut(customer_churn_visualization['Tenure'], bins=10)
tenure_counts = customer_churn_visualization['Tenure Bins'].value_counts().reset_index()
tenure_counts.columns = ['Tenure Bins', 'Count']
tenure_counts['Tenure Bins'] = pd.Categorical(tenure_counts['Tenure Bins'], categories=sorted(customer_churn_visualization['Tenure Bins'].cat.categories), ordered=True)
tenure_counts = tenure_counts.sort_values(by='Tenure Bins')
tenure_counts['Tenure Bins'] = tenure_counts['Tenure Bins'].astype(str)
hbar_chart_tenure = px.bar(tenure_counts, 
                           y='Tenure Bins', 
                           x='Count', 
                           orientation='h', 
                           title='Customer Count by Tenure',
                           labels={'Tenure Bins': 'Tenure Categories (Months)', 'Count': 'Customer Count'},
                           color_discrete_sequence=['mediumvioletred'])
hbar_chart_tenure.update_layout(paper_bgcolor='black',
                                plot_bgcolor='rgba(0, 0, 0, 0)',
                                font=dict(color='white'),
                                title_x=0.5,
                                title_font_size=26,
                                margin=dict(l=40, r=5, t=60, b=40))

# Intialize Composite Line Graph To Be Displayed
x_range = list(range(0, 31))
columns_to_examine = ["Usage Frequency", "Support Calls", "Payment Delay", "Last Interaction"]
count_data = {'Value': x_range}
for column in columns_to_examine:
    count_data[column] = [customer_churn_visualization[column].eq(value).sum() for value in x_range]
count_df = pd.DataFrame(count_data)
long_format_df = pd.melt(count_df,
                         id_vars=['Value'],
                         value_vars=columns_to_examine, 
                         var_name='Feature',
                         value_name='Count')
composite_line_graph = px.line(long_format_df, 
                               x='Value', 
                               y='Count', 
                               color='Feature',
                               title="Customer Count by Feature",
                               labels={'Value': 'Count of Instances', 'Count': 'Customer Count', 'Feature': 'Feature'})
composite_line_graph.update_layout(paper_bgcolor='black',
                                   font=dict(color='white'),
                                   title_x=0.5,
                                   title_font_size=26,
                                   margin=dict(l=40, r=5, t=60, b=40))


# Define The Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Label('Select Filter Criteria:', style={'font-size': '30px', 'margin-top': '20px', 'margin-left': '20px', 'font-weight': 'bold'}),
            dbc.Checklist(
                options=[
                    {"label": "Subscription Type", "value": "subscription"},
                    {"label": "Contract Length", "value": "contract"}
                ],
                value=[],
                id="filter-criteria",
                inline=True,
                style={"font-size": "20px", "margin-left": "20px"}),
        ],width=4),
        dbc.Col([
            html.Div(id='subscription-filter', children=[
                html.Label('Subscription Type:', style={'font-size': '20px', 'margin-top': '20px'}),
                dcc.Dropdown(
                    id='subscription-dropdown',
                    options=[
                        {'label': 'Basic Subscription', 'value': 'Basic'},
                        {'label': 'Standard Subscription', 'value': 'Standard'},
                        {'label': 'Premium Subscription', 'value': 'Premium'}
                    ],
                    value=[],
                    placeholder='Select Subscription(s)',
                    multi=True,
                    clearable=False,
                    style={'color': 'black', 'font-size': '15px', 'font-weight': 'bold', 'margin-right': '20px'}
                ),
            ], style={'display': 'none'}),
        ], width=4),
        dbc.Col([
            html.Div(id='contract-filter', children=[
                html.Label('Contract Length:', style={'font-size': '20px', 'margin-top': '20px'}),
                dcc.Dropdown(
                    id='contract-dropdown',
                    options=[
                        {'label': 'Monthly Contract', 'value': 'Monthly'},
                        {'label': 'Quarterly Contract', 'value': 'Quarterly'},
                        {'label': 'Annual Contract', 'value': 'Annual'}
                    ],
                    value=[],
                    placeholder='Select Contract(s)',
                    multi=True,
                    clearable=False,
                    style={'color': 'black', 'font-size': '15px', 'font-weight': 'bold', 'margin-right': '20px'}
                ),
            ], style={'display': 'none'}),
        ], width=4),
    ]),
     dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(html.Button('Total Customers',
                                    id='total-customers',
                                    n_clicks=0, 
                                    style={'font-size': '22px',
                                           'font-weight': 'bold',
                                           'margin-top': '20px',
                                           'width': '100%',
                                           'height': '100px',
                                           'background-color': '#FFEBCD'}), 
                                    width=3,
                                    style={'padding': '0 10px'}),
                dbc.Col(html.Button('Churned Customers',
                                    id='churned-customers',
                                    n_clicks=0, 
                                    style={'font-size': '22px',
                                           'font-weight': 'bold',
                                           'margin-top': '20px',
                                           'width': '100%',
                                           'height': '100px',
                                           'background-color': '#FFEBCD'}), 
                                    width=3,
                                    style={'padding': '0 10px'}),
                dbc.Col(html.Button('Female Customers',
                                    id='female-customers',
                                    n_clicks=0, 
                                    style={'font-size': '22px',
                                           'font-weight': 'bold',
                                           'margin-top': '20px',
                                           'width': '100%',
                                           'height': '100px',
                                           'background-color': '#FFEBCD'}),
                                    width=3,
                                    style={'padding': '0 10px'}),
                dbc.Col(html.Button('Male Customers',
                                    id='male-customers',
                                    n_clicks=0, 
                                    style={'font-size': '22px',
                                           'font-weight': 'bold',
                                           'margin-top': '20px',
                                           'width': '100%',
                                           'height': '100px',
                                           'background-color': '#FFEBCD'}), 
                                    width=3,
                                    style={'padding': '0 10px'}),
            ], style={'margin-left': '0px', 'margin-right': '0px'}),
            dbc.Row([
                dbc.Col(dcc.Graph(id='age-bar', figure=hbar_chart_age), width=4),
                dbc.Col(dcc.Graph(id='spend-bar', figure=hbar_chart_spend), width=4),
                dbc.Col(dcc.Graph(id='tenure-bar', figure=hbar_chart_tenure), width=4)
            ], style={'margin-top': '20px'}),
            dbc.Row([
                dbc.Col(dcc.Graph(id='composite-line', figure=composite_line_graph), width=12)
            ], style={'margin-top': '20px', 'margin-bottom': '20px'}),
        ], width=12)
    ])
], fluid=True)

# DataFrame Filtering Function
def filter_dataframe(selected_subscription=[], selected_contract=[]):
    filtered_dataframe = customer_churn_visualization.copy()
    if selected_subscription:
        filtered_dataframe = filtered_dataframe[filtered_dataframe['Subscription Type'].isin(selected_subscription)]
    if selected_contract:
        filtered_dataframe = filtered_dataframe[filtered_dataframe['Contract Length'].isin(selected_contract)]
    return filtered_dataframe

# Callback To Show/Hide Filters Based On Checklist Selection
@callback(
    [Output('subscription-filter', 'style'),
     Output('contract-filter', 'style')],
    [Input('filter-criteria', 'value')]
)

# Function To Show/Hide Filters Based On Checklist Selection
def toggle_filters(selected_filters):
    subscription_display = {'display': 'block'} if 'subscription' in selected_filters else {'display': 'none'}
    contract_display = {'display': 'block'} if 'contract' in selected_filters else {'display': 'none'}
    return subscription_display, contract_display

# Callback To Update Graphs Based On Filter Criteria
@callback(
    [Output('age-bar', 'figure'),
     Output('spend-bar', 'figure'),
     Output('tenure-bar', 'figure'),
     Output('composite-line', 'figure')],
    [Input('subscription-dropdown', 'value'),
     Input('contract-dropdown', 'value')]
)

# Function To Update Graphs Based On Filter Criteria
def update_graph(selected_subscription, selected_contract):
    filtered_df = filter_dataframe(selected_subscription, selected_contract)

    # Update Age Horizontal Bar Chart
    filtered_df['Age Bins'] = pd.cut(filtered_df['Age'], bins=10)
    age_counts = filtered_df['Age Bins'].value_counts().reset_index()
    age_counts.columns = ['Age Bins', 'Count']
    age_counts['Age Bins'] = age_counts['Age Bins'].astype(str)
    age_counts = age_counts.sort_values(by='Age Bins')
    hbar_chart_age = px.bar(age_counts, 
                            y='Age Bins', 
                            x='Count', 
                            orientation='h', 
                            title='Customer Count by Age',
                            color_discrete_sequence=['mediumvioletred'])
    hbar_chart_age.update_layout(paper_bgcolor='black',
                                 plot_bgcolor='rgba(0, 0, 0, 0)',
                                 font=dict(color='white'),
                                 title_x=0.5,
                                 yaxis_title="Age Categories",
                                 xaxis_title="Customer Count",
                                 title_font_size=26,
                                 margin=dict(l=40, r=5, t=60, b=40))
    
    # Update Spending Horizontal Bar Chart
    filtered_df['Rounded Spend'] = filtered_df['Total Spend'].round()
    spend_counts = filtered_df['Rounded Spend'].value_counts().reset_index()
    spend_counts.columns = ['Spend', 'Count']
    spend_counts['Spend Bins'] = pd.cut(spend_counts['Spend'], bins=15)
    spend_counts['Spend Bins'] = pd.Categorical(spend_counts['Spend Bins'], categories=sorted(spend_counts['Spend Bins'].cat.categories), ordered=True)
    spend_counts = spend_counts.sort_values(by='Spend Bins')
    binned_data = spend_counts.groupby('Spend Bins')['Count'].sum().reset_index()
    binned_data['Spend Bins'] = binned_data['Spend Bins'].astype(str)
    hbar_chart_spend = px.bar(binned_data,
                              y='Spend Bins',
                              x='Count',
                              orientation='h',
                              title='Customer Count by Spending',
                              color_discrete_sequence=['mediumvioletred'])
    hbar_chart_spend.update_layout(paper_bgcolor='black',
                                   plot_bgcolor='rgba(0, 0, 0, 0)',
                                   font=dict(color='white'),
                                   title_x=0.5,
                                   yaxis_title="Spending Categories",
                                   xaxis_title="Customer Count",
                                   title_font_size=26,
                                   margin=dict(l=40, r=5, t=60, b=40))
    
    # Update Tenure Horizontal Bar Chart
    filtered_df['Tenure Bins'] = pd.cut(filtered_df['Tenure'], bins=10)
    tenure_counts = filtered_df['Tenure Bins'].value_counts().reset_index()
    tenure_counts.columns = ['Tenure Bins', 'Count']
    tenure_counts['Tenure Bins'] = pd.Categorical(tenure_counts['Tenure Bins'], categories=sorted(customer_churn_visualization['Tenure Bins'].cat.categories), ordered=True)
    tenure_counts = tenure_counts.sort_values(by='Tenure Bins')
    tenure_counts['Tenure Bins'] = tenure_counts['Tenure Bins'].astype(str)
    hbar_chart_tenure = px.bar(tenure_counts,
                               y='Tenure Bins',
                               x='Count',
                               orientation='h',
                               title='Customer Count by Tenure',
                               labels={'Tenure Bins': 'Tenure Categories (Months)', 'Count': 'Customer Count'},
                               color_discrete_sequence=['mediumvioletred'])
    hbar_chart_tenure.update_layout(paper_bgcolor='black',
                                    plot_bgcolor='rgba(0, 0, 0, 0)',
                                    font=dict(color='white'),
                                    title_x=0.5,
                                    title_font_size=26,
                                    margin=dict(l=40, r=5, t=60, b=40))
    
    # Update Composite Line Graph
    x_range = list(range(0, 31))
    columns_to_examine = ["Usage Frequency", "Support Calls", "Payment Delay", "Last Interaction"]
    count_data = {'Value': x_range}
    for column in columns_to_examine:
        count_data[column] = [filtered_df[column].eq(value).sum() for value in x_range]
    count_df = pd.DataFrame(count_data)
    long_format_df = pd.melt(count_df,
                             id_vars=['Value'],
                             value_vars=columns_to_examine,
                             var_name='Feature',
                             value_name='Count')
    composite_line_graph = px.line(long_format_df,
                                   x='Value',
                                   y='Count',
                                   color='Feature',
                                   title="Customer Count by Feature",
                                   labels={'Value': 'Count of Instances',
                                           'Count': 'Customer Count',
                                           'Feature': 'Feature'})
    composite_line_graph.update_layout(paper_bgcolor='black',
                                       font=dict(color='white'),
                                       title_x=0.5,
                                       title_font_size=26,
                                       margin=dict(l=40, r=5, t=60, b=40))
    
    
    return hbar_chart_age, hbar_chart_spend, hbar_chart_tenure, composite_line_graph

# Callbacks To Update The Buttons
@callback(
    [Output('total-customers', 'children'),
     Output('male-customers', 'children'),
     Output('female-customers', 'children'),
     Output('churned-customers', 'children')],
    [Input('subscription-dropdown', 'value'),
     Input('contract-dropdown', 'value')]
)

# Function To Update The Buttons
def update_buttons(selected_subscription, selected_contract):
    filtered_df = filter_dataframe(selected_subscription, selected_contract)
    total_count = len(filtered_df)
    male_count = len(filtered_df[filtered_df['Gender'] == 'Male'])
    female_count = len(filtered_df[filtered_df['Gender'] == 'Female'])
    churned_count = len(filtered_df[filtered_df['Churn'] == 1.0])
    return (
        f'Total Customers: {total_count}', 
        f'Male Customers: {male_count}', 
        f'Female Customers: {female_count}', 
        f'Churned Customers: {churned_count}'
    )

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__)
