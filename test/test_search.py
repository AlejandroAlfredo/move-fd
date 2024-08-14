import os
import time
from movefd.searchfiles import SearchFiles
from movefd.searchdirs import SearchDirectories
from movefd.searchfd import SearchFD


class TestSearch:
    mypath = (
        os.getenv("USERPROFILE") + "\\Desktop"
        if os.name in ("nt", "dos")
        else "/Desktop"
    )

    def message(function):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            function(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"\n[It took {end_time - start_time:0.2f} second(s) to complete]")
            return None

        return wrapper

    @message
    def test_search_files(self):
        searchfiles = SearchFiles(path=self.mypath)
        searchfiles.start()
        searchfiles.join()
        print(f"\n>> Files found: {searchfiles.files_found}")
        print(f"\n>> Files: {searchfiles.get_files()}")

    @message
    def test_search_dirs(self):
        searchdirs = SearchDirectories(path=self.mypath)
        searchdirs.start()
        searchdirs.join()
        print(f"\n>> Dirs found: {searchdirs.dirs_found}")
        print(f"\n>> Dirs: {searchdirs.get_dirs()}")

    @message
    def test_searchfd(self):
        searchfd = SearchFD(path=self.mypath)
        searchfd.start()
        searchfd.join()
        
        print(f"\n>> Files found: {searchfd.files_found}")
        print(f"\n>> Files: {searchfd.get_files()}")

        print(f"\n>> Dirs found: {searchfd.dirs_found}")
        print(f"\n>> Dirs: {searchfd.get_dirs()}")
