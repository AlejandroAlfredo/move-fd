# python 3.8
import os
import shutil
import argparse


def move_file(archive: str, output: str):
    try:
        if not os.path.exists(archive):
            print("'{}' not found!".format(archive))
        if not os.path.exists(output):
            print("'{}' does not exist!".format(output))
        if os.path.exists(archive) and os.path.exists(output):
            shutil.move(archive, output)
            print("'{}' has been moved!".format(archive))
    except IOError as ioe:
        print("Error: " + str(ioe))
    except Exception as e:
        raise


parser = argparse.ArgumentParser(
    description='script to easily move files from one place to another')

parser.add_argument('-x', '--archive', type=str, metavar='', required=True,
                    help='file or folder name, example -x "one.txt"')

parser.add_argument('-o', '--output', type=str, metavar='', required=True,
                    help='output example: -o "{}"'.format(os.getcwd()))

args = parser.parse_args()
if __name__ == '__main__':
    move_file(args.archive, args.output)
