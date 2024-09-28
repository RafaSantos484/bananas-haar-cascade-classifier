import os
import shutil


def clear_folder(folder: str):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)


def copy_folder_content(src: str, dest: str):
    for filename in os.listdir(src):
        shutil.copy(os.path.join(src, filename), dest)
