# python 3
# programa scripting para mover archivos y carpetas.
# scripting program to move files and folders.
import os
import shutil
import argparse


def mover_archivo(archive, output):
    try:
        if not os.path.exists(archive):
            print("'{}' not found!".format(archive))
        if not os.path.exists(output):
            print("'{}' does not exist!".format(output))
        if os.path.exists(archive) and os.path.exists(output):
            shutil.move(archive, output)
            print("'{}' has been moved!".format(archive))
    except IOError as err:
        print(str(err))


# example: python move-fd.py -x "file.txt" -o "c:\Users\PROFILE\Desktop"
parser = argparse.ArgumentParser(description='script to easily move files from one place to another')
parser.add_argument('-x', '--archive', type=str, metavar='', required=True, help='file or folder name, example -x "one.txt"')
parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='output example: -o "{}"'.format(os.getcwd()))

args = parser.parse_args()

if __name__ == '__main__':
    mover_archivo(args.archive, args.output)
