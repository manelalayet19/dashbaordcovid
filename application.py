# -*- coding: utf-8 -*-
from dash import get_relative_path
from dash import get_asset_url
from apps import app1, app2, landing_page, Home, crimeindicators, signup, login, contact, map
from dash_extensions import Lottie
from app import server
import dash_bootstrap_components as dbc
from dash import dash_table
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
from dash_bootstrap_components._components.DropdownMenuItem import DropdownMenuItem
from dash import Dash
import dash

# import dash_auth
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))

stat = 'https://assets4.lottiefiles.com/private_files/lf30_lyvbczgo.json'
vis = 'https://assets4.lottiefiles.com/private_files/lf30_lZDkKW.json'
application = 'https://assets8.lottiefiles.com/packages/lf20_7pzyukmv.json'
url_covid = 'https://assets5.lottiefiles.com/packages/lf20_xbeapo0i.json'
url_test = 'https://assets5.lottiefiles.com/packages/lf20_4ilboxgz.json'
url_image = 'https://assets5.lottiefiles.com/packages/lf20_wt7bupjp.json'
url_canada = 'https://assets5.lottiefiles.com/packages/lf20_CXxysN.json'
news = 'https://assets9.lottiefiles.com/packages/lf20_glclg2kr.json'
news2 = 'https://assets2.lottiefiles.com/private_files/lf30_4FGi6N.json'
news3 = 'https://assets2.lottiefiles.com/packages/lf20_Fr8Ziv.json'
# --------------------------------------------------------
external_stylesheets = [dbc.themes.QUARTZ]

app = dash.Dash(external_stylesheets=external_stylesheets)

# app layout
nav_item = dbc.Nav(
    [dbc.NavItem(dbc.NavLink("Home", href="/apps/Home")),
     dbc.NavItem(dbc.NavLink("Data", href="#")),
     dbc.NavItem(dbc.NavLink("Persons with disabilities", href="#")),
     dbc.NavItem(dbc.NavLink("Health inscription", href="#")),
     dbc.NavItem(dbc.NavLink(
         "Vaccine", href="https://www.canada.ca/en/health-canada/services/drugs-health-products/covid19-industry/drugs-vaccines-treatments/vaccines.html")),
     dbc.NavItem(dbc.NavLink("Map", href="/apps/map")),
     dbc.NavItem(dbc.NavLink("Contact", href="/apps/contact")),
     dbc.NavItem(dbc.NavLink("login", href="/apps/login")),
     dbc.NavItem(dbc.NavLink("sign up", href="/apps/signup")),
     ]
)
# make a reuseable dropdown for the different examples https://github.com/facultyai/dash-bootstrap-components/blob/main/examples/multi-page-apps/navbar.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(dbc.NavLink("page 1", href="/apps/landing_page")),
        dbc.DropdownMenuItem(dbc.NavLink(
            "general data ", href="/apps/crimeindicators")),
        dbc.DropdownMenuItem(dbc.NavLink("page 2", href="/apps/app2")),
        dbc.DropdownMenuItem(dbc.NavLink("page 3", href="/apps/app1")),
        dbc.DropdownMenuItem(dbc.NavLink("Home", href="/apps/Home")),
    ],
    nav=True,
    in_navbar=True,
    label="Next",
)
# this is the default navbar style created by the NavbarSimple component
default = dbc.NavbarSimple(
    children=[nav_item, dropdown],
    brand="COVID-19 Dashboard",
    brand_href=app.get_asset_url("assets/favicon.ico"),
    sticky="top",
    className="mb-5",
    color="dark",
    dark=True,
)
app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    default,

    html.Div(id='page-content', children=[]),

    # ---------------------------------------------------Footer-------------------------------------
    html.Footer(children=[
        html.P(
            '@copyright2022', className=''),
        html.A(' Author Github', href='https://github.com/manelalayet19',
               target='_blank', className=''),
        html.A([
            html.Img(
                src=app.get_asset_url("universite_de_sherbrooke_logo.png"),
                # style={'height':'4%','width':'8%','float':'right','position':'relative','padding-top':'20px','padding-right':0}
            )], href="https://www.usherbrooke.ca/geomatique/", target='_blank'),
    ], className="bg-dark"),
], fluid=True)


@ app.callback(Output(component_id='page-content', component_property='children'),
               [Input(component_id='url', component_property='pathname')])
def display_page_url(pathname):
    if pathname == '/apps/crimeindicators':
        return crimeindicators.layout
    elif pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/login':
        return login.layout
    elif pathname == '/apps/landing_page':
        return landing_page.layout
    elif pathname == '/apps/Home':
        return Home.layout
    elif pathname == '/apps/signup':
        return signup.layout
    elif pathname == '/apps/map':
        map.layout
    elif pathname == '/apps/contact':
        return contact.layout
    else:
        return '404 page not found'


if __name__ == '__main__':
    app.run_server(debug=True)
