import argparse
from camera import Camera

def setup_cli():
    """Configura la interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(description="Control de cámara para telescopio basado en Raspberry Pi")
    subparsers = parser.add_subparsers(dest='command', help="Subcomandos disponibles")

    # Subcomando para capturar imagen
    image_parser = subparsers.add_parser('capture-image', help="Captura una imagen estática")
    image_parser.add_argument('-o', '--output', required=True, help="Archivo de salida (JPEG)")
    image_parser.add_argument('-r', '--resolution', nargs=2, type=int, metavar=('WIDTH', 'HEIGHT'),
                              help="Resolución de la imagen (ancho alto)")
    image_parser.add_argument('-e', '--exposure', type=int, help="Tiempo de exposición en microsegundos")

    # Subcomando para capturar video
    video_parser = subparsers.add_parser('capture-video', help="Captura un video")
    video_parser.add_argument('-o', '--output', required=True, help="Archivo de salida (H.264)")
    video_parser.add_argument('-d', '--duration', type=int, required=True, help="Duración en segundos")
    video_parser.add_argument('-r', '--resolution', nargs=2, type=int, metavar=('WIDTH', 'HEIGHT'),
                              help="Resolución del video (ancho alto)")
    video_parser.add_argument('-e', '--exposure', type=int, help="Tiempo de exposición en microsegundos")

    return parser.parse_args()

def main():
    """Función principal que ejecuta los comandos de la CLI."""
    args = setup_cli()
    camera = Camera()

    if args.command == 'capture-image':
        camera.capture_image(args.output, resolution=args.resolution, exposure_time=args.exposure)
    elif args.command == 'capture-video':
        camera.capture_video(args.output, args.duration, resolution=args.resolution, exposure_time=args.exposure)

if __name__ == "__main__":
    main()