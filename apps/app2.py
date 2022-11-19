import dash
import plotly
import plotly.express as px
import pandas as pd
import geojson
from dash import html, dcc, Input, Output
import dash_leaflet as dl
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
from app import app
from dash_extensions import Lottie
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# ---------------------------------APP render -----------------------
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
# ---------------------------------------Lottie design -------------------
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))
url_covid = 'https://assets5.lottiefiles.com/packages/lf20_xbeapo0i.json'
url_test = 'https://assets5.lottiefiles.com/packages/lf20_4ilboxgz.json'
url_image = 'https://assets5.lottiefiles.com/packages/lf20_wt7bupjp.json'
url_canada = 'https://assets5.lottiefiles.com/packages/lf20_CXxysN.json'

# --------------------------------------------------------read csv files ------------------------------------------------
df = pd.read_csv('assets/mapping/data_prices.csv', delimiter=';')
df["Date"] = pd.to_datetime(df["Date"])
# print(df)
# print(df.dtypes)
df['month_year'] = df['Date'].dt.strftime('%b-%Y')
# print(df)
# --------------------------------------------------plotly graph objects --------------------------------------------------------
fig = make_subplots(
    rows=4,
    cols=3,
    column_widths=[0.5, 0.5, 0.8],
    print_grid=False,
    shared_xaxes=True,
    shared_yaxes=False,
    x_title='Date',
    y_title='value',
    subplot_titles=("Food", "Transportation", "Clothing and footwear", "Household and equipments",
                    "Gasoline", "Health and personal care",
                    "Recreation education and reading", "Shelter", "Health and personal care",
                    "Alcoholic,tobacco products and cannabis",
                    "All-items excluding food and energy", "All-items excluding energy", "Energy", "Goods", "Services"))
fig.update_xaxes(tickformat="%b\n%Y"),
fig.add_trace(go.Bar(x=df['month_year'], y=df.Food),
              row=1, col=1)

fig.add_trace(go.Bar(x=df['month_year'], y=df.Transportation),
              row=1, col=2)

fig.add_trace(go.Bar(x=df['month_year'], y=df['Clothing and footwear']),
              row=1, col=3)

fig.add_trace(go.Bar(x=df['month_year'], y=df['Household operations  furnishings and equipment']),
              row=2, col=1)

fig.add_trace(go.Bar(x=df['month_year'], y=df['Shelter']),
              row=2, col=2)

fig.add_trace(go.Bar(x=df['month_year'], y=df['Health and personal care']),
              row=2, col=3)
fig.add_trace(go.Bar(x=df['month_year'], y=df['Alcoholic beverages  tobacco products and recreational cannabis']),
              row=3, col=1)
fig.add_trace(go.Bar(x=df['month_year'], y=df['All-items excluding food and energy']),
              row=3, col=2)
fig.add_trace(go.Bar(x=df['month_year'], y=df['All-items excluding energy']),
              row=3, col=3)
fig.add_trace(go.Bar(x=df['month_year'], y=df['Energy']),
              row=4, col=1)
fig.add_trace(go.Bar(x=df['month_year'], y=df['Goods']),
              row=4, col=2)
fig.add_trace(go.Bar(x=df['month_year'], y=df['Services']),
              row=4, col=3)
fig.update_layout(
    showlegend=False,
    # height=750, width=750,
    title_text=" prices",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)', template='simple_white')

# ----------------------------------------------Layout section ---------------------------------------------------
layout = html.Div([
    dbc.Container([
        # cette partie pour les indices globaux. décés , genre, age, etc.
        # dbc.Row([
        #     dbc.Col([
        #         dbc.Card([
        #             dbc.CardHeader(
        #                 Lottie(options=options, width="32%", height="32%", url=url_covid)),
        #             dbc.CardBody([
        #                 html.H4('Total tests performed'),
        #                 html.H6("65,873,060"),
        #                 html.H6('statcan,2022')
        #             ], style={
        #                 'textAlign': 'center',
        #                 'borderRadius': '100px',
        #                 'size': '12px'
        #             })
        #         ], color="dark", inverse=True),
        #     ], width={'size': 3, 'offset': 0, 'order': 1}, className="mt-4 mb-3 "),

        #     dbc.Col([
        #         dbc.Card([
        #             dbc.CardHeader(
        #                 Lottie(options=options, width="32%", height="32%", url=url_image)),
        #             dbc.CardBody([
        #                 html.H4('Total cases'),
        #                 html.H6('4,357,478'),
        #                 html.H6('statcan,2022'),
        #             ], style={
        #                 'textAlign': 'center',
        #                 'borderRadius': '100px'
        #             })
        #         ], color="dark", inverse=True),
        #     ], width={'size': 3, 'offset': 0, 'order': 2}, className="mt-4 mb-3 "),
        #     dbc.Col([
        #         dbc.Card([
        #             dbc.CardHeader(
        #                 Lottie(options=options, width="32%", height="32%", url=url_test)),
        #             dbc.CardBody([
        #                 html.H4('Deaths'),
        #                 html.H6("46,710"),
        #                 html.H6('statcan,2022')
        #             ], style={
        #                 'textAlign': 'center',
        #                 'borderRadius': '100px',
        #                 'AlignItem': 'Stretch',
        #             })
        #         ], color="dark", inverse=True),
        #     ], width={'size': 3, 'offset': 0, 'order': 3}, className="mt-4 mb-3 "),
        # ]),
    ]),
    dbc.Col(dcc.Graph(figure=fig), width=12),

    dbc.Row([

            dbc.Col(
                dcc.Graph(id='graph2',
                          figure={'data': [
                              {'x': [2018, 2020],
                               'y':[60.2, 68.6],
                                  'type':'bar', 'name':"Santé autoévaluée : très bonne ou excellente"
                               },
                              {'x': [2018, 2020],
                               'y':[68.2, 54],
                                  'type':'bar', 'name':'Santé mentale autoévaluée : très bonne ou excellente'
                               },
                          ],
                              'layout':{
                              'title': 'Enquête sur la santé dans les collectivités canadiennes entre 2018-2020',
                              'style': {'color': 'white'},
                              ' template': 'simple_white',
                              'plot_bgcolor': 'rgba(0,0,0,0)',
                              'paper_bgcolor': 'rgba(0,0,0,0)',
                          }
                          }), width={'size': 5, 'offset': 1, 'order': 1}, className='mt-2 mb-2'
            ),
            dbc.Col([
                    dcc.Graph(id='10',
                              figure={'data': [
                                  {'x': ["Diplômé du secondaire ou moins", "Études postsecondaires ou plus", "Revenu le plus bas", "Revenu moyen", "Revenu le plus élevé", "Immigrant reçu ou résident non permanent, statut d'immigrant", "Non-immigrant, statut d'immigrant", "minorité visible ou identité autochtone",
                                         "Identité autochtone", "Pas une minorité visible ou pas un Autochtone", "Premières Nations (hors réserve)",
                                         "Métis", "Inuit, identité autochtone", "Autochtone", "Population n’ayant pas d’identité autochtone",
                                         "Noire", "Asiatique EST", "Asiatique Ouest", "Arabe ou Asiatique de l’Ouest", "Latino-Américaine", "Autres origines"],
                                   'y':[10981700, 2719900, 7704000, 3953100, 3679100, 3316200, 2720900, 8260800, 1860200, 469500, 8461600, 238500, 197000, 15300, 18700, 10322600, 256900, 619000, 409400, 134500, 114200, 326300, ],
                                   'type':'lines', 'name':"Les deux sexes"
                                   },
                                  {'x': ["Diplômé du secondaire ou moins", "Études postsecondaires ou plus", "Revenu le plus bas", "Revenu moyen", "Revenu le plus élevé", "Immigrant reçu ou résident non permanent, statut d'immigrant", "Non-immigrant, statut d'immigrant", "minorité visible ou identité autochtone",
                                         "Identité autochtone", "Pas une minorité visible ou pas un Autochtone", "Premières Nations (hors réserve)",
                                         "Métis", "Inuit, identité autochtone", "Autochtone", "Population n’ayant pas d’identité autochtone",
                                         "Noire", "Asiatique EST", "Asiatique Ouest", "Arabe ou Asiatique de l’Ouest", "Latino-Américaine", "Autres origines"],
                                   'y':[5661600, 1277800, 4095300, 1761200, 1945200, 1938600, 1386800, 4274800, 957800, 233300, 4378600, 116800, 101500, 6700, 8300, 5336800, 116100, 328200, 203700, 71600, 69200, 169000],
                                   'type':'bar', 'name':"Homme"
                                   },
                                  {'x': ["Diplômé du secondaire ou moins", "Études postsecondaires ou plus", "Revenu le plus bas", "Revenu moyen", "Revenu le plus élevé", "Immigrant reçu ou résident non permanent, statut d'immigrant", "Non-immigrant, statut d'immigrant", "minorité visible ou identité autochtone",
                                         "Identité autochtone", "Pas une minorité visible ou pas un Autochtone", "Premières Nations (hors réserve)",
                                         "Métis", "Inuit, identité autochtone", "Autochtone", "Population n’ayant pas d’identité autochtone",
                                         "Noire", "Asiatique EST", "Asiatique Ouest", "Arabe ou Asiatique de l’Ouest", "Latino-Américaine", "Autres origines"],
                                   'y':[5320100, 1442100, 3608700, 2191900, 1733900, 1377600, 1334100, 3986000, 902400, 236300, 4083000, 121700, 95600, 8600, 10400, 4985800, 140800, 290800, 205700, 62800, 45000, 157300],
                                   'type':'bar', 'name':"femme"
                                   },
                              ],
                                  'layout':{
                                  'title': "Nombre d'adultes ayant au moins un problème de santé sous-jacent",
                                  'style': {'color': 'white'}, 'plot_bgcolor': 'rgba(0,0,0,0)',
                                  'paper_bgcolor': 'rgba(0,0,0,0)',
                                  'template': 'simple_white'
                              }
                              }),

                    ], width={'size': 5, 'offset': 1, 'order': 2},),

            ]),
    dbc.Row([
            dbc.Col(
                dcc.Graph(id='graph3',
                          figure={'data': [
                              {'x': ['Total, 15ans et plus', '15 ans à 24 ans', '25 à 34ans', '35 à 44ans', '45 à 54ans', '55 à 64ans', '65ans et plus'],
                               'y':[68.2, 62.1, 66.1, 68.9, 67.6, 70.4, 72.2],
                                  'type':'bar', 'name':"Santé autoévaluée : très bonne ou excellente 2018"
                               },
                          ],
                              'layout':{
                              'title': "enquête sur la santé selon l'âge entre 2018-2020",
                              'style': {'color': 'white'},
                              'template': "simple_white",
                              'plot_bgcolor': 'rgba(0,0,0,0)',
                              'paper_bgcolor': 'rgba(0,0,0,0)',
                          }
                          }), width={'size': 5, 'offset': 1, 'order': 2}

            ),
            dbc.Col(
                dcc.Graph(id='graph4',
                          figure={'data': [
                              {'x': ['Femmes', 'Hommes', 'Tous'],
                               'y':[11, 13, 9],
                                  'type':'bar', 'name':"Autochtones"
                               },
                              {'x': ['Femmes', 'Hommes', 'Tous'],
                               'y':[5, 5, 4],
                                  'type':'bar', 'name':"non auchtones"
                               },
                          ],
                              'layout':{
                              'title': "l'impact de la COVID-19 sur la violence familiale( %)",
                              'style': {'color': 'white'},
                              'template': "simple_white",
                              'plot_bgcolor': 'rgba(0,0,0,0)',
                              'paper_bgcolor': 'rgba(0,0,0,0)',
                          }
                          }), width={'size': 5, 'offset': 1, 'order': 1}

            ),

            ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='graph6',
                      figure={'data': [
                          {'x': ['mars-20', 'avr-20', 'mai-20', 'juin-20', 'mars-20', 'avr-20', 'mai-20', 'juin-20', 'mars-20', 'avr-20', 'mai-20', 'juin-20'],
                           'y':[1220, 889, 1110, 1202, 161, 127, 156, 164, 414, 365, 424, 398],
                           'type':'bar', 'name':"Total des voies de fait "
                           },
                          {'x': ['mars-20', 'avr-20', 'mai-20', 'juin-20', 'mars-20', 'avr-20', 'mai-20', 'juin-20', 'mars-20', 'avr-20', 'mai-20', 'juin-20'],
                           'y':[718, 616, 489, 482, 125, 125, 159, 112, 523, 559, 368, 309],
                           'type':'bar', 'name':"Total des affaires d'introduction par effraction"
                           },
                          {'x': ['mars-20', 'avr-20', 'mai-20', 'juin-20', 'mars-20', 'avr-20', 'mai-20', 'juin-20', 'mars-20', 'avr-20', 'mai-20', 'juin-20'],
                           'y':[1881, 1649, 1879, 1859, 371, 386, 427, 445, 514, 502, 497, 506],
                           'type':'bar', 'name':"Querelles de ménage et conflits familiaux"
                           },
                      ],
                          'layout':{
                          'title': "Demandes d'intervention pendant la pandémie, mars 2020 à juin 2020.",
                          'style': {'color': 'white'},
                          'template': "simple_white",
                          'plot_bgcolor': 'rgba(0,0,0,0)',
                          'paper_bgcolor': 'rgba(0,0,0,0)',
                      }
                      }), className="w-50"

        ),
        dbc.Col(

            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Description", className="card-title"),
                        html.P([
                            "L'isolement social, la perte d'emploi et la baisse du revenu sont tous des facteurs reconnus pour augmenter le risque de violence familiale. Ces conditions se sont accentuées au cours des derniers mois.Un peu plus de la moitié (54 % ) des services aux victimes participants ont déclaré une hausse du nombre de victimes de violence familiale qu'ils ont servies entre la mi-mars et le début de juillet.La plupart des services aux victimes ont trouvé des façons de s'adapter à la pandémie de COVID-19 afin de continuer à servir leurs clients, par exemple en adoptant des pratiques de nettoyage accrues, en demandant à leur personnel de travailler à domicile ou en utilisant la technologie pour communiquer avec leurs clients.",
                        ],
                            className="card-text",
                        ),
                    ]
                ),
                className="w-60 h-75 color-danger mt-4 mb-2",
            ),

        )

    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='graph7',
                      figure={'data': [
                          {'x': ['Alcohol', 'Tabac', 'Canabis', ],
                           'y':[3.5, 13.8, 4.1],
                              'type':'line', 'name':"2022"
                           },
                      ],
                          'layout':{
                          'title': "impact du covid sur la consommation des boisons canabis et autres",
                          'style': {'color': 'white'}, 'plot_bgcolor': 'rgba(0,0,0,0)',
                          'paper_bgcolor': 'rgba(0,0,0,0)',
                      }
                      }), width={'size': 5, 'offset': 1, 'order': 2}

        ),
        dbc.Col(
            dcc.Graph(id='graph8',
                      figure={'data': [
                          {'x': ["Provinces de l'Atlantique", "Qc", "Ont", "Man et Sask", "Alb", "C -B"],
                           'y':[8.1, 8.2, 8.1, 8.1, 8, 8],
                           'type':'lines', 'name':"2018"
                           },
                          {'x': ["Provinces de l'Atlantique", "Qc", "Ont", "Man et Sask", "Alb", "C -B"],
                           'y':[7.1, 6.8, 6.7, 7, 6.7, 6.5],
                           'type':'lines', 'name':"2020"
                           },
                      ],
                          'layout':{
                          'title': "la santé dans les collectivités canadiennes",
                          'style': {'color': 'white'}, 'plot_bgcolor': 'rgba(0,0,0,0)',
                          'paper_bgcolor': 'rgba(0,0,0,0)',
                      }
                      }), width={'size': 5, 'offset': 1, 'order': 1}

        ),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='graph9',
                      figure={'data': [
                          {'x': ['Blancs', 'Sud-Asiatiques', 'Chinois', 'Noirs', 'Philippins', 'Arabes'],
                           'y':[52.2, 55.3, 48.1, 48.1, 45.5, 48.6],
                              'type':'lines', 'name':"Santé mentale un peu moins bonne ou bien moins bonne depuis 2019"
                           },
                          {'x': ['Blancs', 'Sud-Asiatiques', 'Chinois', 'Noirs', 'Philippins', 'Arabes'],
                           'y':[24.2, 34.6, 22, 32, 37.2, 30],
                           'type':'lines', 'name':"un trouble d'anxiété généralisée modéré ou sévère"
                           },
                          {'x': ['Blancs', 'Sud-Asiatiques', 'Chinois', 'Noirs', 'Philippins', 'Arabes'],
                           'y':[22.9, 30.3, 25.7, 27.9, 26.9, 21],
                           'type':'lines', 'name':"santé mentale passable ou mauvaise"
                           },
                      ],
                          'layout':{
                          'title': "Répercussions sur laSanté mentale(du 24 avril au 11 mai 2020).",
                          'style': {'color': 'white'}, 'plot_bgcolor': 'rgba(0,0,0,0)',
                          'paper_bgcolor': 'rgba(0,0,0,0)',
                          'Showlegend': False,
                      }
                      }), className='w-50', width={'size': 6, 'offset': 0, 'order': 2}

        ),
        dbc.Col(
            dcc.Graph(id='graph5',
                      figure={'data': [
                              {'x': ['noir', 'Coréen', 'chinois', 'phillipin', "N'appartenant pas à une minorité visible"],
                               'y':[11, 13, 9],
                                  'type':'bar', 'name':"2020"
                               },
                              ],
                              'layout':{
                              'title': "les perceptions à l'égard de la sécurité",
                              'style': {'color': 'white'},
                              'template': "simple_white",
                              'plot_bgcolor': 'rgba(0,0,0,0)',
                              'paper_bgcolor': 'rgba(0,0,0,0)',
                      }
                      }), width={'size': 5, 'offset': 1, 'order': 1}

        ),
    ]),

])
# if __name__ == '__main__':
#     app.run_server(debug=True)
