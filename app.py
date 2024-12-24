from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/examenes', methods=['GET', 'POST'])
def examenes():
    if request.method == 'POST':
        # Aquí manejarás el formulario de exámenes, puedes agregarlo a un archivo, lista o base de datos
        pass
    return render_template('examenes.html')

@app.route('/ausentismos', methods=['GET', 'POST'])
def ausentismos():
    if request.method == 'POST':
        # Aquí manejarás el formulario de ausentismos
        pass
    return render_template('ausentismos.html')

@app.route('/capacitaciones', methods=['GET', 'POST'])
def capacitaciones():
    if request.method == 'POST':
        # Aquí manejarás el formulario de capacitaciones
        pass
    return render_template('capacitaciones.html')

if __name__ == '__main__':
    app.run(debug=True)
