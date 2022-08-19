# python 3.10.5
import os
import argparse
import time

try:
    from extra import search_ff
    from extra import functions
except ImportError as ie:
    raise Exception(str(ie))

parser = argparse.ArgumentParser(
    description='Script to easily move files from one place to another.')

group = parser.add_argument_group(description="[move-fd]")

group.add_argument('-x',
                   '--archive',
                   type=str,
                   metavar='',
                   help='file or folder name, example -x "one.txt"')

group.add_argument('-o',
                   '--output',
                   type=str, 
                   metavar='',
                   help='output example: -o "{}"'.format(os.getcwd()))

group_search = parser.add_argument_group(
    description="[search_ff]* ~> Only for folders")

group_search.add_argument('--files',
                          dest='files_found',
                          action='store_true',
                          help="total number of files.")

group_search.add_argument('--folders',
                          dest='folders_found',
                          action='store_true',
                          help="total number of folders.")

group_search.add_argument('--get-files',
                          dest='get_files',
                          action='store_true',
                          help=("print files, "
                                "(recommendation do not use this if there are many files)"))

group_search.add_argument('--get-folders',
                          dest='get_folders',
                          action='store_true',
                          help=("print folders, "
                                "(recommendation do not use this if there are many folders)"))

args = parser.parse_args()


def main(args: argparse):
    sff = None  # search_ff
    if args.archive:
        sff = search_ff.Search_FF(args.archive)

    if args.archive and args.output:
        functions.move_file(args.archive, args.output)

    if args.files_found:
        num_files = sff.files_found()
        print("(files found): " + str(num_files))

    if args.get_files:
        for f in sff.get_files():
            time.sleep(0.100)
            print("(file): " + str(f))

    if args.folders_found:
        num_folders = sff.folders_found()
        print("(folders found): " + str(num_folders))

    if args.get_folders:
        for f in sff.get_folders():
            time.sleep(0.100)
            print("(folder): " + str(f))


if __name__ == '__main__':
    main(args)
