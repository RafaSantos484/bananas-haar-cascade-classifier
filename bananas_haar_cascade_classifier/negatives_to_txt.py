import os
import shutil
import subprocess


def run():
    current_dir = os.getcwd()
    os.chdir('tmp/negatives')

    subprocess.run('dir /b *.jpg > bg.txt', shell=True)
    shutil.move('bg.txt', os.path.join('..', 'bg.txt'))

    os.chdir(current_dir)
