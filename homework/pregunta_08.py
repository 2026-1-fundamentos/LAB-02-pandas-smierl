"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

DATA_DIR = "files/input/"

def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de `c0` y `c2` al
    data frame que contiene el archivo `tbl0.tsv`.
    """
    df = pd.read_csv(DATA_DIR + "tbl0.tsv", sep="\t")
    df["suma"] = df["c0"] + df["c2"]
    return df