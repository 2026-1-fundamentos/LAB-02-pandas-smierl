"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

DATA_DIR = "files/input/"

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.
    """
    df = pd.read_csv(DATA_DIR + "tbl1.tsv", sep="\t")

    return (
        df.groupby("c0")["c4"]
        .apply(lambda x: ",".join(sorted(x)))
        .reset_index()
    )