from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')
def index():
    # aqui retorna lo que uno le diga (puede ser un texto simple o una pagina web)
    # para este caso vamos a redirigil a index.html
    return render_template('index.html')

@app.route('/about')
def about():
    # aqui retorna lo que uno le diga (puede ser un texto simple o una pagina web)
    # para este caso vamos a redirigil a about.html
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9500')