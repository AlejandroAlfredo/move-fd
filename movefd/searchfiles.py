import os
import time
import threading


class SearchFiles(threading.Thread):
    def __init__(self, path: str, **kwargs):
        super().__init__(**kwargs)
        self.path = path
        self.__counter = 0
        self.__files = []

    def __search(self, directory: str):
        files = []
        full_path = ""
        current = os.listdir(directory)
        for file in current:
            if os.name in ("linux", "posix", "osx"):
                full_path = directory + "/" + file
            elif os.name in ("nt", "dos"):
                full_path = directory + "\\" + file
            files.append(full_path)
        for file in files:
            if os.path.isfile(file):
                time.sleep(1 / 1000)
                self.__counter += 1
                self.__files.append(file)
            elif os.path.isdir(file):
                self.__search(file)

    def run(self):
        self.__search(self.path)

    def files_found(self) -> int:
        return self.__counter

    def get_files_path(self) -> list[str]:
        return self.__files
