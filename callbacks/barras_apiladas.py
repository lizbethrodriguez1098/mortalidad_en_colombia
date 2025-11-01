from dash import Output, Input, callback
import plotly.express as px
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro

df = consolidacion_mortalidad()

@callback(
    Output('grafico_barras_apiladas', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualizar_barras_sexo(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    df_sexo_agrupado =  df_filtrado.groupby(['DEPARTAMENTO','SEXO']).size().reset_index(name="NUMERO DE MUERTES")
    df_sexo_agrupado["SEXO"] = df_sexo_agrupado["SEXO"].replace({
    1: "Masculino",
    2: "Femenino",
    3: "Indeterminado"
    })

    fig = px.bar(
    df_sexo_agrupado,
    x="DEPARTAMENTO",
    y="NUMERO DE MUERTES",
    color="SEXO",
    barmode="stack",
    title="Comparación del total de muertes por sexo en " + (departamento if departamento != "TODOS" else "cada departamento"),
    labels={"NUMERO DE MUERTES": "Número de muertes", "DEPARTAMENTO": "Departamento", "SEXO": "Sexo"},
    color_discrete_map={
        "Masculino": "#007bff",
        "Femenino": "#e83e8c",
        "Indeterminado": "#6c757d"
    },
    template=None 
    )
    fig.update_layout(title_x=0.5)
    return fig
