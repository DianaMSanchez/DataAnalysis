from flask import Flask, render_template
import tratamiento as t

#Creo la app
app = Flask(__name__)

app.jinja_env.globals["restByCountry"] = t.restByCountry()
app.jinja_env.globals["restByClaimed"] = t.restByClaimed()
app.jinja_env.globals["restByVegetarian"] = t.restByVegetarian()
app.jinja_env.globals["restByVegan"] = t.restByVegan()
app.jinja_env.globals["restByGluten"] = t.restByGluten()
app.jinja_env.globals["promRestByCountry"] = t.promRestByCountry()
app.jinja_env.globals["promFoodByCountry"] = t.promFoodByCountry()
app.jinja_env.globals["promServiceByCountry"] = t.promServiceByCountry()

def cities(country):
    ciudades = t.ciudades(country)
    return ciudades

app.jinja_env.filters['cities'] = cities

#Acciones de precarga. 
@app.before_request
def before_request():
    #Ejecutamos estadísticas para tomar lo que haya en la BD 
    #t.ejecutarEstadisticas()
    print ("Precarga de pantalla")

#Acciones después de la petición
@app.after_request
def after_request(response):
    print ("Después de la petición")
    return response

#Ruta principal
@app.route("/")
def index():
    #Datos a enviar a la página
    data = {
        'titulo' : 'Inicio',
        'bienvenida' : 'Hola, te damos la bienvenida',
    }    
    #Retornamos la renderización de index
    return render_template('index.html', data=data)

@app.route('/restaurante', methods=['GET', 'POST'] )
def restaurante():
    #Array de tipos de comida
    tipos_comida = ['Selecciona', 'Italiana', 'Griega', 'Española']
    horario = ['Selecciona', 'comer', 'cenar']
    ciudades = ['Selecciona', 'Madrid', 'Roma', 'Bruselas']
    pais  = t.paises()
    precio = ['Selecciona', '€', '€€', '€€€€']
    #Datos a enviar a la página
    data = {
        'titulo' : 'Inicio',
        'bienvenida' : 'Dónde comemos hoy?',
        'tipos_comida' : tipos_comida,
        'horario' : horario,
        'paises' :  pais,
        'ciudades' : ciudades,
        'precio' : precio
    }    
    #Retornamos la renderización de la pagina
    return render_template('restaurantes.html', data=data)



#Ruta de información de analisis de datos
@app.route('/analisis')
def analisis():
    data = {
        'titulo' : 'Estadísticas',
        'bienvenida' : 'Los datos de un vistazo',
        'id' : [0]
    }
    return render_template('analisis.html', data=data)

#Ruta de detalle de estadísticas
@app.route('/estadistica/<statId>')
def estadistica(statId):
    data = {
        'titulo' : 'Estadísticas',
        'bienvenida' : 'Estadísticas',
        'id' : statId
    }
    return render_template('estadisticas.html', data=data)

#Ruta de Conocenos
@app.route('/about')
def about():
    data = {
        'titulo' : 'Acerca de',
        'bienvenida' : 'Sobre nosotras'
    }
    return render_template('about.html', data=data)



def page_not_found(error):
    return render_template('404.html'), 404

# Ejecución de la app
if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5000)