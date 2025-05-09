# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Read the airline data into the pandas dataframe
airline_data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
    encoding="ISO-8859-1",
    dtype={'Div1Airport': str, 'Div1TailNum': str,
           'Div2Airport': str, 'Div2TailNum': str})

# Create a dash application
app = dash.Dash(__name__)

# Layout of the application
app.layout = html.Div([
    html.H1("Airline Performance Dashboard", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='input-year',
        options=[
            {'label': str(year), 'value': year} for year in airline_data['Year'].unique()
        ],
        placeholder="Select a year",
        style={'width': '50%'}
    ),
    dcc.Graph(id='line-plot'),
    dcc.Graph(id='bar-plot')  # New graph for bar chart
])

# Callback to update line graph based on dropdown selection
@app.callback(
    Output(component_id='line-plot', component_property='figure'),
    Input(component_id='input-year', component_property='value')
)
def update_line_graph(selected_year):
    if selected_year is None:
        return go.Figure()

    filtered_data = airline_data[airline_data['Year'] == selected_year]
    fig = go.Figure(data=go.Scatter(
        x=filtered_data['Month'],
        y=filtered_data['Flights'],
        mode='lines+markers'
    ))
    fig.update_layout(
        title=f"Monthly Flights in {selected_year}",
        xaxis_title="Month",
        yaxis_title="Number of Flights"
    )
    return fig

# Callback to update bar graph based on dropdown selection
@app.callback(
    Output(component_id='bar-plot', component_property='figure'),
    Input(component_id='input-year', component_property='value')
)
def update_bar_graph(selected_year):
    if selected_year is None:
        return go.Figure()

    filtered_data = airline_data[airline_data['Year'] == selected_year]
    avg_delays = filtered_data.groupby('Reporting_Airline')['ArrDelay'].mean().reset_index()
    avg_delays = avg_delays.dropna()  # Remove rows with NaN values

    fig = go.Figure(data=go.Bar(
        x=avg_delays['Reporting_Airline'],
        y=avg_delays['ArrDelay'],
        text=avg_delays['ArrDelay'],
        textposition='auto'
    ))
    fig.update_layout(
        title=f"Average Arrival Delays by Airline in {selected_year}",
        xaxis_title="Airline",
        yaxis_title="Average Arrival Delay (minutes)"
    )
    return fig

# Run the application
if __name__ == '__main__':
    app.run(debug=True)