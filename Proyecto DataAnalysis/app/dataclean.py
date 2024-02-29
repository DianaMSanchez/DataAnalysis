import csv
import mysql.connector

# Establecer la conexión a la base de datos MySQL
conn = mysql.connector.connect(
        host="34.89.156.140",
        user="root",
        password="curso",
        database="restaurantes"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()
# query="use restaurantes;"
# cursor.execute(query)
# cursor.fetchall

# Ruta al archivo CSV
archivo_csv = "../csv/hnscshort.csv"


# Abrir el archivo CSV y leer línea por línea
r=0
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Verificar si la línea contiene campos nulos
        if not any(field is None for field in row):
            # Insertar la línea en la tabla de la base de datos
            # cursor.execute("INSERT INTO restaurantes.cleanvalues (restaurant_link, restaurant_name, country, region, province, city, address, latitude, longitude, claimed, awards, top_tags, price_level, price_range, meals, cuisines, special_diets, features, vegetarian_friendly, vegan_options, gluten_free, original_open_hours, open_days_per_week, open_hours_per_week, working_shifts_per_week, avg_rating, total_reviews_count, default_language, reviews_count_in_default_language, excellent, very_good, average, poor, terrible, food, service, value, atmosphere, keywords) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%i,%i,%i,%i,%i,%s,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%s)", row)
            # Hacer commit para guardar los cambios
            # conn.commit()
            print (row)
            print (r)
            r+=1
           

# Cerrar el cursor y la conexión
print ("Lineas copiadas: ",r)
cursor.close()
conn.close()