from dash import Output, Input, callback
import plotly.express as px
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro

df = consolidacion_mortalidad()

@callback(
    Output('grafico_pie', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualizar_pie(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    df_menor_mortalidad = df_filtrado.groupby("MUNICIPIO").size().reset_index(name="NUM_MUERTES").sort_values(by="NUM_MUERTES", ascending=True).head(10)
    fig = px.pie(
        df_menor_mortalidad,
        names="MUNICIPIO",
        values="NUM_MUERTES",
        title="Top 10 de ciudades con menor índice de mortalidad en " + (departamento if departamento != 'TODOS' else 'Colombia'),
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig.update_traces(textinfo='percent', pull=[0.05]*len(df_menor_mortalidad))
    fig.update_layout(template="plotly_white",title_x=0.5)

    return fig
