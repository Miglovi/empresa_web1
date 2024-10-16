from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio
@app.route('/')
def home():
    # Comentario: Página principal con el nombre, descripción y enlaces a otras secciones.
    return render_template('index.html')

# Página "Quiénes Somos"
@app.route('/about')
def about():
    # Comentario: Información sobre la empresa, misión, visión y el equipo.
    return render_template('about.html')

# Página de Servicios
@app.route('/services')
def services():
    # Comentario: Lista de servicios que ofrece GCA Technology.
    return render_template('services.html')

# Página de Noticias
@app.route('/news')
def news():
    # Comentario: Artículos o noticias relacionadas con la empresa.
    return render_template('news.html')

# Página de Contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Comentario: Maneja los datos del formulario de contacto.
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        return f"Gracias, {nombre}. Tu mensaje ha sido enviado."
    return render_template('contact.html')

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
