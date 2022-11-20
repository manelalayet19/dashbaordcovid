# -*- coding: utf-8 -*-
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
import os
from app import app
# Fontawesome = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))
gmail = 'https://assets3.lottiefiles.com/packages/lf20_tszzqucf.json'
github = 'https://assets9.lottiefiles.com/packages/lf20_6HFXXE.json'
facebook = 'https://assets7.lottiefiles.com/packages/lf20_bgHQHE.json'
login = 'https://assets2.lottiefiles.com/packages/lf20_1vcsnju7.json'
# app = dash.Dash(__name__, external_stylesheets=[
#                 dbc.themes.QUARTZ, Fontawesome])

layout = html.Div([
    # -----------------------------Logo image ---------------------
    dcc.Location(id='url', refresh=False),
    html.Link(
        rel='stylesheet',
        href='/assets/file1.css'
    ),

    html.H1('Sign up', className='text-center font-weight-bold mt-5'),

    # --------------------------Form ---------------------------------
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
                type="invalid"),
        ], width={'size': 9, 'offset': 2, 'order': 1}, className='mt-2'),
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
    # dbc.Row([
    #     dbc.Col([
    #         dcc.DatePickerRange(
    #             id='date-picker-range',
    #             min_date_allowed=date(1900, 1, 1),
    #             max_date_allowed=date(2027, 1, 1),
    #             end_date=date(2027, 12, 31),
    #             initial_visible_month=date(2022, 11, 18),
    #             show_outside_days=True,
    #             day_size=32,
    #             display_format='DD/MM/YYYY',
    #             clearable=True,
    #             style={'zIndex': 10}
    #         ),    html.Div(id='output-container-date-picker-range')

    #     ], width={'offset': 2, 'size': 3, 'order': 1}, className=' mt-2 ml-4'),
    # ]),
    dbc.Row([
        dbc.Col([
            dbc.Label(id='Phone'),
            dbc.Input(type='tel', id='phone',
                      placeholder="Enter Phone number", pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}")
        ], width={'offset': 2, 'size': 9, 'order': 1}),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Switch(
                id='switcher', value=False),
            html.A(href='#', target='_blank'),
            dbc.Label('read the terms and agree to them 😁 ',
                      html_for='switcher'),

        ], width={'offset': 2, 'size': 9, 'order': 1}, className='d-flex')

    ], className='mt-2 mb-2 ml-2'),
    dbc.Row([
        dbc.Col(dbc.Button("Sign up", color="primary"),
                width={'offset': 2, 'size': 9, 'order': 1}, className='d-grid gap-2')

    ]),
    # -----------------three images -------------------------------
    html.Div([
        html.I(className="fab fa-facebook"),
        html.I(className="fab fa-github "),
        html.I(className="fab fa-google"),

    ], className="logos"),
])


@app.callback(
    [Output("email-input", "valid"), Output("email-input",
                                            "invalid")],
    [Input('email-input', 'value')],


)
def emailChecker(mail):
    if mail:
        gmail = Input.endwith('@gmail.com')
        return gmail, not gmail
        return False, False


# if __name__ == '__main__':
#     app.run_server(debug=True)
