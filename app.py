import dash
import dash_bootstrap_components as dbc
#import dash_auth
import random
import flask
from flask import send_from_directory
import os
Fontawesome = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
# bootstrap theme
external_stylesheets = [dbc.themes.QUARTZ, dbc.icons.FONT_AWESOME, Fontawesome]
# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, assets_external_path='assets',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


# @app.server.route('/assests/<path:path>')
# def static_file(path):
#     static_folder = os.path.join(os.getcwd(), 'assests')
#     return send_from_directory(static_folder, path)
