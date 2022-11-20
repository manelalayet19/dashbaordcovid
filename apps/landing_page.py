from distutils import extension
from distutils.log import debug
from tokenize import group
from unicodedata import category
import dash
from dash import Output, Input
from dash import dcc
from dash import html
from dash import Dash
import dash_bootstrap_components as dbc
from dash_extensions import Lottie
import pandas
import pandas as pd
import plotly
import plotly.express as px
import geojson
from app import app
import dash_leaflet as dl
from dash_extensions.javascript import arrow_function
from plotly.subplots import make_subplots
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))
url_covid = 'https://assets5.lottiefiles.com/packages/lf20_xbeapo0i.json'
url_test = 'https://assets5.lottiefiles.com/packages/lf20_4ilboxgz.json'
url_image = 'https://assets5.lottiefiles.com/packages/lf20_wt7bupjp.json'
url_canada = 'https://assets5.lottiefiles.com/packages/lf20_CXxysN.json'
# ------------------------------------------------------------------------DF--------------------------------------------
consumer_prices = pd.read_csv(
    'assets/Consumer Price Index, monthly, not seasonally adjusted 2019-2022 janvier.csv', delimiter=';')
# print(consumer_prices)
df = pd.read_csv('assets/metalhealth2018.csv', delimiter=';',
                 skiprows=0, low_memory=False)
df_1 = pd.read_csv('assets/Provincial_Daily_Totals.csv')
chommage = pd.read_csv('assets/taux de chommage.csv', delimiter=';')
heure_travail = pd.read_csv('assets/heures de travail.csv', delimiter=';')

# ---------------------------- Geojson files ----------------------------------------------------------------
geojson = dl.GeoJSON(url="https://gist.githubusercontent.com/manelalayet19/868e09410808752ae66656763e5b3e05/raw/a5bb2e48012e496524a48ac9c4e083f3b4fc3e74/canada_covid.geojson", zoomToBounds=True,
                     hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray='')))
testing_covid = dl.GeoJSON(url='https://raw.githubusercontent.com/manelalayet19/manel/master/testing_covid.geojson', zoomToBounds=True,
                           hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray='')))
# ------------------------------------plotly figures -------------------------------------------------------
fig1 = make_subplots(rows=1, cols=1, shared_xaxes=True,
                     vertical_spacing=0.008, horizontal_spacing=0.008, start_cell='top-left')
fig1['layout']['margin'] = {'l': 5, 'r': 10, 'b': 0, 't': 25}
fig1.update_layout(
    title_text="Indice des prix à la consommation mensuel, non désaisonnalisé ",
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    # height=350,
    # width=450,
    template="simple_white",
    font=dict(
        size=12,
        family='Times New Roman',
        color='white'
    ),
)

fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['January 2019'], 'type': 'scatter', 'name': 'ensemble'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['March 2019'], 'type': 'bar', 'name': 'Aliments'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['June 2019'], 'type': 'bar', 'name': 'Logement'}, 1, 1)
fig1.append_trace({'x': consumer_prices['Products'], 'y': consumer_prices['September 2019'],
                  'type': 'bar', 'name': 'Dépenses courantes'}, 1, 1)
fig1.append_trace({'x': consumer_prices['Products'], 'y': consumer_prices['December 2019'],
                  'type': 'bar', 'name': 'Vêtements et chaussures'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['January 2020'], 'type': 'bar', 'name': 'Transports'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['March 2020'], 'type': 'bar', 'name': 'Essence'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['June 2020'], 'type': 'bar', 'name': 'Soins'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['September 2020'], 'type': 'bar', 'name': 'Loisirs'}, 1, 1)
fig1.append_trace({'x': consumer_prices['Products'], 'y': consumer_prices['December 2020'],
                  'type': 'bar', 'name': 'Boissons et autres'}, 1, 1)
fig1.append_trace({'x': consumer_prices['Products'], 'y': consumer_prices['January 2021'],
                  'type': 'bar', 'name': 'sauf aliments et énergie'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['March 2021'], 'type': 'bar', 'name': 'sauf énergie'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['June 2021'], 'type': 'bar', 'name': 'energie'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['September 2021'], 'type': 'bar', 'name': 'Biens'}, 1, 1)
fig1.append_trace(
    {'x': consumer_prices['Products'], 'y': consumer_prices['December 2021'], 'type': 'bar', 'name': 'Services'}, 1, 1)
# économique barchart
fig2 = px.bar(chommage, x='periode ', y='Taux de chômage',
              color='region', barmode='group', title='taux de chommage 2019-2022')
fig2.update_layout(
    title_text="Taux de chommage ",
    showlegend=False,
    yaxis=dict(range=[0, 15], visible=False),
    template="simple_white",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=12,
        family="Balto",
        color='white'
    )
)
fig3 = px.bar(chommage, x='periode ', y="Taux d'activité",
              color='region', barmode='group', title="taux d'activité par période")
fig3.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    template='simple_white',
    showlegend=False,
    font=dict(
        size=12,
        family='Balto',
        color='white',
    ),

)
fig4 = px.bar(chommage, x='periode ', y="Taux d'emploi",
              color='region', barmode='group')
fig4.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title_text="Taux d'emploi",
    showlegend=False,
    font=dict(
        size=12,
        family='Balto',
        color='white',
    ),
    yaxis=dict(autorange=True, visible=False)
)
# horaire de travail
fig5 = make_subplots(rows=1, cols=1, shared_xaxes=True,
                     vertical_spacing=0.008, horizontal_spacing=0.008, start_cell='top-left')
fig5['layout']['margin'] = {'l': 5, 'r': 10, 'b': 0, 't': 30}
fig5.update_layout(showlegend=True,
                   title_text="horaire de travail  ",
                   template="simple_white",
                   plot_bgcolor='rgba(0,0,0,0)',
                   paper_bgcolor='rgba(0,0,0,0)',
                   font=dict(
                       size=12,
                       color='white',
                   ),
                   yaxis=dict(autorange=True, visible=False)
                   )
fig5.append_trace(
    {'x': heure_travail['période'], 'y': heure_travail['production de biens'], 'type': 'bar', 'name': 'Biens'}, 1, 1)
fig5.append_trace(
    {'x': heure_travail['période'], 'y': heure_travail['Agriculture'], 'type': 'bar', 'name': 'agricole'}, 1, 1)
fig5.append_trace(
    {'x': heure_travail['période'], 'y': heure_travail['Fabrication'], 'type': 'bar', 'name': 'fabrication'}, 1, 1)
fig5.append_trace(
    {'x': heure_travail['période'], 'y': heure_travail['culture et loisirs'], 'type': 'bar', 'name': 'culture'}, 1, 1)

fig6 = px.histogram(df, x='Indicateurs', y='VALEUR',
                    color="Groupe d'âge")
fig6.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title_text="nombre de besoin psychiatrique selon l'age (2018)",
    font=dict(
        size=12,
        color='white',
        family='balto'
    ),
    template='simple_white'
)

fig7 = px.pie(df, names='Indicateurs', values='VALEUR',
              color_discrete_map=["Groupe d'âge"])
fig7.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title_text="nombre de besoin psychiatrique selon l'age (2018)",
    font=dict(
        size=12,
        color='white',
        family='balto'
    ),
    template='simple_white')
# ---------------------layout------------------------------
charts = [fig1, fig2, fig3, fig4, fig5, fig6, fig7]
for g in charts:
    g.update_layout(showlegend=False, template='simple_white')
# --------------------------------------------------------------------layout--------------------------------------
# app = dash.Dash(external_stylesheets=[
#                 dbc.themes.SOLAR],)
layout = html.Div([
    dbc.Container([
        # ici le nav bar et les btns pour la connexion ou le passage vers d'autres pages !
        # cette partie pour les indices globaux. décés , genre, age, etc.
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=url_covid)),
                    dbc.CardBody([
                        html.H4('Au moin une dose'),
                        html.H5(id='covid-2022', children="83%"),
                        html.H6("32320750 personne"),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="secondary", inverse=True),
            ], width={'size': 3, 'offset': 0, 'order': 1}, className="mt-4 mb-3"),

            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=url_image)),
                    dbc.CardBody([
                        html.H4('Décès'),
                        html.H5(id='test-2022',
                                children="9268 personnes"),
                        html.H6('27/09/2020'),
                        html.H6('statcan,2022'),
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px'
                    })
                ], color="info", inverse=True),
            ], width={'size': 3, 'offset': 0, 'order': 2}, className="mt-4 mb-3"),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=url_test)),
                    dbc.CardBody([
                        html.H4('Taux de mortalité'),
                        html.H5(id='image-2022', children="6.1%"),
                        html.H6("71% personnes + de 80 ans"),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'AlignItem': 'Stretch',
                    })
                ], color="primary", inverse=True),
            ], width={'size': 3, 'offset': 0, 'order': 3}, className="mt-4 mb-3"),

            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=url_canada)),
                    dbc.CardBody([
                        html.H4('rappel doses'),
                        html.H5(id='canada-2022',
                                children="8.1% (3157174)"),
                        html.H6('depuis le 1er Août 2022'),
                        html.H6('OpendataCanada,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px'
                    })
                ], color="secondary", inverse=True),
            ], width={'size': 3, 'offset': 0, 'order': 4}, className="mt-4 mb-4"),
        ], className='CoronaIndex'),
    ]),
    html.Div([
        html.Div(dl.Map([dl.TileLayer(), testing_covid], center=(-106.01368920084386, 55.99001883073848), zoom=8, style={
            'width': '80%', 'height': '50vh', 'margin': "auto", "display": "block"}, className="mb-2 mt-2", id="1")),


        html.Div(dl.Map([dl.TileLayer(), geojson], center=(-106.01368920084386, 55.99001883073848), zoom=8, style={
            'width': '80%', 'height': '50vh', 'margin': "auto", "display": "block"}, className="mb-2 mt-2", id="2")),
    ], className="grid-parent"),
    # className='mapAreaRow'
    html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ]),
        html.Div([

            dcc.Graph(id='graph2', figure=fig2),
        ]),

    ], className='grid-parent'),
    html.Div([

        html.Div([

            dcc.Graph(id='graph3', figure=fig3),
        ]),

        html.Div([

            dcc.Graph(id='graph4', figure=fig4),
        ]),
    ], className='grid-parent'),
    html.Div([
        html.Div([

            dcc.Graph(id='graph5', figure=fig5),
        ]),

        html.Div([
            dcc.Graph(id='graph6', figure=fig6),
        ]),
    ], className='grid-parent'),
    html.Div([
        html.Div([
            dcc.Graph(id='graph7', figure=fig7),
        ]),
    ], className='grid-parent'),



])
# if __name__ == '__main__':
#     app.run_server(debug=True)
