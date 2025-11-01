from dash import Output, Input, callback, dash_table, html
import plotly.express as px
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro

df = consolidacion_mortalidad()

@callback(
    Output('grafico_tabla', 'children'),
    Input('dropdown_departamento', 'value')
)
def actualizar_tabla(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    df_causas = df_filtrado.groupby(['COD_MUERTE', 'DESCRIPCION TRES CARACTERES']).size().reset_index(name='TOTAL CASOS')
    df_causas = df_causas.sort_values(by='TOTAL CASOS', ascending=False).head(10)
    tabla = dash_table.DataTable(
        columns=[
            {"name": "Código", "id": "COD_MUERTE"},
            {"name": "Causa de Muerte", "id": "DESCRIPCION TRES CARACTERES"},
            {"name": "Total de Casos", "id": "TOTAL CASOS"},
        ],
        data=df_causas.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'fontFamily': 'Arial',
            'padding': '8px'
        },
        style_header={
            'backgroundColor':'#e9ecef',
            'fontWeight': 'bold',
            'textAlign': 'center'
        },
        page_size=10
    )
    titulo = html.H4(
        "Top 10 causas de muerte en " + (departamento if departamento != 'TODOS' else 'Colombia'),
        style={'textAlign': 'center', 'marginBottom': '15px', 'fontWeight': 'bold'}
    )
    return html.Div([titulo, tabla])
