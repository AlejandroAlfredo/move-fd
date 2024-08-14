import os
import time
import threading


class SearchDirectories(threading.Thread):
    def __init__(self, path: str, daemon: bool = True, **kwargs):
        """Search directories.

        Args:
            path (str): your full path
            daemon (bool, optional): daemon. Defaults to True.
        """
        super().__init__(daemon=daemon, **kwargs)
        self.path = path
        self.__counter = 0
        self.__directories = []

    def __search(self, directory: str):
        files = []
        full_path = ""
        current = os.listdir(directory)
        for file in current:
            time.sleep(1 / 1000)
            if os.name in ("linux", "posix", "osx"):
                full_path = directory + "/" + file
            elif os.name in ("nt", "dos"):
                full_path = directory + "\\" + file
            files.append(full_path)
        for file in files:
            time.sleep(1 / 1000)
            if os.path.isdir(file):
                self.__counter += 1
                self.__directories.append(file)
                self.__search(file)

    def run(self):
        self.__search(self.path)

    @property
    def dirs_found(self):
        return self.__counter

    def get_dirs(self):
        return self.__directories
