import dash
from dash import Dash
from dash_bootstrap_components._components.DropdownMenuItem import DropdownMenuItem
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
# import dash_auth
from dash import dash_table
import dash_bootstrap_components as dbc
from dash_extensions import Lottie
from app import app
from dash import get_asset_url
from dash import get_relative_path
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
# ----------------------------------------------Body ----------------------------------------

# app = dash.Dash(external_stylesheets=[
#                 dbc.themes.SOLAR],)
layout = html.Div([
    dbc.Container([

        dbc.Row([
            dbc.Col(html.H1('The real impact of Covid-19'),
                    className='mt-4 m-b-4')
        ]),
        dbc.Row([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": app.get_asset_url('1.jpg')},
                    {"key": "2", "src": app.get_asset_url('2.jpg')},
                    {"key": "3", "src": app.get_asset_url('3.jpg')},
                ],
                controls=True,
                indicators=True,
                className=''
            ),
        ]),
        dbc.Row([
            dbc.Col([html.H1('Prevention measures'), html.Hr()]),
        ]),
        dbc.Row([
            html.Div([
                html.Img(
                    src=app.get_asset_url('64753-covid-icon-use-a-mask.gif'), id='MesuresImg1'),
                html.Img(src=app.get_asset_url(
                    '64455-covid-icon-dont-touch-face.gif'), id='MesuresImg2'),
                html.Img(src=app.get_asset_url(
                    '64311-covid-icon-avoid-handshakes.gif'), id='MesuresImg3'),
            ], className='Mesures'),
            html.Div([
                html.Img(src=app.get_asset_url(
                    '64195-covid-icon-avoid-crowd-places.gif'), id='MesuresImg4'),
                html.Img(src=app.get_asset_url(
                    '64153-covid-icon-avoid-contacts.gif'), id='MesuresImg5'),
                html.Img(src=app.get_asset_url(
                    '34954-covid-19-distance.gif'), id='MesuresImg6'),
            ], className='Mesures'),
            html.Div([
                html.Img(src=app.get_asset_url(
                    '64371-covid-icon-avoid-travelling.gif'), id='MesuresImg'),
                html.Img(src=app.get_asset_url(
                    '64837-covid-icon-use-hand-sanitizer.gif'), id='MesuresImg8'),
                html.Img(src=app.get_asset_url(
                    '64592-covid-icon-stay-at-home.gif'), id='MesuresImg7'),

            ], className='Mesures'),

            dbc.Row([
                dbc.Col([html.H1('Symptoms'),
                         html.Hr()]),
                html.Div([
                    html.Img(src=app.get_asset_url(
                        '68203-covid-icon-sore-throat.gif')),
                    html.Img(src=app.get_asset_url(
                        '66245-covid-icon-shortness-of-breath.gif')),
                    html.Img(src=app.get_asset_url(
                        '65783-covid-icon-pneumonia.gif')),

                ], className='Mesures'),
                html.Div([
                    html.Img(src=app.get_asset_url(
                        '65725-covid-icon-hemoptysis.gif')),
                    html.Img(src=app.get_asset_url(
                        '65667-covid-icon-headache.gif')),
                    html.Img(src=app.get_asset_url(
                        '65627-covid-icon-fever.gif')),

                ], className='Mesures'),
                html.Div([
                    html.Img(src=app.get_asset_url(
                        '65357-covid-icon-fatigue.gif')),
                    html.Img(src=app.get_asset_url(
                        '65231-covid-icon-dry-cough.gif')),
                    html.Img(src=app.get_asset_url(
                        '65079-covid-icon-diarrhea.gif')),

                ], className='Mesures'),
            ]),


        ]),

        # ----------------------description section --------------------------------
        dbc.Row([
            dbc.Col([html.H1('Description'),
                     html.Hr()
                     ]),
            dbc.Col(dcc.Markdown('''
        COVID-19 continues to impact Canadians, with approximately 132,000 hospitalizations and over 35,000 deaths to date.
        Canadians continue to respond—over 30 million people are fully vaccinated. Despite these efforts, the spread of Omicron means Canadians continue to live with COVID-19, but perhaps in a different way, as restrictions begin to lift across the country.
        To mark the second year of the pandemic, Statistics Canada is reviewing the major social and economic impacts on the lives of Canadians and on Canadian businesses, and highlighting potential longer-term structural changes moving forward. This review builds on previous efforts to track impacts throughout the pandemic, including COVID-19 in Canada:
         A Year-end Update on Social and Economic Impacts, released in December 2021; COVID-19 in Canada: A One-year Update on Social and Economic Impacts, released to mark the first year of the pandemic; and The Social and Economic Impacts of COVID-19: A Six-month Update.
                Keeping up to date with COVID-19 vaccines continues to be one of the most effective ways to protect against severe illness, hospitalization, and death from COVID-19.
                First Nations, Inuit and Métis across the country have access to vaccines through vaccine clinics and health centres.
                [statistique Canada]('https://www150.statcan.gc.ca/n1/pub/11-631-x/11-631-x2022001-eng.htm')
                '''))

        ]),
        dbc.Row([
            dbc.Col([html.H1('Activity'),
                     html.Hr()]),
        ]),
        dbc.Row([
            dbc.Card([
                dbc.CardHeader(
                    Lottie(options=options, width="32%", height="32%", url=stat)),
                dbc.CardBody([
                    html.P('SOMETHING HERE ', className='p'),
                ], style={
                    'textAlign': 'center',
                    'borderRadius': '100px',
                    'size': '12px'
                })
            ], color="secondary", inverse=True),
            dbc.Card([
                dbc.CardHeader(
                    Lottie(options=options, width="32%", height="32%", url=vis)),
                dbc.CardBody([
                    html.P('SOMETHING HERE ', className='p'),
                ], style={
                    'textAlign': 'center',
                    'borderRadius': '100px',
                    'size': '12px'
                })
            ], color="info", inverse=True),
            dbc.Card([
                dbc.CardHeader(
                    Lottie(options=options, width="32%", height="32%", url=application)),
                dbc.CardBody([
                    html.P('SOMETHING HERE ', className='p'),
                ], style={
                    'textAlign': 'center',
                    'borderRadius': '100px',
                    'size': '12px'
                })
            ], color="primary", inverse=True),

        ], className='RowActivity'),
        dbc.Row([
            dbc.Col([html.H1('Latest News '), html.Hr()]),
        ]),
        dbc.Row([
            dbc.Card([dbc.CardHeader(
                Lottie(options=options, width="32%", height="32%", url=news)),
                dbc.CardBody([
                    html.P('COVID-19 Announcements ', className='p'),
                    html.Button([
                        html.A(
                            'Read More ', href='https://www.canada.ca/en/news/COVID-19-announcements.html'),
                    ], className='BtnNews'),
                ], style={
                    'textAlign': 'center',
                    'borderRadius': '100%',
                    'size': '12px'
                }),
            ], color="primary", inverse=True),
            dbc.Card([dbc.CardHeader(
                Lottie(options=options, width="32%", height="32%", url=news2)),
                dbc.CardBody([
                    html.P('COVID-19: Outbreak update ', className='p'),
                    html.Button([
                        html.A(
                            'Read More ', href='https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html'),
                    ], className='BtnNews'),
                ], style={
                    'textAlign': 'center',
                    'borderRadius': '100%',
                    'size': '12px'
                }),
            ], color="danger", inverse=True, className='CardNews1'),
            dbc.Card([dbc.CardHeader(
                Lottie(options=options, width="32%", height="32%", url=news3)),
                dbc.CardBody([
                    html.P('Info Base', className='p'),
                    html.Button([
                        html.A(
                            'Read More ', href='https://health-infobase.canada.ca/covid-19/'),
                    ], className='BtnNews'),
                ], style={
                    'textAlign': 'center',
                    'borderRadius': '100%',
                    'size': '12px'
                }),
            ], color="Warning", inverse=True, className='CardNews3'),
        ], className='RowNews'),




    ]),
])
# if __name__ == '__main__':
#     app.run_server(debug=True)
