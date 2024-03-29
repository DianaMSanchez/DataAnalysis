
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import send_file
import mysql.connector 
from io import BytesIO


 # Establecer la conexión
conn = mysql.connector.connect(
    host="34.89.156.140",
    user="root",
    password="curso",
    database="restaurantes"
)

query = "SELECT restaurant_link, restaurant_name, country, region, province, city, address, latitude, longitude, claimed, awards, top_tags, price_level, price_range, meals, cuisines, special_diets, features, vegetarian_friendly, vegan_options, gluten_free, open_days_per_week, open_hours_per_week, working_shifts_per_week, avg_rating, total_reviews_count, default_language, reviews_count_in_default_language, excellent, very_good, average, poor, terrible, food, service, value, atmosphere, keywords FROM cleanvalues"
df = pd.read_sql (query, conn)

#df = pd.read_csv("csv/hnsc_clean.csv") 

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

    #Estadística descriptiva de nuestros datos. 
    print("Estadistica Descriptiva")
    print (df.describe())

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
    plt.figure(figsize=(6, 12)) #tamaño en pulgadas.
    #Pinto la figura con la agrupación realizada
    grouped["restaurant_name"].plot(kind='barh')
    #Modifico algunas configuraciones de la figura pintada
    plt.title('Restaurantes por país', size=20)
    plt.xlabel('País', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    plt.show()
    plt.savefig('DistribRestaurantes.jpg') #Para guardar la imagen

# Función para obtener la distribución de restaurantes por países
def restByCountry():
    #Número de restaurantes por País.
    print("Número de restaurantes por País")
    grouped = df.groupby("country").agg({
        "restaurant_name" : 'count'
    }).sort_values( by="restaurant_name", ascending=True)
    print (grouped)

    #Grafico de distribución de restaurantes
    #Creo la figura y le doy tamaño
    colores = ["#AAF683"]
    plt.figure(figsize=(10, 6)) #tamaño en pulgadas.
    #Pinto la figura con la agrupación realizada
    grouped["restaurant_name"].plot(kind='barh', color = colores)
    #Modifico algunas configuraciones de la figura pintada
    plt.xlabel('País', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    img_buffer = BytesIO()
    plt.savefig('./static/images/DistribucionRestaurantes.png') #Para guardar la imagen
    #img_buffer.seek(0)
    plt.clf()
    #plt.show()
    #return send_file(img_buffer, mimetype='image/png')

#Función para obtener cuántos restaruantes han sido reclamados 
def restByClaimed():
    #Número de restaurantes reclamados
    print("Claimed")
    grouped = df.groupby("claimed").agg({
        "claimed" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    #Pinto la figura con la agrupación realizada
    grouped["claimed"].plot(kind='bar', color ="#FF9B85", figsize=(8,8))
    #Modifico algunas configuraciones de la figura pintada
    plt.xlabel('Categoría', size=15)
    plt.ylabel('Numero Restaurantes', size=15)
    plt.savefig('./static/images/DistribucionClaimed.png') #Para guardar la imagen
    plt.clf()
    #plt.show()

#Distribución de Restaurantes por si son Vegetarianos o no. 
def restByVegetarian():
    #Número de restaurantes por Ciudad.
    print("Vegetarianos")
    grouped = df.groupby("vegetarian_friendly").agg({
        "vegetarian_friendly" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    colores = ["#EE6055","#60D394"]
    desfase = (0, 0.1)
    nombres = ["No friendly","Friendly"]
    #Pinto la figura con la agrupación realizada
    grouped["vegetarian_friendly"].plot(kind='pie', labels = nombres, autopct="%0.1f %%", colors=colores, explode=desfase)
    #Modifico algunas configuraciones de la figura pintada
    plt.axis("equal") 
    plt.savefig('./static/images/DistribucionVegetariano.png') #Para guardar la imagen
    plt.clf()
    #plt.show()

#Distribución de Restaurantes por si son Veganos o no. 
def restByVegan():
    #Distribución de restaurantes veganos
    print("Veganos")
    grouped = df.groupby("vegan_options").agg({
        "vegan_options" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    nombres = ["No opción vegana","Disponible Vegana"]
    colores = ["#AAF683","#FFD97D"]
    desfase = (0, 0.01)
    #Pinto la figura con la agrupación realizada
    grouped["vegan_options"].plot(kind='pie', labels = nombres, autopct="%0.1f %%", colors=colores, explode=desfase)
    #Modifico algunas configuraciones de la figura pintada
    plt.axis("equal") 
    plt.savefig('./static/images/DistribucionVegano.png') #Para guardar la imagen
    plt.clf()
    #plt.show()

#Distribución de Restaurantes por si son Gluten_free o no. 
def restByGluten():
    #Distribución de restaurantes por gluten
    print("Gluten Free")
    grouped = df.groupby("gluten_free").agg({
        "gluten_free" : 'count'
    })
    print (grouped)
    
    #Grafico de distribución de restaurantes
    nombres = ["Posible con gluten","Sin gluten"]
    colores = ["#FF9B85","#FFD97D"]
    desfase = (0, 0.1)
    #Pinto la figura con la agrupación realizada
    grouped["gluten_free"].plot(kind='pie', labels = nombres, autopct="%0.1f %%", colors=colores, explode=desfase)
    #Modifico algunas configuraciones de la figura pintada
    plt.axis("equal") 
    plt.savefig('./static/images/DistribucionGluten.png') #Para guardar la imagen
    plt.clf()
    #plt.show()


# Función para obtener la nota promedio de restaurantes por países
def promRestByCountry():
    #Nota promedio de restaurantes por País.
    print("Ranking de países con mejores restaurantes basado en la nota media")
    
    colores = ["#fdcae1"]
    #Ordenar datos después de groupby
    grouped = df.groupby("country").agg({"value" : 'mean'}).sort_values( by="value", ascending=True)
    print (grouped)

    #Grafico de distribución de restaurantes
    #Pinto la figura con la agrupación realizada
    grouped.plot(kind = 'barh', color=colores, figsize=(10,6))
    #Modifico algunas configuraciones de la figura pintada
    #plt.title('Ranking de países con mejores restaurantes basado en la nota media', size=20)
    plt.xlabel('Nota media restaurantes', size=15)
    plt.ylabel('País', size=15)
    plt.savefig('./static/images/Ranking.png') #Para guardar la imagen
    plt.clf()
    #plt.show()

# Función para obtener la calificacion promedio en comida de restaurantes por países
def promFoodByCountry():
    #Nota promedio de restaurantes por País.
    print("Ranking de países basado en la nota media de comida")
    
    colores = ["#77dd77"]
    #Ordenar datos después de groupby
    grouped = df.groupby("country").agg({"food" : 'mean'}).sort_values( by="food", ascending=True)
    print (grouped)

    #Grafico de distribución de restaurantes
    #Pinto la figura con la agrupación realizada
    grouped.plot(kind = 'barh', color=colores, figsize=(10,6))
    #Modifico algunas configuraciones de la figura pintada
    #plt.title('Ranking de países con mejores restaurantes basado en la nota media', size=20)
    plt.xlabel('Nota media comida', size=15)
    plt.ylabel('País', size=15)
    plt.savefig('./static/images/RankingFood.png') #Para guardar la imagen
    plt.clf()
    #plt.show()

# Función para obtener la calificacion promedio en comida de restaurantes por países
def promServiceByCountry():
    #Nota promedio de restaurantes por País.
    print("Ranking de países basado en la nota media de comida")
    
    colores = ["#b0c2f2"]
    #Ordenar datos después de groupby
    grouped = df.groupby("country").agg({"service" : 'mean'}).sort_values( by="service", ascending=True)
    print (grouped)

    #Grafico de distribución de restaurantes
    #Pinto la figura con la agrupación realizada
    grouped.plot(kind = 'barh', color=colores, figsize=(10,6))
    #Modifico algunas configuraciones de la figura pintada
    #plt.title('Ranking de países con mejores restaurantes basado en la nota media', size=20)
    plt.xlabel('Nota media servicio', size=15)
    plt.ylabel('País', size=15)
    plt.savefig('./static/images/RankingService.png') #Para guardar la imagen
    plt.clf()
    #plt.show()


#Ejecutar estadísticas
def ejecutarEstadisticas():
    restByClaimed()
    restByCountry()
    restByVegetarian()
    restByVegan()
    restByGluten()
    promRestByCountry()    
    promFoodByCountry()
    promServiceByCountry()

#Main. 
if __name__ == '__main__':
    #paises()
    #pruebas ()
    #ciudades("France")
    restByClaimed()
    #restByCountry()
    restByVegetarian()
    restByVegan()
    restByGluten()
    #promRestByCountry()
    #promFoodByCountry()
    #promServiceByCountry()