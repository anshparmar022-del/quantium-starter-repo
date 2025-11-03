import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv('data/processed_data.csv')

# Ensure correct column casing
df.columns = df.columns.str.lower()

# Create the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1(
        "Soul Foods — Pink Morsel Sales Dashboard",
        style={"textAlign": "center", "color": "#e91e63", "marginBottom": "30px"}
    ),

    html.Div([
        html.Label("Filter by Region:", style={"fontWeight": "bold", "fontSize": "18px"}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '15px', 'fontSize': '16px'}
        )
    ], style={"textAlign": "center", "marginBottom": "40px"}),

    html.Div([
        dcc.Graph(id='sales-line-chart')
    ], style={
        "backgroundColor": "#ffffff",
        "boxShadow": "0 4px 8px rgba(0,0,0,0.1)",
        "borderRadius": "10px",
        "padding": "20px",
        "width": "90%",
        "margin": "0 auto"
    })
], style={"fontFamily": "Arial, sans-serif", "backgroundColor": "#fff8f9", "padding": "30px"})


# Callback for interactive chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color='region',
        title='Pink Morsel Sales Over Time',
        labels={'sales': 'Total Sales', 'date': 'Date'}
    )

    fig.update_layout(
        title_x=0.5,
        plot_bgcolor="#fce4ec",
        paper_bgcolor="#fce4ec",
        font=dict(color="#880e4f"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.3)')
    )

    return fig


# Run the Dash app
if __name__ == "__main__":
    app.run(debug=True)
