from dash import Input, Output, callback
import plotly.express as px
import pandas as pd
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro
from util.asignar_categoria import asignar_categoria_edad

df = consolidacion_mortalidad()

@callback(
    Output('grafico_histograma', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actaulizar_histograma_edades(departamento):

    df_filtrado = funcion_filtro(df, departamento)
    df_filtrado["GRUPO_EDAD1"] = pd.to_numeric(df_filtrado["GRUPO_EDAD1"], errors="coerce")
    df_filtrado["CATEGORIA_EDAD"] = df_filtrado["GRUPO_EDAD1"].apply(asignar_categoria_edad)

    df_conteo = df_filtrado.groupby('CATEGORIA_EDAD').size().reset_index(name='MUERTES')
    fig = px.bar(
        df_conteo, 
        x='CATEGORIA_EDAD', 
        y='MUERTES',
        color='CATEGORIA_EDAD',
        title="Distribución de muertes por grupo de edad en " + (departamento if departamento != 'TODOS' else 'Colombia'),
        category_orders={
            "CATEGORIA_EDAD": [
            "Mortalidad neonatal (<1 mes)",
            "Mortalidad infantil (1-11 meses)",
            "Primera infancia (1-4 años)",
            "Niñez (5-14 años)",
            "Adolescencia (15-19 años)",
            "Juventud (20-29 años)",
            "Adultez temprana (30-44 años)",
            "Adultez intermedia (45-59 años)",
            "Vejez (60-84 años)",
            "Longevidad / Centenarios (85+ años)",
            "Edad desconocida"]}
        )
    fig.update_layout(title_x=0.5)
    return fig
