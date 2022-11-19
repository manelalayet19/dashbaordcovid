import dash
from dash import Dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
from dash import dash_table
import dash_bootstrap_components as dbc
from dash_extensions import Lottie
from app import app
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))

layout = html.Div([
    dbc.Container([
        # # ----------------------------------------------Body ----------------------------------------
        # dbc.Row([
        #         dbc.Col(html.H1('The real impact of Covid-19'),
        #                 className='mt-4 m-b-4')
        #         ]),

        # dbc.Row([
        #     dbc.Carousel(
        #         items=[
        #             {"key": "1", "src": app.get_asset_url('1.jpg')},
        #             {"key": "2", "src": app.get_asset_url('2.jpg')},
        #             {"key": "3", "src": app.get_asset_url('3.jpg')},
        #         ],
        #         controls=True,
        #         indicators=True,
        #         className=''
        #     ),
        # ]),
        # dbc.Row([
        #         dbc.Col([html.H1('Activity'),
        #                  html.Hr()]),
        #         ]),
        # dbc.Row([
        #     dbc.Card([
        #         dbc.CardHeader(
        #             Lottie(options=options, width="32%", height="32%", url=stat)),
        #         dbc.CardBody([
        #             html.P('SOMETHING HERE ', className='p'),
        #         ], style={
        #             'textAlign': 'center',
        #             'borderRadius': '100px',
        #             'size': '12px'
        #         })
        #     ], color="secondary", inverse=True),
        #     dbc.Card([
        #         dbc.CardHeader(
        #             Lottie(options=options, width="32%", height="32%", url=vis)),
        #         dbc.CardBody([
        #             html.P('SOMETHING HERE ', className='p'),
        #         ], style={
        #             'textAlign': 'center',
        #             'borderRadius': '100px',
        #             'size': '12px'
        #         })
        #     ], color="info", inverse=True),
        #     dbc.Card([
        #         dbc.CardHeader(
        #             Lottie(options=options, width="32%", height="32%", url=application)),
        #         dbc.CardBody([
        #             html.P('SOMETHING HERE ', className='p'),
        #         ], style={
        #             'textAlign': 'center',
        #             'borderRadius': '100px',
        #             'size': '12px'
        #         })
        #     ], color="primary", inverse=True),

        # ], className='RowActivity'),
        # dbc.Row([
        #     dbc.Col([html.H1('Latest News '), html.Hr()]),
        # ]),
        # dbc.Row([
        #         dbc.Card([dbc.CardHeader(
        #             Lottie(options=options, width="32%", height="32%", url=news)),
        #             dbc.CardBody([
        #                 html.P('COVID-19 Announcements ', className='p'),
        #                 html.Button([
        #                     html.A(
        #                         'Read More ', href='https://www.canada.ca/en/news/COVID-19-announcements.html'),
        #                 ], className='BtnNews'),
        #             ], style={
        #                 'textAlign': 'center',
        #                 'borderRadius': '100%',
        #                 'size': '12px'
        #             }),
        #         ], color="primary", inverse=True),
        #         dbc.Card([dbc.CardHeader(
        #             Lottie(options=options, width="32%", height="32%", url=news2)),
        #             dbc.CardBody([
        #                 html.P('COVID-19: Outbreak update ', className='p'),
        #                 html.Button([
        #                     html.A(
        #                         'Read More ', href='https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html'),
        #                 ], className='BtnNews'),
        #             ], style={
        #                 'textAlign': 'center',
        #                 'borderRadius': '100%',
        #                 'size': '12px'
        #             }),
        #         ], color="danger", inverse=True, className='CardNews1'),
        #         dbc.Card([dbc.CardHeader(
        #             Lottie(options=options, width="32%", height="32%", url=news3)),
        #             dbc.CardBody([
        #                 html.P('Info Base', className='p'),
        #                 html.Button([
        #                     html.A(
        #                         'Read More ', href='https://health-infobase.canada.ca/covid-19/'),
        #                 ], className='BtnNews'),
        #             ], style={
        #                 'textAlign': 'center',
        #                 'borderRadius': '100%',
        #                 'size': '12px'
        #             }),
        #         ], color="Warning", inverse=True, className='CardNews3'),
        #         ], className='RowNews'),
        # dbc.Row([
        #     dbc.Col([html.H1('Prevention measures'), html.Hr()]),
        # ]),
        # dbc.Row([
        #         html.Div([
        #             html.Img(
        #                 src=app.get_asset_url('64753-covid-icon-use-a-mask.gif'), id='MesuresImg1'),
        #             html.Img(src=app.get_asset_url(
        #                 '64455-covid-icon-dont-touch-face.gif'), id='MesuresImg2'),
        #             html.Img(src=app.get_asset_url(
        #                 '64311-covid-icon-avoid-handshakes.gif'), id='MesuresImg3'),
        #         ], className='Mesures'),
        #         html.Div([
        #             html.Img(src=app.get_asset_url(
        #                 '64195-covid-icon-avoid-crowd-places.gif'), id='MesuresImg4'),
        #             html.Img(src=app.get_asset_url(
        #                 '64153-covid-icon-avoid-contacts.gif'), id='MesuresImg5'),
        #             html.Img(src=app.get_asset_url(
        #                 '34954-covid-19-distance.gif'), id='MesuresImg6'),
        #         ], className='Mesures'),
        #         html.Div([
        #             html.Img(src=app.get_asset_url(
        #                 '64371-covid-icon-avoid-travelling.gif'), id='MesuresImg'),
        #             html.Img(src=app.get_asset_url(
        #                 '64837-covid-icon-use-hand-sanitizer.gif'), id='MesuresImg8'),
        #             html.Img(src=app.get_asset_url(
        #                 '64592-covid-icon-stay-at-home.gif'), id='MesuresImg7'),

        #         ], className='Mesures'),

        #         dbc.Row([
        #             dbc.Col([html.H1('Symptoms'),
        #                      html.Hr()]),
        #             html.Div([
        #                 html.Img(src=app.get_asset_url(
        #                     '68203-covid-icon-sore-throat.gif')),
        #                 html.Img(src=app.get_asset_url(
        #                     '66245-covid-icon-shortness-of-breath.gif')),
        #                 html.Img(src=app.get_asset_url(
        #                     '65783-covid-icon-pneumonia.gif')),

        #             ], className='Mesures'),
        #             html.Div([
        #                 html.Img(src=app.get_asset_url(
        #                     '65725-covid-icon-hemoptysis.gif')),
        #                 html.Img(src=app.get_asset_url(
        #                     '65667-covid-icon-headache.gif')),
        #                 html.Img(src=app.get_asset_url(
        #                     '65627-covid-icon-fever.gif')),

        #             ], className='Mesures'),
        #             html.Div([
        #                 html.Img(src=app.get_asset_url(
        #                     '65357-covid-icon-fatigue.gif')),
        #                 html.Img(src=app.get_asset_url(
        #                     '65231-covid-icon-dry-cough.gif')),
        #                 html.Img(src=app.get_asset_url(
        #                     '65079-covid-icon-diarrhea.gif')),

        #             ], className='Mesures'),
        #         ]),


        #         ]),
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
    ]),
]),
