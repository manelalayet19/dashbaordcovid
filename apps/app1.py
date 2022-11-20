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
import pandas as pd
import plotly
import plotly.express as px
import geojson
from plotly.subplots import make_subplots
from app import app
from urllib.request import urlopen
# ---------------------------------LOTTIE CONFIG -----------------------------------------------
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))
url_covid = 'https://assets9.lottiefiles.com/packages/lf20_qsgaud1w.json'
url_canada = 'https://assets9.lottiefiles.com/packages/lf20_wt7bupjp.json'
flag = 'https://assets3.lottiefiles.com/packages/lf20_hlfjaudz.json'
# -------------------------------------PANDAS FILES-------------------------------------
df = pd.read_csv('assets/Provincial_Summaries.csv', delimiter=';')
df3 = pd.read_csv(
    'assets/mapping/Statistics_Canada_Health_Regions.csv', delimiter=';')
df2 = pd.read_csv(
    'assets/mapping/Location_of_health_and_social_services_network_facilities_in_Quebec.csv', delimiter=';')
df3 = pd.read_csv(
    'assets/mapping/COVID19_Testing_Centres_in_Canada.csv', delimiter=';')
df4 = pd.read_csv(
    'assets/mapping/Casernes_de_pompiers_au_Qu%C3%A9bec.csv', delimiter=';')
df5 = pd.read_csv('assets/mapping/BC_First_Responders.csv', delimiter=';')
# --------------------------------GEOJSON FILES---------------------------------------------------
stats = 'https://gist.githubusercontent.com/manelalayet19/f0002a30c8d171b1aeaf85e3945a56bb/raw/a6d2dbc6cbf4077aa367d6a8723389cb731c81ca/statistique.geojson'
provinces = 'https://gist.githubusercontent.com/manelalayet19/291d54195ce7897b24f7b356b20c9e0c/raw/de2a0190da2602a3b932c2056e66463958babe6e/provinces.geojson'
localisation = 'https://gist.githubusercontent.com/manelalayet19/be857089cc75cb7574c1fc939d3c4886/raw/1611a81c13639058260bf6791866206a7780e646/localisation_health.geojson'
healthCenters = 'https://gist.githubusercontent.com/manelalayet19/3cdb2d4458438448fe9045f890bdecf8/raw/ca5b879f72b76b63f0719cf067354c52723f52a2/health_regionsCA.geojson'
testing_cenetrs = 'https://gist.githubusercontent.com/manelalayet19/5be74554143775a52e2b96a631153a33/raw/8c8a7d3ca17627564332f2f85a1c89445e595c26/testin_centersCa.geojson'
path = 'https://gist.githubusercontent.com/manelalayet19/868e09410808752ae66656763e5b3e05/raw/a5bb2e48012e496524a48ac9c4e083f3b4fc3e74/canada_covid.geojson'
# ----------------------------------------------------GEOJSON-----------------------------------------------
with urlopen(path) as response:
    covid_summary = geojson.load(response)

# for feature in covid_summary['features']:
#     print(covid_summary)
# ------------------------------------------------GRAPH OBJECTS---------------------------------------------------------------
fig = px.choropleth_mapbox(df, geojson=covid_summary, locations='OBJECTID', featureidkey="properties.OBJECTID", color='NOM',
                           color_continuous_scale="Viridis",
                           width=750,
                           hover_name='Vaccinated',
                           hover_data=["Deaths", "Case_Total", "Vaccinated",
                                       "Dose1", "Dose2", "HBAS12HP", "DoseBoost"],
                           labels={'Décès': 'Covid-19'},
                           mapbox_style="carto-darkmatter",
                           zoom=2, title=' Covid-19 Provincial Summaries',
                           center={"lat": 46.8131, "lon": -71.2075})
fig.update_layout(showlegend=False)

fig2 = px.scatter_mapbox(df2, lat="X", lon="Y", hover_name="ETAB_NOM",
                         hover_data=["ETAB_NOM_A", "INSTAL_N_1", "ADRESSE", "DATE_OUVER", "MUN_NOM",
                                     "RLS_NOM"],
                         color='FID',
                         zoom=5, title='Location of health and social services network facilities in Quebec')
fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(showlegend=False)

fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig3 = px.scatter_mapbox(df3, lat="X", lon="Y", hover_name="USER_Name", hover_data=["USER_Phone", "USER_City",
                                                                                    "USER_Street", "USER_Sun",
                                                                                    "USER_Mon", "USER_Tue", "USER_Wed",
                                                                                    "USER_Thur", "USER_Fri",
                                                                                    "USER_Sat", "USER_Prov"],
                         color_discrete_sequence=["fuchsia"], zoom=5, title='COVID-19 Testing Centres in Canada')
fig3.update_layout(mapbox_style="open-street-map")
fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
crime = pd.read_csv('assets/crime rate.csv', delimiter=';')
fig1 = px.pie(crime, names="Infractions et demandes d'intervention", values="avr-19"

              )
fig4 = px.scatter_mapbox(df4, lat="X", lon="Y", hover_name="rue", hover_data=['nom_servic', 'no_cvq', 'rue', 'ville', 'cp'
                                                                              ],
                         color_discrete_sequence=["fuchsia"], zoom=5, title='Casernes de pompiers QC')
fig4.update_layout(mapbox_style="open-street-map")
fig4.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig5 = px.scatter_mapbox(df5, lat="LATITUDE", lon="LONGITUDE", hover_name="FCLTY_NM", hover_data=["FCLTY_NM", "ADDRESS", "MAIL_ADD", "ST_ADDRESS", "LOCALITY"
                                                                                                  ],
                         color_discrete_sequence=["fuchsia"], zoom=5, title='BC First responders')
fig5.update_layout(mapbox_style="open-street-map")
fig5.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
graphs_custom = [fig1, fig, fig2, fig3, fig4, fig5]
for graph in graphs_custom:
    graph.update_layout(showlegend=False, template='simple_white')
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
# -------------------------------------LAYOUT--------------------------------------------------------------

layout = html.Div([

    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=url_covid)),
                    dbc.CardBody([
                        html.H4('Received at least one dose'),
                        html.H5(id='covid-2020',
                                children="Total Population : 83%"),
                        html.H6("12 and older : 89.7%"),
                        html.H6("5 to 11 years : 53.8%"),
                        html.H6(' October 9, 2022'),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="secondary", inverse=True),
            ]),
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=url_canada)),
                    dbc.CardBody([
                        html.H4('Primary series completed'),
                        html.H5(id='covid-2021',
                                children="Total Population : 88.0%"),
                        html.H6("12 and older : 89.7%"),
                        html.H6("5 to 11 years : 41.6%"),
                        html.H6(' October 9, 2022'),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="info", inverse=True),
            ]),
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=flag)),
                    dbc.CardBody([
                        html.H4('New cases'),
                        html.H4(id='covid-20202',
                                children="New cases (14 days) : +33,590"),
                        html.H5("New cases (1d) : 1006"),
                        html.H5('Cases per 1 M pers : 116,337'),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="danger", inverse=True),
            ]),
        ], className='grid-parent'),

        html.Div([
            html.Div(dcc.Graph(figure=fig)),

            html.Div(dcc.Graph(figure=fig1)),
        ], className='grid-parent'),

        html.Div([
            html.Div(dcc.Graph(figure=fig2)),

            html.Div(dcc.Graph(figure=fig3)),
        ], className='grid-parent'),
        html.Div([
            html.Div(dcc.Graph(figure=fig4)),

            html.Div(dcc.Graph(figure=fig5)),
        ], className='grid-parent'),


    ]),
])
# if __name__ == '__main__':
#     app.run_server(debug=True)
