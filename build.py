import os
import subprocess

command = (
    "python setup.py build" if os.name in ("nt", "dos") else "python3 setup.py build"
)

p1 = subprocess.Popen(
    command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)
p1.wait()
