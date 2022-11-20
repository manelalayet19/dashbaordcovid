# -*- coding: utf-8 -*-
from dash import get_relative_path
from dash import get_asset_url
from dash_extensions import Lottie
import dash_bootstrap_components as dbc
from dash import dash_table
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
from dash_bootstrap_components._components.DropdownMenuItem import DropdownMenuItem
from dash import Dash
import dash
from app import app
# app = dash.Dash(__name__, external_stylesheets=[
#                 dbc.themes.QUARTZ], assets_external_path='assets')
layout = html.Div(children=[

    html.Div([
        html.Img(src='/assets/17699-covid-19.gif', className="ContactImg"),
        html.H1('Wear a mask Save lives ',
                className='text-center mt-4 mb-2 font-weight-bold'),

    ],         className="ContainerContact"
    ),
    # html.Img(src='/assets/contact-us-faq.gif', className="ContactImg"),
    html.Div([
        dbc.Textarea(className='messageContainer',
                     placeholder="send us a message"),
        html.Div(dbc.Button('submit', type='submit',
                            color='primary', className="btn15 w-100 mt-1 mb-4"))
    ], className="ElementsBtn"),
])
# if __name__ == '__main__':
#     app.run_server(debug=True)
