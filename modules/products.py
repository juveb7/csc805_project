import plotly.express as px
from dash import html, dcc, Output, Input, ctx

def setup_product_insights(app, df):
    # update graph based on the button clicked
    def update_product_graph(rating_nclicks, popularity_nclicks, freq_nclicks):
        button_id = ctx.triggered_id if ctx.triggered else 'rating-btn'

        if button_id == 'rating-btn':
            fig = px.bar(
                df.groupby('Item Purchased')['Review Rating'].mean().reset_index(),
                x='Item Purchased',
                y='Review Rating',
                title='Average Rating by Product'
            )
        elif button_id == 'popularity-btn':
            item_counts = df['Item Purchased'].value_counts().reset_index()
            item_counts.columns = ['Item Purchased', 'Count']
            fig = px.bar(
                item_counts,
                x='Item Purchased',
                y='Count',
                title='Popularity of Products (Number of Purchases)'
            )
        elif button_id == 'freq-btn':
            fig = px.bar(
                df.groupby('Item Purchased')['Frequency_Num'].sum().reset_index(),
                x='Item Purchased',
                y='Frequency_Num',
                title='Purchase Frequency of Products'
            )

        fig.update_layout(xaxis={'categoryorder': 'total descending'})
        return fig

    # callback
    app.callback(
        Output('product-graph', 'figure'),
        [Input('rating-btn', 'n_clicks'),
         Input('popularity-btn', 'n_clicks'),
         Input('freq-btn', 'n_clicks')]
    )(update_product_graph)

    # layout for the product insights section
    product_insights_layout = html.Div([
        html.H1("Product Insights", style={'textAlign': 'center'}),
        dcc.Graph(id='product-graph'),
        html.Div([
            html.Button('Rating', id='rating-btn', n_clicks=0),
            html.Button('Popularity', id='popularity-btn', n_clicks=0),
            html.Button('Purchase Frequency', id='freq-btn', n_clicks=0),
        ], style={'textAlign': 'center', 'margin': '10px'}),
    ], style={'border': '1px solid black', 'padding': '10px', 'margin': '10px'})

    return product_insights_layout
