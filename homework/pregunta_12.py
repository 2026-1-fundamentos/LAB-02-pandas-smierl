"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

DATA_DIR = "files/input/"

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c5a` y `c5b` (unidos por ':') de la tabla
    `tbl2.tsv`.
    """
    df = pd.read_csv(DATA_DIR + "tbl2.tsv", sep="\t")

    return (
        df.sort_values(["c0", "c5a"])
          .assign(c5=lambda x: x["c5a"] + ":" + x["c5b"].astype(str))
          .groupby("c0")["c5"]
          .apply(",".join)
          .reset_index()
    )