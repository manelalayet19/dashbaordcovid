import dash
import dash_bootstrap_components as dbc
#import dash_auth
import random
import os
# bootstrap theme
external_stylesheets = [dbc.themes.QUARTZ]
# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, assets_external_path='assets/style.css',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# define password login  form auth
# USERNAME_PASSWORD_PAIRS=[['username','password']
# auth= dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS) #authentification per person
server = app.server
app.config.suppress_callback_exceptions = True
