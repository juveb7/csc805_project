import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

def setup_purchase_insights(app, df):
    # APP LAYOUT
    layout = html.Div(children=[
        html.H1(children='Seasonal Purchase Totals By Item'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': item, 'value': item} for item in df['Item Purchased'].unique()],
            value='Blouse'
        ),
        dcc.Graph(id='bar_graph')
    ], style={'border': '1px solid black', 'padding': '10px', 'margin': '10px'})

    # CALLBACK FUNCTION
    @app.callback(
        Output(component_id='bar_graph', component_property='figure'),
        Input(component_id='dropdown', component_property='value')
    )
    def update_graph(dropdown):
        dff = df[df['Item Purchased'] == dropdown]

        barchart = px.histogram(
            dff,
            x='Season',
            y='Purchase Amount (USD)',
            color='Season',
            color_discrete_sequence=['pink', 'orange', 'blue', 'brown']
        )

        return barchart

    return layout
