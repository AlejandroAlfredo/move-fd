# programa scripting para mover archivos y carpetas.
import os
import shutil
import argparse

def mover_archivo(archive, output):
    if os.path.exists(archive) and os.path.exists(output):
        shutil.move(archive, output)
        print(f"{archive} se ha movido!")
    else:
        print(f"{archive} no encontrado o {output} no existe!")


parser = argparse.ArgumentParser(description="script para mover archivos fácilmente de un lugar a otro.")
parser.add_argument('-x', '--archive', type=str, metavar='', required=True,help="nombre del archivo o carpeta, la 'dirección' es opcional")
parser.add_argument('-o', '--output', type=str, metavar='', required=True, help="ubicación de salida")
args = parser.parse_args()

if __name__ == '__main__':
    mover_archivo(args.archive, args.output)
