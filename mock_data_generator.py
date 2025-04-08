import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies
import plotly.express as px
'''
# Lees de CSV
df = pd.read_csv('exclusieve_schoenen_verkoop_met_locatie.csv')

# Zorg ervoor dat de datumkolom als datetime wordt gelezen
df['datum'] = pd.to_datetime(df['datum'])

# Voeg een kolom toe voor de maand en het jaar
df['maand'] = df['datum'].dt.to_period('M')

# Initialiseer de Dash-app
app = dash.Dash(__name__)

# Layout van de app
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Verkoop per maand', children=[
            dcc.Graph(id='verkoop-per-maand')
        ]),
        dcc.Tab(label='Verkoop per land', children=[
            dcc.Graph(id='verkoop-per-land')
        ])
    ])
])

# Callback voor de eerste visualisatie (verkoop per maand)
@app.callback(
    Output('verkoop-per-maand', 'figure'),
    Input('verkoop-per-maand', 'id')
)
def update_verkoop_per_maand(_):
    verkoop_per_maand = df.groupby('maand').size().reset_index(name='aantal')
    fig = px.line(verkoop_per_maand, x='maand', y='aantal', title='Verkoop per maand')
    return fig

# Callback voor de tweede visualisatie (verkoop per land)
@app.callback(
    Output('verkoop-per-land', 'figure'),
    Input('verkoop-per-land', 'id')
)
def update_verkoop_per_land(_):
    verkoop_per_land = df['land'].value_counts().reset_index()
    verkoop_per_land.columns = ['land', 'aantal']
    fig = px.bar(verkoop_per_land, x='land', y='aantal', title='Verkoop per land')
    return fig

# Run de app
if __name__ == '__main__':
    app.run_server(debug=True)
'''
