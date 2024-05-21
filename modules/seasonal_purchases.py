import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

def setup_purchase_insights(app, df):

    #APP LAYOUT
    app.layout = html.Div(children = [
        html.H1(children='Seasonal Purchase Totals By Item'),
        dcc.Dropdown(df['Item Purchased'].unique(), 'Blouse', id='dropdown'),
        dcc.Graph(id='bar_graph')
    ], style={'border': '1px solid black', 'padding': '10px', 'margin': '10px'})

    
    #CALLBACK FUNCTION
    @app.callback(
        Output(component_id='bar_graph', component_property='figure'),
        Input(component_id='dropdown', component_property='value')
    )

    def update_graph(dropdown):

        dff = df[df['Item Purchased']==dropdown]
        seasons = dff['Season']
        purchamt = dff['Purchase Amount (USD)']

        print(dropdown)

        barchart = px.histogram(
                dff,
                x=dff['Season'], 
                y=dff['Purchase Amount (USD)'],
                color='Season',
                color_discrete_sequence=['pink','orange','blue','brown']
                )
        
        return barchart

    return app.layout
                           