import pandas as pd
from collections import Counter
import plotly.graph_objects as go

data = pd.read_csv('pivoted_data2.csv')

initial_column = 'Count Backpack'
count_columns  = [col for col in data.columns if 'Count' in col]

# Define a function to create hover text based on the item
def create_hover_text(df, item):
    return (df['Location'] + '<br>' +
            'Average Age of Customers: ' + df[f'Average_Age {item}'].map(lambda x: f"{x:.2f}") + '<br>' +
            'Most Common Color: ' + df[f'Most_Common_Color {item}'] + '<br>' +
            'Most Common Size: ' + df[f'Most_Common_Size {item}'] + '<br>' +
            'Total Amount (USD): ' + df[f'Total_Amount {item}'].map(lambda x: f"{x:.2f}"))

data['text'] = create_hover_text(data, 'Backpack')

fig = go.Figure(data=go.Choropleth(
    locations=data['Code'], # Spatial coordinates
    z = data[initial_column].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'reds',
    text=data['text'], # hover text
    colorbar_title = "Count",
))

# Update the layout to add a title and limit the map scope to the USA
fig.update_layout(
    title_text='Purchased Items',
    geo_scope='usa',  # limit map scope to USA
)

# Add dropdowns
buttons = []

# Generate dropdown buttons dynamically based on items
items = sorted(set(col.split(' ')[-1] for col in data.columns if ' ' in col))
buttons = []
for item in items:
    buttons.append(dict(
        method='update',
        label=item,
        args=[{'z': [data[f'Count {item}'].astype(float)],
               'text': [create_hover_text(data, item)]},
              {'choropleth': {'colorbar': {'title': f'Count {item}'}},
               'title_text': 'Purchased Items - ' + item}]
    ))
# Include buttons in the layout
fig.update_layout(
    updatemenus=[dict(
        x=0.1,
        xanchor='left',
        y=1.065,
        yanchor='top',
        buttons=buttons,
        showactive=True
    )]
)

# Show the figure
fig.show()