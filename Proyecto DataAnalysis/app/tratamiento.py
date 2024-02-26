
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import plotly.express as px
import mysql.connector
import dbconnection

# Establecer la conexión
# conn = mysql.connector.connect(
#     host="34.89.156.140",
#     user="root",
#     password="curso",
#     database="restaurantes"
# )


conn = conectadb ()
print (conn.is_connected())
df = pd.read_sql("SELECT * FROM valoraciones", conn)

#df = pd.read_csv("csv/hnsc.csv") 

def paises():
    #Mostrar países únicos
    #countries = df["country"].drop_duplicates()
    print("Listar paises")
    print (countries)
    return countries

def ciudades(pais):
    #Filtrar datos de una sola columna. En este caso solo las ciudades
    cities = (df["country"]==pais)
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
    
    print("Número de restaurantes por País ordenado de mayor a menor")
    #Ordeno la agrupación por conteo de mayor a menor
    df2 = grouped.groupby(['country'])['Age'].count()
    df2 = df.sort_values(by="restaurant_name", ascending=False, inplace=True)
    print (df2)

    #Grafico de distribución de restaurantes
    #Creo la figura y le doy tamaño
    plt.figure(figsize=(8, 15)) #tamaño en pulgadas.
    #Pinto la figura con la agrupación realizada
    grouped["restaurant_name"].plot(kind='barh')
    #Modifico algunas configuraciones de la figura pintada
    plt.title('Restaurantes por país', size=20)
    plt.xlabel('País', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    plt.show()
    plt.savefig('Distribución Restaurantes.png') #Para guardar la imagen

def restByCountry():
    #Número de restaurantes por País.
    print("Número de restaurantes por País")
    grouped = df.groupby("country").agg({
        "restaurant_name" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    #Creo la figura y le doy tamaño
    plt.figure(figsize=(15, 8)) #tamaño en pulgadas.
    #Pinto la figura con la agrupación realizada
    grouped["restaurant_name"].plot(kind='barh')
    #Modifico algunas configuraciones de la figura pintada
    plt.title('Restaurantes por país', size=20)
    plt.xlabel('País', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    plt.show()
    #plt.savefig('DistribucionRestaurantes.png') #Para guardar la imagen

def restByClaimed():
    #Número de restaurantes por Ciudad.
    print("Claimed")
    grouped = df.groupby("claimed").agg({
        "claimed" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    #Creo la figura y le doy tamaño
    plt.figure(figsize=(8, 15)) #tamaño en pulgadas.
    #Pinto la figura con la agrupación realizada
    grouped["claimed"].plot(kind='bar')
    #Modifico algunas configuraciones de la figura pintada
    plt.title('Restaurantes administrados por sus dueños', size=20)
    plt.xlabel('Categoría', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    plt.show()
    #plt.savefig('DistribucionRestaurantesCity.png') #Para guardar la imagen


def restByClaimed():
    #Número de restaurantes por Ciudad.
    print("Claimed")
    grouped = df.groupby("claimed").agg({
        "claimed" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    #Creo la figura y le doy tamaño
    plt.figure(figsize=(9, 4)) #tamaño en pulgadas.
    #Pinto la figura con la agrupación realizada
    grouped["claimed"].plot(kind='bar', color='r')
    #Modifico algunas configuraciones de la figura pintada
    plt.title('Restaurantes administrados por sus dueños', size=20)

    plt.xlabel('Categoría', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    plt.show()
    #plt.savefig('DistribucionRestaurantesCity.png') #Para guardar la imagen

#Main. 
if __name__ == '__main__':
    #paises()
    #pruebas ()
    #ciudades("France")
    restByClaimed()
    restByCountry()
