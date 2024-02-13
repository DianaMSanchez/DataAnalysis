from flask import Flask, render_template

#Creo la app
app = Flask(__name__)

@app.route("/")
def index():
    #Array de tipos de comida
    tipos_comida = ['Italiana', 'Griega', 'Española']
    #Datos a enviar a la página
    data = {
        'titulo' : 'Inicio',
        'bienvenida' : 'Hola, te damos la bienvenida',
        'tipos_comida' : tipos_comida
    }
    #Retornamos la renderización de index
    return render_template('index.html', data=data)

# Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True, port=5000)