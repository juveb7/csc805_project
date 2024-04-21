# main.py
import pandas as pd
from dash import Dash, html
from modules.data_summary import create_data_summary
from modules.products import setup_product_insights

dataset_path = "J:/datasets/shopping_trends_updated.csv"
df = pd.read_csv(dataset_path)

# Mapping 'Frequency of Purchases' from text to numerical value
frequency_mapping = {
    'Weekly': 52, 'Fortnightly': 26, 'Monthly': 12,
    'Quarterly': 4, 'Annually': 1, 'Bi-Weekly': 24
}
df['Frequency_Num'] = df['Frequency of Purchases'].map(frequency_mapping)

app = Dash(__name__)

# Define the layout of your app
app.layout = html.Div([
    html.H1("CSC 805 Visualization Project: Shopping Trends", style={'textAlign': 'center', }),
    html.Div(create_data_summary(), style={'border': '1px solid black', 'padding': '10px', 'margin': '10px'}),
    setup_product_insights(app, df)
], style={'fontFamily': 'Arial, sans-serif'})

if __name__ == '__main__':
    app.run_server(debug=True)