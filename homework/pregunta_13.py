"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

DATA_DIR = "files/input/"

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.
    """
    tbl0 = pd.read_csv(DATA_DIR + "tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv(DATA_DIR + "tbl2.tsv", sep="\t")

    df = tbl0.merge(tbl2, on="c0")

    return df.groupby("c1")["c5b"].sum()
