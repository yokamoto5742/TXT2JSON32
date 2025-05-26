import os
import subprocess
import shutil

from version_manager import update_version, update_version_py


def build_executable():
    new_version = update_version()
    update_version_py(new_version)

    subprocess.run([
        "pyinstaller",
        "--name=TXT2JSON32",
        "--windowed",
        "--icon=assets/TXT2JSON32.ico",
        "main.py"
    ])

    dist_dir = os.path.join("dist", "TXT2JSON32")
    internal_dir = os.path.join(dist_dir, "_internal")

    shutil.copy("utils/config.ini", os.path.join(internal_dir, "config.ini"))
    shutil.copy("C:\Shinseikai\TXT2JSON32\mouseoperation.exe", os.path.join(dist_dir, "mouseoperation.exe"))
    shutil.copy("C:\Shinseikai\TXT2JSON32\soapcopy.exe", os.path.join(dist_dir, "soapcopy.exe"))

    print(f"Executable built successfully. Version: {new_version}")


if __name__ == "__main__":
    build_executable()