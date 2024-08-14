import os
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["pytest", "unittest"],
    "include_msvcr": True if os.name in ("nt", "dos") else False,
}

setup(
    name="move-fd",
    version="1.2",
    description="Scripting program to move files and folders",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "move-fd.py",
            base="console",
            copyright="Copyright (c) 2022 AlejandroAlfredo",
            target_name="move-fd",
        )
    ],
)
