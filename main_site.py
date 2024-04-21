import pandas as pd
from dash import Dash, html, dcc

# Assuming 'df' is your DataFrame, which you've loaded from your dataset.
dataset_path = "J:/datasets/shopping_trends_updated.csv"
df = pd.read_csv(dataset_path)

# Setup the Dash app.
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Data Summary"),
        dcc.Markdown('''
            **Dataset Overview:**
            This dataset provides a view on customer behavior and purchasing patterns. It covers various customer variables like age, gender, and more.
            
            - **Number of Records:** 3900
            - **Number of Columns:** 18
            
            **Columns:**
            - **Customer ID**: Unique identifier for each customer
            - **Age**: Age of the customer
            - **Gender**: Gender of the customer (Male/Female)
            - **Item Purchased**: The item purchased by the customer
            - **Category**: Category of the item purchased
            - **Purchase Amount (USD)**: The amount of the purchase in USD
            - **Location**: Location where the purchase was made
            - **Size**: Size of the purchased item
            - **Color**: Color of the purchased item
            - **Season**: Season during which the purchase was made
            - **Review Rating**: Rating given by the customer for the purchased item
            - **Subscription Status**: Indicates if the customer has a subscription (Yes/No)
            - **Shipping Type**: Type of shipping chosen by the customer
            - **Discount Applied**: Indicates if a discount was applied to the purchase (Yes/No)
            - **Promo Code Used**: Indicates if a promo code was used for the purchase (Yes/No)
            - **Previous Purchases**: The total count of transactions concluded by the customer at the store, excluding the ongoing transaction
            - **Payment Method**: Customer's most preferred payment method
            - **Frequency of Purchases**: Frequency at which the customer makes purchases (e.g., Weekly, Fortnightly, Monthly)
            '''),
    ], style={'padding': '20px', 'border': '1px solid #ddd', 'margin-bottom': '20px'}),
])

app.run_server(debug=True)