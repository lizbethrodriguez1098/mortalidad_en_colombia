from dash import Output, Input, callback
import plotly.express as px
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro

df = consolidacion_mortalidad()

@callback(
    Output('grafico_barras', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualizar_barras_homicidios(departamento):
    codigos_homicidios = ['X95']
    df_filtrado = funcion_filtro(df, departamento)
    df_filtrado = df_filtrado[df_filtrado["COD_MUERTE"].isin(codigos_homicidios)].copy()
    df_ciudades = (
        df_filtrado.groupby("MUNICIPIO")
        .size()
        .reset_index(name="NUM_HOMICIDIOS")
        .sort_values(by="NUM_HOMICIDIOS", ascending=False)
        .head(5)
    )

    fig = px.bar(
        df_ciudades,
        x="MUNICIPIO",
        y="NUM_HOMICIDIOS",
        text="NUM_HOMICIDIOS",
        color="MUNICIPIO",
        title="Top 5 ciudades más violentas en " + (departamento if departamento != 'TODOS' else 'Colombia'),
        labels={"MUNICIPIO": "Ciudad", "NUM_HOMICIDIOS": "Número de homicidios"}
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(template="plotly_white", showlegend=False, xaxis_tickangle=-30)
    return fig
