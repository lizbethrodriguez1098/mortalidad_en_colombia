from dash import Input, Output, callback
import plotly.express as px
from data_processing.consolidacion import consolidacion_mortalidad
from util.filtro_departamento import funcion_filtro

df = consolidacion_mortalidad()

@callback(
    Output('grafico_mapa', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualizar_mapa(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    df_conteo = df_filtrado.groupby('COD_DEPARTAMENTO').size().reset_index(name='NUM_MUERTES')
    df_nombres = df_filtrado[['COD_DEPARTAMENTO', 'DEPARTAMENTO']].drop_duplicates()
    df_conteo = df_conteo.merge(df_nombres, on='COD_DEPARTAMENTO', how='left')
    df_conteo["COD_DEPARTAMENTO"] = df_conteo["COD_DEPARTAMENTO"].astype(str).str.zfill(2)
    fig = px.choropleth(
        df_conteo,
        geojson="https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json",
        locations="COD_DEPARTAMENTO",
        featureidkey="properties.DPTO",
        hover_name="DEPARTAMENTO",    
        hover_data={"NUM_MUERTES": True, "COD_DEPARTAMENTO": False},
        color="NUM_MUERTES",
        color_continuous_scale="Reds",
        title = f"Mortalidad en {departamento}" if departamento != "TODOS" else "Mortalidad por departamento en Colombia"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(title_x=0.5)
    return fig
