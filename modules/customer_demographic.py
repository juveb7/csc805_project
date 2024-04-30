import pandas as pd
import plotly.express as px

def create_demographics_figure(df, age_range, selected_genders):
    # Filter the DataFrame based on the selected age range
    filtered_df = df.loc[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
    
    # Further filter by selected genders if 'All' is not selected
    if 'All' not in selected_genders:
        filtered_df = filtered_df.loc[filtered_df['Gender'].isin(selected_genders)]
    
    # Group by 'Age' and (if necessary) 'Gender', then calculate the mean purchase amount
    if 'All' not in selected_genders:
        grouped_df = filtered_df.groupby(['Age', 'Gender'], as_index=False)['Purchase Amount (USD)'].mean()
        fig = px.bar(grouped_df, x='Age', y='Purchase Amount (USD)', color='Gender',
                     title='Average Purchase Amount by Age and Gender',
                     color_discrete_map={'Male': 'blue', 'Female': 'magenta'},  # Assign colors
                     barmode='group')
    else:
        grouped_df = filtered_df.groupby('Age', as_index=False)['Purchase Amount (USD)'].mean()
        fig = px.bar(grouped_df, x='Age', y='Purchase Amount (USD)',
                     title='Average Purchase Amount by Age',
                     barmode='group')
    
    # Customize the layout
    fig.update_layout(
        xaxis_title='Age',
        yaxis_title='Average Purchase Amount (USD)',
        legend_title='Gender',
        hovermode='closest'
    )
    
    # Customize the hover data
    fig.update_traces(
        hoverinfo='y+name',
        marker=dict(line=dict(width=0.5, color='DarkSlateGrey')),
        selector=dict(type='bar')
    )
    
    return fig
