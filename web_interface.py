from flask import Flask, render_template, request, redirect, url_for
from camera import Camera  # Importa tu clase Camera
import os

app = Flask(__name__)
camera = Camera()

# Directorio para guardar las capturas
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    """Muestra la página principal con formularios."""
    return render_template('index.html')

@app.route('/capture_image', methods=['POST'])
def capture_image():
    """Captura una imagen con parámetros básicos."""
    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'captured_image.jpg')
    resolution = request.form.get('resolution')  # Ejemplo: "2028x1520"
    if resolution:
        resolution = tuple(map(int, resolution.split('x')))
    else:
        resolution = None
    camera.capture_image(output_file, resolution=resolution)
    return redirect(url_for('index'))

@app.route('/capture_video', methods=['POST'])
def capture_video():
    """Captura un video con duración especificada."""
    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'captured_video.h264')
    duration = int(request.form.get('duration'))  # Duración en segundos
    resolution = request.form.get('resolution')
    if resolution:
        resolution = tuple(map(int, resolution.split('x')))
    else:
        resolution = None
    camera.capture_video(output_file, duration, resolution=resolution)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)