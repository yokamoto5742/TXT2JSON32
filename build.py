import os
import subprocess
import shutil

from version_manager import update_version, update_version_py


def build_executable():
    os.chdir(r"C:\Users\yokam\PycharmProjects\TXT2JSON32")

    new_version = update_version()
    update_version_py(new_version)

    subprocess.run([
        "pyinstaller",
        "--name=TXT2JSON32",
        "--windowed",
        "--icon=assets/TXT2JSON.ico",
        "main.py"
    ])

    dist_dir = os.path.join("dist", "TXT2JSON")
    internal_dir = os.path.join(dist_dir, "_internal")

    shutil.copy("utils/config.ini", os.path.join(internal_dir, "config.ini"))

    print(f"Executable built successfully. Version: {new_version}")


if __name__ == "__main__":
    build_executable()