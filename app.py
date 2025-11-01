from dash import Dash
from data_processing.consolidacion import consolidacion_mortalidad
from layout import dashboard_layout


app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Panel de mortalidad Colombia"
df = consolidacion_mortalidad()
departamentos = sorted(df["DEPARTAMENTO"].unique())

app.layout = dashboard_layout(departamentos)

import callbacks.histograma
import callbacks.mapa
import callbacks.lineas
import callbacks.barras
import callbacks.circular
import callbacks.tabla
import callbacks.barras_apiladas
if __name__ == '__main__':
    app.run(debug=True)