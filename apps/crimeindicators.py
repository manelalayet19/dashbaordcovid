import pandas as pd
import dash
from dash import Dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_extensions
from dash_extensions import Lottie
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from app import app
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))
crime1 = 'https://assets8.lottiefiles.com/packages/lf20_elinisdo.json'
crime2 = 'https://assets8.lottiefiles.com/packages/lf20_d6xl55tg.json'
crime3 = 'https://assets8.lottiefiles.com/packages/lf20_qkekrsxe.json'
police = 'https://assets8.lottiefiles.com/packages/lf20_wr3tzurd.json'


# -------------------------------------------------------------------PANDAS DF ----------------------------------------
CrimePerrace = {
    'race': ['Noir', 'Korean', 'Chinese', 'Philippin', 'other'],
    'Values': [26, 26, 25, 22, 10],
}
victimes = {
    'type': ['Hausse', 'Aucun changement', 'Baisse'
             ],
    "Nbr TOT d'actes criminels": [31, 50, 19
                                  ],
    "Nbr TOT de violence familiale": [54, 29, 17
                                      ]
}
data = {
    'gender': ['femmes', 'hommes', 'femmes', 'hommes'],
    'type': ['Autochtones', 'Autochtones', 'Non Autochtones', 'Non Autochtones'],
    'Values': [11, 13, 5, 5]
}
Canada = {
    'Year': [1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018
             ],
    'suicide total deaths': [4090, 4140, 4220, 4330, 4370, 4410, 4440, 4440, 4430, 4460, 4360, 4350, 4330, 4340, 4280, 4300, 4270, 4320, 4360, 4420, 4440, 4430, 4550, 4630, 4760, 4830, 4870, 4830, 4760, 4700]
}
hapinnessScore = {
    'happiness Index': [74.2, 0, 74.8, 74.9, 74.9, 76.5, 74.3, 74.2, 75.9, 73, 74.1, 72.5, 74.2, 71.8, 71.1, 70.3, 70.3
                        ],
    'Year': [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020
             ]
}
inflation = {
    'inflation index': [0.888, 3.07, 4.59, 2.04, 0.843, 1.26, 2.44, 1.36, 1.07, -1.36, 3.98, -2.31, 2.85, 3.23, 1.21, 1.74, 1.94, -0.877, 0.754, 2.56, 1.62, 1.48, 0.75],
    'Year': [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019
             ],
}
enqueteSante = pd.DataFrame({
    'Health': ['Health auto-evoluation : good or excellent', 'Mental health auto-evaluation: good or excellent'],
    'Values': [60.2, 68.2]
})
healthpercentage = {
    'Age': [
        'Total, 15ans et plus',
        '15 ans ?? 24 ans',
        '25 ?? 34ans',
        '35 ?? 44ans',
        '45 ?? 54ans',
        '55 ?? 64ans',
        '65ans et plus'
    ],
    '2018': [68.2,
             62.1,
             66.1,
             68.9,
             67.6,
             70.4,
             72.2
             ],
    '2020': [54,
             41.5,
             47.1,
             46.4,
             49.8,
             61.9,
             71.2
             ],
}
anxiety = {
    'pourcentage': ['No symptoms', 'light symptoms', 'Moderate to severe symptoms'
                    ],
    'Homme': [16, 63.6, 20.5],
    'Femme': [9.7, 61, 29.3],
    'Autres': [1.1, 37.1, 61.8],
}
# ---------------------------------------------------------------------
anxious = pd.DataFrame(anxiety)
df2 = pd.DataFrame(inflation)
test = pd.DataFrame(data)
race = pd.DataFrame(CrimePerrace)
vic = pd.DataFrame(victimes)
actesCriminal = pd.read_csv(
    'assets/mapping/actes-criminels.csv', delimiter=',')
happ = pd.DataFrame(hapinnessScore)
df = pd.DataFrame(Canada)
df3 = pd.read_csv('assets/mapping/CPI.csv', delimiter=';')
# print(df)
df4 = pd.read_csv('assets/mapping/custody.csv', delimiter=';')
df5 = pd.read_csv('assets/mapping/custody2.csv', delimiter=';')
res = df5.groupby('Age group')['VALUE'].sum()
# print(res)
CustodyAgegroup = pd.DataFrame(res)
# CustodyAgegroup.to_csv('custodygroup.csv')
df6 = pd.read_csv('assets/mapping/custodygroup.csv', delimiter=',')
df7 = pd.read_csv('assets/mapping/police2.csv', delimiter=';')
fd = df7.groupby('Indigenous identity')['VALUE'].sum()
# fg = fd.to_csv('indigenos_identity.csv')
df8 = pd.read_csv('assets/mapping/indigenos_identity.csv', delimiter=',')
# print(CustodyAgegroup)
df9 = pd.read_csv('assets/mapping/police3.csv', delimiter=';')
pf = df9.groupby('GEO')['VALUE'].sum()
# pf.to_csv('GEO.csv')
df9 = pd.read_csv('assets/GEO.csv', delimiter=',')
familyViolence = pd.read_csv(
    'assets/mapping/familyViolence.csv', delimiter=';')
covid19 = pd.DataFrame({
    'gender': ['Homme', 'Femme', 'Tous'],
    'Impact majeur': [11, 12, 10],
    'Impact mod??r??, mineur, ou aucun': [7, 8, 6],
})
Covid2 = pd.read_csv('assets/mapping/sant??avantaprescovid.csv', delimiter=';')
# --------------------------------------------------Graphs -------------------------------------
suicide_graph = px.bar(df, x='Year', y='suicide total deaths',
                       color='Year', title='Total suicide deaths source world bank ', template='simple_white')
happiness = px.bar(happ, x='Year', y='happiness Index',
                   color='Year', title='Canada Happiness index 2004-2020', template='simple_white')
inflationIndex = px.bar(df2, x='Year', y='inflation index',
                        color='Year', title='Inflation index World bank data')
CPI = px.histogram(df3, x='CPI',
                   y='CPI excluding food and energy', color='Time', hover_data=df3.columns, template='simple_white')
Custody = px.histogram(
    df4, x='Custodial and community supervision', y='VALUE', color='REF_DATE', title='Custodial and community supervision ', template='simple_white')
fig5 = px.bar(df6, x='Age group', y='VALUE', color='Age group',
              title='Custodial and community supervision  grouped by age ', template='simple_white')
fig6 = px.bar(df8, x='Indigenous identity', y='VALUE',
              color='Indigenous identity', title='Indigenous identity grouped by Value', template='simple_white')
fig4 = px.bar(df9, x='GEO', y='VALUE', color='GEO',
              title='Custodial and community supervision per region ', template='simple_white')
fig2 = px.bar(healthpercentage, x='Age', y='2018', template='simple_white',
              title=' la sant?? dans les collectivit??s canadiennes de 2018')
fig3 = px.pie(race, names='race', values='Values', template='simple_white',
              title="Les perceptions ?? l'??gard de la s??curit??, 12 au 25-mai-2020.")
fig = px.pie(test, names='gender', values='Values', color='type', template='simple_white',
             title='Les r??percussions de la COVID-19 ??? Sant?? mentale.')
fig7 = px.bar(vic, x='type', template='simple_white',
              y="Nbr TOT de violence familiale",
              title="Nbr TOT de victimes de violence familiale qui ont re??u des services")
fig9 = px.bar(familyViolence, x='TYPE', y='femme', color='Homme', template='simple_white',
              title="R??percussions de la COVID-19 sur les inqui??tudes quant ?? la violence familiale avril-2020")
fig10 = px.bar(covid19, x='gender', y='Impact majeur', color='gender', template='simple_white',
               title="le stress financier et la victimisation au cours d'une quarantaine et d'un isolement social")

fig12 = px.bar(Covid2, orientation='h', x='Age', y='ESCC??- 2019', color='Age', template='simple_white',
               title="Sant?? mentale avant et apr??s le d??but de la pand??mie de COVID-19 selon le groupe d'??ge")
fig13 = px.bar(Covid2, orientation='h', x='Age', y='SEPC1',
               color='Age', template='simple_white')
fig14 = px.bar(Covid2, orientation='h', x='Age', y='SEPC4',
               color='Age', template='simple_white')
fig15 = make_subplots(rows=3, cols=1, shared_yaxes=True)


fig11 = make_subplots(rows=1, cols=2, shared_xaxes=True)
fig11.append_trace(go.Bar(
    x=covid19['gender'],
    y=covid19['Impact majeur']
), row=1, col=1)
fig11.append_trace(go.Bar(
    x=covid19['gender'],
    y=covid19['Impact mod??r??, mineur, ou aucun']
), row=1, col=2)
fig11.update_layout(
    title="le stress financier et la victimisation au cours d'une quarantaine et d'un isolement social")
fig15.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)', template='simple_white', showlegend=False, title="Nbr de personnes ayant des sympt??mes d'anxi??t?? ")
fig15.append_trace(go.Bar(
    x=anxious['pourcentage'],
    y=anxious['Homme'],
), row=1, col=1)
fig15.append_trace(go.Bar(
    x=anxious['pourcentage'],
    y=anxious['Femme'],
), row=2, col=1)
fig15.append_trace(go.Bar(
    x=anxious['pourcentage'],
    y=anxious['Autres'],
), row=3, col=1)
# --------------------------------------------------------Layout function ------------------
graphs = [suicide_graph, fig, fig10, fig11, fig12, fig13,
          fig14, fig15, fig2, fig4, fig5, fig6, fig9, fig7, Custody, CPI, inflationIndex, happiness]
for graph in graphs:
    graph.update_layout(showlegend=False, template='simple_white')
# fig1 = px.bar(enqueteSante, title='Sources :Statistique Canada, Enqu??te sur la sant?? dans les collectivit??s canadiennes de 2018 et S??rie d???enqu??tes sur les perspectives canadiennes de 2020.')
# -------------------------------------------------------------Layout -------------------------
layout = html.Div([

    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=crime1)),
                    dbc.CardBody([
                        html.H6('Crime Severity Index'),
                        html.H6(id='crime-15',
                                children="73.7%"),
                        html.H6("12 and older : 89.7%"),
                        html.H6("5 to 11 years : 53.8%"),
                        html.I(className="bi bi-arrow-down-circle-fill"),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="dark", inverse=True),
            ]),
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=crime2)),
                    dbc.CardBody([
                        html.H6(
                            'Police-reported crime rate per 100,000 population'),
                        html.H6(id='crime20',
                                children="5.375"),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="light", inverse=True),
            ]),
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=crime3)),
                    dbc.CardBody([
                        html.H6('Violent Crime Severity Index'),
                        html.H6(id='crime24',
                                children="92.5%"),
                        html.H6("5.1%"),
                        html.I(className="bi bi-arrow-up-circle-fill"),
                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="danger", inverse=True),
            ]),
        ], className="grid-parent"),
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=crime1)),
                    dbc.CardBody([
                        html.H6('Homicide victims'),
                        html.H6(id='crime27',
                                children="743 victims"),
                        html.H6('Homicide rate per 100,000 population :2.0'),
                        html.H6('7.0 % annual change'),
                        html.H6('statcan,2020')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="primary", inverse=True),
            ]),
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=crime3)),
                    dbc.CardBody([
                        html.H6('Non-violent Crime Severity Index'),
                        html.H6(id='crime5',
                                children="66.7"),
                        html.H6("-2.8%"),

                        html.H6('statcan,2022')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="info", inverse=True),
            ], className="grid-parent"),
            html.Div([
                dbc.Card([
                    dbc.CardHeader(
                        Lottie(options=options, width="32%", height="32%", url=police)),
                    dbc.CardBody([
                        html.H6('Youth crime rate'),
                        html.H6(id='crime2',
                                children="2.175"),
                        html.H6("-2.6%"),
                        html.H6('statcan,2020')
                    ], style={
                        'textAlign': 'center',
                        'borderRadius': '100px',
                        'size': '12px'
                    })
                ], color="dark", inverse=True),
            ]),
        ], className="grid-parent"),
        # ----------------------------Graphs -----------------------------------------------

        html.Div([
            html.Div([dcc.Graph(id='suicide_rate', figure=suicide_graph),
                      ]),
            html.Div(dcc.Graph(id='happinessIndex',
                               figure=happiness)),
        ], className='grid-parent'),
        html.Div([
            html.Div([dcc.Graph(id='ih', figure=inflationIndex),
                      ]),
            html.Div(dcc.Graph(id='cc', figure=CPI)),
        ], className="grid-parent"),


        html.Div([
            html.Div([dcc.Graph(id='hh', figure=Custody),
                      ]),
            html.Div(dcc.Graph(id='ff', figure=fig5)),
        ], className='grid-parent'),
        html.Div([
            html.Div([dcc.Graph(id='ft', figure=fig6),
                      ]),
            html.Div(dcc.Graph(id='ij', figure=fig4)),
        ], className='grid-parent'),
        html.Div([
            html.Div([dcc.Graph(id='xo', figure=fig3),
                      ]),
            html.Div(dcc.Graph(id='tf', figure=fig7)),
        ], className='grid-parent'),
        html.Div([
            html.Div([dcc.Graph(id='x', figure=fig),
                      ]),
            html.Div(dcc.Graph(id='y', figure=fig9)),
        ], className='grid-parent'),
        html.Div([
            html.Div(dcc.Markdown('''
            **??volution du paysage de la vuln??rabilit????: le stress financier et la victimisation au cours d'une quarantaine et d'un isolement social peuvent accro??tre le risque de violence familiale
            Un stress financier peut ??tre ressenti en temps de crise, en particulier au sein des populations les plus vuln??rables.**

            Les r??sultats du projet de collecte par approche participative d'avril r??v??lent que le stress financier ??tait associ?? ?? des inqui??tudes plus ??lev??es de violence familiale.
            Environ 1??participant sur 6 (16??%) a d??clar?? penser que la pand??mie pourrait avoir des ????r??percussions majeures???? sur sa capacit?? ?? respecter ses obligations financi??res. Ces pr??occupations au sein de la population immigrante (20??%) sont sup??rieures ?? celles de la population n??e au Canada (12??%).
            Parmi ces participants, environ 11??% ont d??clar?? que la possibilit?? de violence familiale semait chez eux beaucoup ou ??norm??ment d'inqui??tude, comparativement ?? 7??% chez les autres participants.
            Lien entre la capacit?? de rencontrer ses obligations financi??res et la violence familiale.
            Source:Statistiqu Canada, Approche participative??: R??percussions de la COVID-19 sur les Canadiens, 2020.
'''),  className='mt-2 mb-2'
                     ),
            html.Div(dcc.Graph(id='df', figure=fig10),
                     className='mt-2 mb-2'),
        ], className='grid-parent'),
        dbc.Row([
            html.Div(dcc.Graph(figure=fig11),  className='mt-2 mb-2'),
            html.Div(dcc.Graph(figure=fig12), className='mt-2 mb-2'),
        ], className='grid-parent'),
        dbc.Row([
            html.Div(dcc.Markdown('''**Avant la pand??mie, les membres de la communaut?? LGBTQ couraient un risque plus ??lev?? d'avoir un trouble de l'humeur.**

Depuis la pand??mie, parmi les r??pondants ?? une enqu??te reposant sur l'approche participative, les personnes de diverses identit??s de genre ??taient???
plus susceptibles de d??clarer avoir une sant?? mentale passable ou mauvaise (70??%), comparativement aux participants de sexe f??minin (25,5??%) et de sexe masculin (21,2??%);
deux fois plus susceptibles que les femmes et trois fois plus susceptibles que les hommes de d??clarer des sympt??mes correspondant ?? un trouble d'anxi??t?? g??n??ralis??e mod??r?? ou grave (62??%, 29??%, 21??%).
Ces diff??rences peuvent s'expliquer en partie par???
le plus jeune ??ge des personnes de diverses identit??s de genre;
les participants de diverses identit??s de genre ??taient plus susceptibles d'??tre tr??s ou extr??mement pr??occup??s par les r??percussions possibles de la COVID-19.
une plus grande probabilit?? de perte d'emploi et de ressources financi??res inad??quates.
Le trouble d'anxi??t?? g??n??ralis??e (TAG) est un ??tat caract??ris?? par des soucis fr??quents et persistants ainsi qu'une anxi??t?? excessive ?? l'??gard de plusieurs ??v??nements ou activit??s.
**Sources:??Statistics Canada, Canadian Community Health Survey, 2019; Canadian Perspectives Survey Series 1; Canadian Perspectives Survey Series 4; *not seasonally adjusted.**
''')),
            html.Div(dcc.Graph(figure=fig14),  className='mt-2 mb-2'),
        ], className='grid-parent'),
        html.Div([
            html.Div(dcc.Graph(figure=fig13),  className='mt-2 mb-2'),
            html.Div(dcc.Graph(figure=fig15), className='mt-2 mb-2'),
        ], className='grid-parent'),
    ]),

])
# if __name__ == '__main__':
#     app.run_server(debug=True)
