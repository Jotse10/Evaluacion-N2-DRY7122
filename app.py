from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenidos! Esta es la pagina web de muestra desplegada con Docker y CI/CD."

if __name__ == '__main__':
    #la aplicacion escuchara en todas las interfaces en el puerto 9999.
    app.run(host="0.0.0.0", port=9999 )    
