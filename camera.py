import subprocess
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Camera:
    def capture_image(self, output_file, resolution=None, exposure_time=None):
        """Captura una imagen estática en formato JPEG con parámetros especificados."""
        cmd = ['libcamera-still', '-o', output_file, '--immediate']
        if resolution:
            cmd.extend(['--width', str(resolution[0]), '--height', str(resolution[1])])
        if exposure_time:
            cmd.extend(['--shutter', str(exposure_time)])
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"Imagen capturada exitosamente: {output_file}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error al capturar imagen: {e.stderr.decode()}")

    def capture_video(self, output_file, duration, resolution=None, exposure_time=None):
        """Captura un video en formato H.264 con la duración y parámetros especificados."""
        cmd = ['libcamera-vid', '-o', output_file, '--timeout', str(duration * 1000)]
        if resolution:
            cmd.extend(['--width', str(resolution[0]), '--height', str(resolution[1])])
        if exposure_time:
            cmd.extend(['--shutter', str(exposure_time)])
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"Video capturado exitosamente: {output_file} ({duration}s)")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error al capturar video: {e.stderr.decode()}")