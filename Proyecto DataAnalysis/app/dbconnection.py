import mysql.connector

def conectadb ():
    # Establecer la conexión
    conn = mysql.connector.connect(
        host="34.89.156.140",
        user="root",
        password="curso",
        database="restaurantes"
    )

    # Comprobar si la conexión fue exitosa
    if conn.is_connected():
        #print('Conexión exitosa a la base de datos')
        cursor = conn.cursor()
        return cursor

def cierradb (cur):
    pass
