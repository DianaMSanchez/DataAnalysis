from flask import Flask, render_template
import tratamiento as t

#Creo la app
app = Flask(__name__)

#Acciones de precarga. 
@app.before_request
def before_request():
    print ("Precarga de pantalla")

#Acciones después de la petición
@app.after_request
def after_request(response):
    print ("Después de la petición")
    return response

#Ruta principal
@app.route("/")
def index():
    #Array de tipos de comida
    tipos_comida = ['Selecciona', 'Italiana', 'Griega', 'Española']
    horario = ['Selecciona', 'comer', 'cenar']
    ciudades = ['Selecciona', 'Madrid', 'Roma', 'Bruselas']
    pais  = t.paises()
    precio = ['Selecciona', '€', '€€', '€€€€']
    #Datos a enviar a la página
    data = {
        'titulo' : 'Inicio',
        'bienvenida' : 'Hola, te damos la bienvenida',
        'tipos_comida' : tipos_comida,
        'horario' : horario,
        'paises' :  pais,
        'ciudades' : ciudades,
        'precio' : precio
    }    
    #Retornamos la renderización de index
    return render_template('index.html', data=data)

#Ruta de información de detalle del restaurante
@app.route('/restaurante/<restaurantId>')
def restaurante(restaurantId):
    data = {
        'titulo' : 'Info Restaurante',
        'id' : restaurantId
    }
    return render_template('restaurante.html', data=data)

def page_not_found(error):
    return render_template('404.html'), 404

# Ejecución de la app
if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5000)