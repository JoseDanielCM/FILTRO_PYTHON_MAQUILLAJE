import json
import csv

RUTA_CATALOGO="catalogo.csv"

def json_traer_datos(archivo):
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def json_guardar_datos(datos,archivo):
    datos=json.dumps(datos,indent=3)
    with open(archivo,"w") as file:
        file.write(datos)

def csv_traer_datos(archivo):
    lista=[]
    with open(archivo,"r") as file:
        lector=csv.DictReader(file)
        for row in lector:
            lista.append(row)
    return lista

