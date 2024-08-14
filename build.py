import os
import subprocess

command = (
    "python setup.py build" if os.name in ("nt", "dos") else "python3 setup.py build"
)

p1 = subprocess.Popen(
    command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
)
out, err = p1.communicate()

print(out)
print(err)
if p1.returncode == 0:
    print("Command success")
else:
    print(f"Command failed. Return code: {p1.returncode}")
