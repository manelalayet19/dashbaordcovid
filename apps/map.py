import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
# app = dash.Dash(__name__)
layout = html.Div(
    html.Div([
        html.Iframe(id='map',
                    srcDoc=open('assets/test.html', 'r').read(),
                    ),
    ]),
)

# if __name__ == '__main__':
#     app.run_server(debug=True)
