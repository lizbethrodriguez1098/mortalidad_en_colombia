import pandas as pd
from functools import lru_cache
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_PATH / "data"

@lru_cache()
def consolidacion_mortalidad():

    # Se leen los archivos de excel 
    df_mortalidad = pd.read_excel(RAW_PATH / "Anexo1.NoFetal2019_CE_15-03-23.xlsx")
    dim_causa = pd.read_excel(RAW_PATH / "Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx", skiprows=8)
    dim_divipola = pd.read_excel(RAW_PATH / "Divipola_CE_.xlsx")

    # Limpieza
    columnas = {
        "Capítulo": "CAPITULO",
        "Nombre capítulo": "NOMBRE CAPITULO",
        "Código de la CIE-10 tres caracteres": "COD_MUERTE",
        "Descripción  de códigos mortalidad a tres caracteres": "DESCRIPCION TRES CARACTERES",
        "Código de la CIE-10 cuatro caracteres": "CIE CUATRO CARACTERES",
        "Descripcion  de códigos mortalidad a cuatro caracteres": "DESCRIPCION CUATRO CARACTERES"
    }
    dim_causa = (
        dim_causa.rename(columns=columnas)
        .drop_duplicates(subset="COD_MUERTE")
        .loc[:, ["CAPITULO", "NOMBRE CAPITULO", "COD_MUERTE", "DESCRIPCION TRES CARACTERES"]]
    )

    df_mortalidad["COD_MUERTE"] = df_mortalidad["COD_MUERTE"].str[:3]

    # Unificación de tablas
    df = (
        df_mortalidad
        .merge(dim_divipola, on=["COD_DANE", "COD_DEPARTAMENTO", "COD_MUNICIPIO"], how="inner")
        .merge(dim_causa, on="COD_MUERTE", how="inner")
    )
    return df
