import pandas as pd
import plotly as px
from dash import Dash, html, dcc, Input, Output
from modules.data_summary import create_data_summary
from modules.products import setup_product_insights
from modules.seasonal_purchases import setup_purchase_insights
from modules.map import map_figure
from modules.customer_demographic import create_demographics_figure

df = pd.read_csv('./dataset/shopping_trends_updated.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("CSC 805 Visualization Project: Shopping Trends", style={'textAlign': 'center'}),

    html.Div(create_data_summary(), style={'border': '1px solid black', 'padding': '10px', 'margin': '10px'}),

    html.Div([
        html.H2("Best Sellers Map"),
        dcc.Graph(figure=map_figure(), style={'width': '100%', 'height': '750px'})
    ], style={'margin': '10px', 'border':'1px solid black', 'padding':'10px'}),

    setup_purchase_insights(app, df),

    html.Div([
        html.H2("Customer Demographics"),
        dcc.Graph(id='demographics-graph'),
        html.Label('Age Range:'),
        dcc.RangeSlider(
            id='age-range-slider',
            min=df['Age'].min(),
            max=df['Age'].max(),
            step=1,
            value=[df['Age'].min(), df['Age'].max()],
            marks={str(age): str(age) for age in range(df['Age'].min(), df['Age'].max() + 1, 5)}
        ),
        html.Label('Select Gender:'),
        dcc.Dropdown(
            id='gender-dropdown',
            options=[{'label': gender, 'value': gender} for gender in df['Gender'].unique()] + [{'label': 'All', 'value': 'All'}],
            value=['All'],
            multi=True
        ),
    ], style={'margin': '10px', 'border': '1px solid black', 'padding': '10px'}),
], style={'fontFamily': 'Arial, sans-serif'})

@app.callback(
    Output('demographics-graph', 'figure'),
    [Input('age-range-slider', 'value'),
     Input('gender-dropdown', 'value')]
)
def update_demographics_graph(selected_age_range, selected_genders):
    return create_demographics_figure(df, selected_age_range, selected_genders)

if __name__ == '__main__':
    app.run_server(debug=True)
