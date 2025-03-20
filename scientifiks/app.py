from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')
def index():
    # aqui retorna lo que uno le diga (puede ser un texto simple o una pagina web)
    # para este caso vamos a redirigil a index.html
    return render_template('index.html')

@app.route('/about') #ruta
def about():
    return render_template('about.html')

@app.route('/operaciones')
def operaciones():
    return render_template('operaciones.html')

@app.route('/producido')
def producido():
    return render_template('producido.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9500')