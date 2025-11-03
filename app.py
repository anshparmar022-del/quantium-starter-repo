import dash
from dash import dcc, html
import pandas as pd
from datetime import datetime

# Load the processed data
df = pd.read_csv("formatted_output.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date (important for line chart)
df = df.sort_values("date")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Over Time",
        style={"textAlign": "center", "color": "#B03060", "marginBottom": "20px"}
    ),
    
    html.P(
        "Visualising sales trends before and after the price increase on January 15, 2021.",
        style={"textAlign": "center"}
    ),
    
    dcc.Graph(
        id="sales-line-chart",
        figure={
            "data": [
                {
                    "x": df["date"],
                    "y": df["sales"],
                    "type": "line",
                    "name": "Sales",
                    "line": {"color": "#FF69B4"}
                }
            ],
            "layout": {
                "title": "Pink Morsel Daily Sales",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Sales ($)"},
                # Add a vertical line for Jan 15, 2021
                "shapes": [
                    {
                        "type": "line",
                        "x0": "2021-01-15",
                        "x1": "2021-01-15",
                        "y0": 0,
                        "y1": max(df["sales"]),
                        "line": {
                            "color": "red",
                            "width": 2,
                            "dash": "dash",
                        },
                    }
                ],
                "annotations": [
                    {
                        "x": datetime(2021, 1, 15),
                        "y": max(df["sales"]),
                        "text": "Price Increase",
                        "showarrow": True,
                        "arrowhead": 2,
                        "ax": 0,
                        "ay": -40
                    }
                ]
            },
        },
    ),
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

