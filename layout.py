from dash import html, dcc
import dash_bootstrap_components as dbc

def dashboard_layout(departamentos):
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1(
                    "Dashboard de Mortalidad en Colombia",
                    className="fw-bold mb-1",
                    style={"color": "#0d6efd","textAlign": "center", "fontSize": "45px"} 
                ),
                html.H5(
                    "Análisis interactivo de causas, distribución y patrones de mortalidad - Año 2019",
                    className="text-center mb-1 text-secondary",
                    style={"textAlign": "center", "fontSize": "20px"} 
                )
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.Label("Selecciona un departamento:", className="fw-bold",style={"fontSize": "18px"}),
                dcc.Dropdown(
                    id='dropdown_departamento',
                    options=[{'label': d, 'value': d} for d in ['TODOS'] + departamentos],
                    value='TODOS',
                    clearable=False,
                    className='mb-4'
                ),
            dcc.Tabs([
                dcc.Tab(label="Mapa geográfico de mortalidad", children=[dcc.Graph(id='grafico_mapa')]),
                dcc.Tab(label="Tendencia mensual de mortalidad", children=[dcc.Graph(id='grafico_lineas')]),
                dcc.Tab(label="Ciudades con mayor índice de homicidios", children=[dcc.Graph(id='grafico_barras')]),
                dcc.Tab(label="Ciudades con menor índice de mortalidad", children=[dcc.Graph(id='grafico_pie')]),
                dcc.Tab(label="Principales causas de muerte", children=[html.Div(id='grafico_tabla')]),
                dcc.Tab(label="Comparativo de mortalidad por sexo", children=[dcc.Graph(id='grafico_barras_apiladas')]),
                dcc.Tab(label="Mortalidad por grupos de edad", children=[dcc.Graph(id='grafico_histograma')]),
            ])
            ], width=7)
        ], justify="center"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.P(
                    "Autores: Farid Steven Baron Bayona & Lizbeth Natalia Rodriguez Castillo",
                    className="text-center fw-semibold mt-3 mb-1"
                ),
                html.P(
                    "Universidad de La Salle — Maestría en Inteligencia Artificial",
                    className="text-center text-secondary",
                    style={"fontSize": "0.9rem"}
                )
            ])
        ])
    ], fluid=True)