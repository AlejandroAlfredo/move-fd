"""
[ move-fd functions ]
"""
import os
import shutil


def move_file(archive: str, output: str):
    try:
        if not os.path.exists(archive):
            print("(move-fd): '{}' not found!".format(archive))
        if not os.path.exists(output):
            print("(move-fd): '{}' does not exist!".format(output))
        if os.path.exists(archive) and os.path.exists(output):
            shutil.move(archive, output)
            print("(move-fd): '{}' has been moved!".format(archive))
    except IOError as ioe:
        print("IOError: " + str(ioe))
    except Exception as e:
        raise Exception(str(e))
