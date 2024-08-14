import os
import argparse
import datetime
from movefd.movefd import MoveFD
from movefd.searchfiles import SearchFiles
from movefd.searchdirs import SearchDirectories
from movefd.searchfd import SearchFD


parser = argparse.ArgumentParser(
    prog="move-fd",
    description="Script to easily move files from one place to another.",
)

group_movefd = parser.add_argument_group(description="[move-fd]")

group_movefd.add_argument(
    "-x",
    "--source",
    type=str,
    nargs=1,
    metavar="<source>",
    help='file or dir name, example -x "one.txt"',
)

group_movefd.add_argument(
    "-o",
    "--output",
    type=str,
    nargs=1,
    metavar="<path>",
    help=f'output example: -o "{os.getcwd()}"',
)

group_search = parser.add_argument_group(description="[search] ~> Only for dirs")

group_search_exclusive = group_search.add_mutually_exclusive_group()

group_search_exclusive.add_argument(
    "-F",
    "--files-found",
    dest="files_found",
    action="store_true",
    help="search files.",
)

group_search_exclusive.add_argument(
    "-D",
    "--dirs-found",
    dest="dirs_found",
    action="store_true",
    help="search directories.",
)

group_search_exclusive.add_argument(
    "-A",
    "--fd-found",
    dest="fdfound",
    action="store_true",
    help="search files and directories",
)

group_search.add_argument(
    "-l",
    "--log",
    dest="log",
    action="store_true",
    help="print log",
)


args = parser.parse_args()


def log_message(files, directories, counter_files, counter_dirs):
    print(f"Date: ({datetime.datetime.now()})\n")
    print(f"files: ({counter_files}) =>\n {files}\n")
    print(f"dirs: ({counter_dirs}) =>\n {directories}\n\n")


if __name__ == "__main__":
    counter_files = 0
    counter_dirs = 0
    files = []
    directories = []
    if args.source:
        instance_sf = SearchFiles(path=args.source[0])
        instance_sd = SearchDirectories(path=args.source[0])
        instance_sfd = SearchFD(path=args.source[0])

    if args.source and args.output:
        instance_movefd = MoveFD(args.source[0], args.output[0])
        instance_movefd.start()
        instance_movefd.join()

    if args.source and args.files_found:
        instance_sf.start()
        instance_sf.join()
        counter_files = instance_sf.files_found
        files = instance_sf.get_files()

    if args.source and args.dirs_found:
        instance_sd.start()
        instance_sd.join()
        counter_dirs = instance_sd.dirs_found
        directories = instance_sd.get_dirs()

    if args.source and args.fdfound:
        instance_sfd.start()
        instance_sfd.join()
        counter_files = instance_sfd.files_found
        counter_dirs = instance_sfd.dirs_found
        files = instance_sfd.get_files()
        directories = instance_sfd.get_dirs()

    if args.log:
        log_message(files, directories, counter_files, counter_dirs)
