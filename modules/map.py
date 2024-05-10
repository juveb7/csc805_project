import pandas as pd
from collections import Counter
import plotly.graph_objects as go

def map_figure():
 # Load data
    data = pd.read_csv('./dataset/pivoted_data2.csv')
    
    # Define a function to create hover text based on the item
    def create_hover_text(df, item):
        return (df['Location'] + '<br>' +
                'Average Age of Customers: ' + df[f'Average_Age {item}'].map(lambda x: f"{x:.2f}") + '<br>' +
                'Most Common Color: ' + df[f'Most_Common_Color {item}'] + '<br>' +
                'Most Common Size: ' + df[f'Most_Common_Size {item}'] + '<br>' +
                'Total Amount (USD): ' + df[f'Total_Amount {item}'].map(lambda x: f"{x:.2f}"))

    # Use the function to create hover text for the initial column
    data['text'] = create_hover_text(data, 'Backpack')
    
    # Create the choropleth map
    fig = go.Figure(data=go.Choropleth(
        locations=data['Code'],
        z=data['Count Backpack'].astype(float),
        locationmode='USA-states',
        colorscale='reds',
        text=data['text'],
        colorbar_title="Count",
    ))
    
    # Update the layout to add a title and limit the map scope to the USA
    fig.update_layout(
        #title_text='Purchased Items',
        geo_scope='usa',
    )

    # Generate dropdown buttons dynamically based on items
    items = sorted(set(col.split(' ')[-1] for col in data.columns if 'Count ' in col))
    buttons = []
    for item in items:
        buttons.append(dict(
            method='update',
            label=item,
            args=[{'z': [data[f'Count {item}'].astype(float)],
                   'text': [create_hover_text(data, item)]},
                  {'choropleth': {'colorbar': {'title': f'Count {item}'}}, 'title_text': 'Purchased Items - ' + item}]
        ))

    # Include buttons in the layout
    fig.update_layout(
        updatemenus=[dict(
            x=0.005,
            xanchor='left',
            y=1,
            yanchor='top',
            buttons=buttons,
            showactive=True
        )]
    )

    return fig
