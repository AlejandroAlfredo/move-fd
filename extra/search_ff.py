"""
[ This is an experimental function ]
Note:
This function has been tested more on Windows than on Linux.
"""
import os
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
            print("(Search_FF): '{}' this does not exist or is not a folder!".format(
                self.__path))

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
        full_path = ""
        current = os.listdir(folder)
        for x in current:
            if os.name in ('linux', 'posix', 'osx'):
                full_path = folder + "/" + x
            else:
                if os.name in ('nt', 'dos'):
                    full_path = folder + "\\" + x
            files.append(full_path)
        for f in files:
            if os.path.isdir(f):
                time.sleep(0.001)
                self.__counter_folders += 1
                self.__folders.append(f)
                self.__search_folders(f)

    def __search_files(self, folder: str):
        files = []
        full_path = ""
        current = os.listdir(folder)
        # name_file = []
        for x in current:
            if os.name in ('linux', 'posix', 'osx'):
                full_path = folder + "/" + x
            else:
                if os.name in ('nt', 'dos'):
                    full_path = folder + "\\" + x
            files.append(full_path)
        for f in files:
            if os.path.isfile(f):
                time.sleep(0.001)
                # [ This is not very important ]
                # if os.name in ('linux', 'posix', 'osx'):
                #     name_file = str(f).split('/')
                # else:
                #     if os.name in ('nt', 'dos'):
                #         name_file = str(f).split('\\')
                # if name_file[len(name_file)-1] == "move-fd.py":
                #     continue
                self.__counter_files += 1
                self.__files.append(f)
            if os.path.isdir(f):
                self.__search_files(f)
