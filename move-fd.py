# python 3.10
import os
import shutil
import argparse
import time


class Search_FF:
    def __init__(self, path: str) -> None:
        """Search files and folders.

        Args:
            path (str): your path
        """
        self.__path = path
        self.__counter_files = 0
        self.__counter_folders = 0
        self.__files = []
        self.__folders = []
        if os.path.isdir(self.__path):
            self.__search_folders(self.__path)
            self.__search_files(self.__path)
        else:
            print("'{}' this does not exist or is not a folder!".format(self.__path))

    def get_files(self) -> list:
        return self.__files

    def get_folders(self) -> list:
        return self.__folders

    def files_found(self) -> int:
        return self.__counter_files

    def folders_found(self) -> int:
        return self.__counter_folders

    def __search_folders(self, folder: str):
        files = []
        current = os.listdir(folder)
        for x in current:
            full_path = folder + "\\" + x
            files.append(full_path)
        for f in files:
            if os.path.isdir(f):
                time.sleep(1/100)
                self.__counter_folders += 1
                self.__folders.append(f)
                self.__search_folders(f)

    def __search_files(self, folder: str):
        files = []
        current = os.listdir(folder)
        for x in current:
            full_path = folder + "\\" + x
            files.append(full_path)
        for f in files:
            if os.path.isfile(f):
                name_file = str(f).split('\\')
                if name_file[len(name_file)-1] == "move-fd.py":
                    continue
                self.__counter_files += 1
                self.__files.append(f)
            if os.path.isdir(f):
                time.sleep(1/100)
                self.__search_files(f)


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
    description='Script to easily move files from one place to another.')

group = parser.add_argument_group(description="[move-fd]")

group.add_argument('-x', '--archive', type=str, metavar='',
                   help='file or folder name, example -x "one.txt"')

group.add_argument('-o', '--output', type=str, metavar='',
                   help='output example: -o "{}"'.format(os.getcwd()))

group_search = parser.add_argument_group(
    description="[search-ff] - Only for folders")

group_search.add_argument('--files', dest='files_found',
                          action='store_true',
                          help="total number of files.")

group_search.add_argument('--folders', dest='folders_found',
                          action='store_true',
                          help="total numbres of folders.")

group_search.add_argument('--get-files', dest='get_files',
                          action='store_true',
                          help=("print files, "
                                "{recommendation do not use this if there are many files}"))

group_search.add_argument('--get-folders', dest='get_folders',
                          action='store_true',
                          help=("print folders, "
                                "{recommendation do not use this if there are many folders}"))


args = parser.parse_args()
if __name__ == '__main__':
    var_sff = None
    if args.archive:
        var_sff = Search_FF(args.archive)

    if args.archive and args.output:
        move_file(args.archive, args.output)

    if args.files_found:
        num_files = var_sff.files_found()
        print(">> files found: " + str(num_files))

    if args.folders_found:
        num_folders = var_sff.folders_found()
        print(">> folders found: " + str(num_folders))

    if args.get_files:
        print("=> files")
        for f in var_sff.get_files():
            print(f)

    if args.get_folders:
        print("=> folders")
        for f in var_sff.get_folders():
            print(f)
