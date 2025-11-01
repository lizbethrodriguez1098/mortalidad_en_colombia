from dash import Output, Input, callback
import plotly.express as px
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro

df = consolidacion_mortalidad()

@callback(
    Output('grafico_lineas', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualizar_lineas(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    df_conteo = df_filtrado.groupby('MES').size().reset_index(name='NUM_MUERTES')

    fig = px.line(
        df_conteo,
        x="MES",
        y="NUM_MUERTES",
        markers=True,
        title="Total de muertes por mes en " + (departamento if departamento != "TODOS" else "Colombia"),
        labels={"MES": "Mes", "NUM_MUERTES": "Número de muertes"}
    )

    fig.update_layout(template="plotly_white",title_x=0.5)
    return fig
