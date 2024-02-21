
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("csv/tripadvisor_european_restaurants.csv") 

# Función para componer una búsqueda de acuerdo a los datos de entrada. 
def filtroRestaurantes (meals, cusines):
    return restaurantes

def paises():
    #Mostrar países únicos
    countries = df["country"].drop_duplicates()
    print("Listar paises")
    print (countries)
    return countries

def ciudades(pais):
    #Filtrar datos de una sola columna. En este caso solo las ciudades
    #cities = (df["country"]==pais))
    print("Listar las ciudades")
    print (cities)
    return cities

#Función pruebas
def pruebas():
    #Traer solo los 5 primeros registros
    print("Imprimo cabecera")
    print (df.head())

    #Traer los últimos 5 registros. 
    print("Imprimo ultimos registros")
    print (df.tail())

    #Filtrar datos de una sola columna. En este caso solo los países. 
    print("Filtro por distintos países")
    print (df["country"].drop_duplicates())

    #Buscar restaurantes en un país específico
    print("Imprimo Restaurantes de un país específico")
    print (df[(df["country"].eq("France"))])

    #Buscar restaurantes en un país específico que sean vegetarianos
    print("Imprimo Restaurantes de un país específico que sean vegetarianos")
    print (df[(df["country"].eq("France")) & (df["vegetarian_friendly"].eq("Y"))])

    #Número de restaurantes por País.
    print("Número de restaurantes por País")
    grouped = df.groupby("country").agg({
        "restaurant_name" : 'count'
    })
    print (grouped)

    #Grafico de distribución
    grouped["restaurant_name"].plot(kind='bar')
    plt.show()


#Main. 
if __name__ == '__main__':
    #paises()
    pruebas ()
    #ciudades("France")
