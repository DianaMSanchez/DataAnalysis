import mysql.connector

def recuperabd (numreg):
    try:
        # Establecer la conexión
        conn = mysql.connector.connect(
            host="34.89.156.140",
            user="root",
            password="curso",
            database="restaurantes"
        )

        # Comprobar si la conexión fue exitosa
        print (conn.is_connected())
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            # Aquí puedes agregar el código para interactuar con la base de datos
            # Por ejemplo, crear un cursor para ejecutar consultas SQL
            cursor = conn.cursor()
            query = "SELECT * FROM valoraciones LIMIT " + str(numreg)
            print (query)
            cursor.execute(query)
            res=cursor.fetchall()

            # No olvides cerrar el cursor y la conexión cuando termines
            # cursor.close()
            # conn.close()

    except mysql.connector.Error as e:
        print('Error al conectar a la base de datos', e)
    finally:
        if conn.is_connected():
            conn.close()
            print('Conexión cerrada')
            return res

# datos = recuperabd (103)
# for fila in datos:
#     print (fila)


    