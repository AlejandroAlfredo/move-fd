import os
import time
import threading
from .searchfiles import SearchFiles
from .searchdirs import SearchDirectories


class SearchFD(threading.Thread):
    def __init__(self, path: str, daemon: bool = True, **kwargs):
        """Search files and directories.

        Args:
            path (str): your full path
            daemon (bool, optional): daemon. Defaults to True.
        """
        super().__init__(daemon=daemon, **kwargs)
        self.path = path
        self.__counter_files = 0
        self.__counter_dirs = 0
        self.__files = []
        self.__directories = []

    def run(self):
        searchfiles = SearchFiles(self.path)
        searchdirs = SearchDirectories(self.path)

        searchfiles.start()
        searchdirs.start()

        searchfiles.join()
        searchdirs.join()

        self.__counter_files = searchfiles.files_found
        self.__files = searchfiles.get_files()

        self.__counter_dirs = searchdirs.dirs_found
        self.__directories = searchdirs.get_dirs()

    def get_files(self):
        return self.__files

    def get_dirs(self):
        return self.__directories

    @property
    def files_found(self):
        return self.__counter_files

    @property
    def dirs_found(self):
        return self.__counter_dirs
