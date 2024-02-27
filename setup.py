import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "C:\\Users\\micro\\AppData\\Local\\Programs\\Python\\Python311\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Users\\micro\\AppData\\Local\\Programs\\Python\\Python311\\tcl\\tk8.6"

base = None
include_files = [
    "./assets",
    "C:\\Users\\micro\\AppData\\Local\\Programs\\Python\\Python311\\DLLs\\tcl86t.dll",
    "C:\\Users\\micro\\AppData\\Local\\Programs\\Python\\Python311\\DLLs\\tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pycrypt",
    version="1.4",
    description="File Encryption App",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "Pycrypt.py",
            base=base,
            icon="./assets/icon.ico"
        )
    ]
)
