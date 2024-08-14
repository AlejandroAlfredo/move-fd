import os
import shutil
import threading


class MoveFD(threading.Thread):
    def __init__(self, source: str, output: str, daemon: bool = True, **kwargs):
        super().__init__(daemon=daemon, **kwargs)
        self.source = source
        self.output = output

    def run(self):
        if os.path.exists(self.source) and os.path.exists(self.output):
            shutil.move(self.source, self.output)
            print(f"(move-fd): '{self.source}' has been moved!")
        else:
            raise IOError(f"'{self.output}' does not exist!")
