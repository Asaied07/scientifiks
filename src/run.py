# Desde App importa la funcion create_app
from app import create_app

# Iguala create_app() a una variable
app = create_app()

# determina si un archivo de Python se está ejecutando como un programa principal 
# o si está siendo importado como un módulo en otro archivo
if __name__ == '__main__':
    # Como si es el archivo principal, se ejecuta app.run con los parametros descritos  
    app.run(host='0.0.0.0', port='9500', debug=True)