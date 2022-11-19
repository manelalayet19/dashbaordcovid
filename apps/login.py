import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import dash_leaflet as dl
import dash_extensions
from dash_extensions import Lottie
import plotly.express as px
from dash import Output, Input
import datetime
from datetime import date
from app import app
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
layout = html.Div(
    children=[

        html.H1('Log in', className='mt-5 mb-2 text-center font-weight-bold'),
        dbc.Row([
            dbc.Col([
                dbc.Label("Email"),
                dbc.Input(
                    type="email",
                    id="email-input",
                    placeholder="Enter email",
                    value=''
                ),
                dbc.FormFeedback(
                    "That looks like a gmail address :-)", type="valid"),
                dbc.FormFeedback(
                    "Sorry, we only accept gmail for some reason...",
                    type="invalid",),
            ], width={'size': 9, 'offset': 2, 'order': 1}, className='mt-2 p-2'),
            dbc.Col([
                dbc.Label("Password", html_for="example-password-grid"),
                dbc.Input(
                    type="password",
                    id="example-password-grid",
                    placeholder="Enter password",
                    value=''
                ),
            ], width={'size': 9, 'offset': 2, 'order': 2}),

        ]),
        dbc.Row([
            dbc.Col([
                dbc.Switch(
                    id='switcher', value=False, label='Remember me 😁 '),
            ], width={'offset': 2, 'size': 9, 'order': 1}, className='d-flex')

        ], className='mt-2 mb-2 ml-2'),
        dbc.Row([
            dbc.Col(dbc.Button("Log in", color="primary"),
                width={'offset': 2, 'size': 9, 'order': 1}, className='d-grid gap-2')

        ]),

    ])
# if __name__ == '__main__':
#     app.run_server(debug=True)
