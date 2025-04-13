
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load normalized data
df = pd.read_csv("normalized_diet_data.csv")

# List of environmental metrics
metrics = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut',
    'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]

# Initialize Dash app
app = Dash(__name__)
app.title = "Environmental Impacts by Diet Type"

# App layout
app.layout = html.Div([
    html.H2("Environmental Impacts by Diet Type", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Sex:"),
        dcc.Dropdown(
            options=[{'label': s, 'value': s} for s in df['sex'].unique()],
            id='sex-filter', value=df['sex'].unique()[0]
        ),
        html.Label("Select Age Group:"),
        dcc.Dropdown(
            options=[{'label': a, 'value': a} for a in sorted(df['age_group'].unique())],
            id='age-filter', value=sorted(df['age_group'].unique())[0]
        ),
    ], style={'width': '25%', 'display': 'inline-block', 'padding': 10, 'verticalAlign': 'top'}),

    html.Div([
        dcc.Graph(id='parallel-coordinates-plot')
    ], style={'width': '70%', 'display': 'inline-block'}),
])

# Callback to update graph
@app.callback(
    Output('parallel-coordinates-plot', 'figure'),
    Input('sex-filter', 'value'),
    Input('age-filter', 'value')
)
def update_graph(selected_sex, selected_age):
    filtered_df = df[(df['sex'] == selected_sex) & (df['age_group'] == selected_age)]

    if filtered_df.empty:
        return px.line(title="No data available for this selection.")

    # Convert diet group to numeric codes for coloring
    filtered_df['diet_code'] = filtered_df['diet_group'].astype('category').cat.codes

    fig = px.parallel_coordinates(
        filtered_df,
        dimensions=metrics,
        color='diet_code',
        color_continuous_scale=px.colors.sequential.Viridis,
        labels={col: col.replace("mean_", "").replace("_", " ").title() for col in metrics},
        title=f"Environmental Impact by Diet for {selected_sex.title()}, Age {selected_age}"
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
