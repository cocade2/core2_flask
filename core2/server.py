from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def holaaa():
   return('Bienvenido a la tabla de paises')

@app.route('/listas')

def renderizar_listas():

   #Próximamente estas listas serán extraidas de la base de datos

   paises = [

   {'pais': 'Argentina' , 'capital': 'Buenos Aires'},

   {'pais': 'Brasil' , 'capital': 'Brasilia'},

   {'pais': 'Chile' , 'capital': 'Santiago de Chile'},

   {'pais': 'Colombia' , 'capital': 'Bogotá'},

   {'pais': 'Costa Rica' , 'capital': 'San José'},

   {'pais': 'Paraguay' , 'capital': 'Asunción'},

   {'pais': 'Perú' , 'capital': 'Lima'}

]

   return render_template('listas.html', estudiantes=paises)

if __name__ == '__main__':
   app.run(debug=True)