import os
import subprocess
from params import img_size
from .utils import clear_folder


def run():
    # Creating a vector of positive images
    clear_folder('tmp/vector')
    num_files = len(os.listdir('tmp/positives/rawdata'))
    command = [
        "tmp/createsamples.exe",
        "-info", "tmp/positives/info.txt",
        "-vec", "tmp/vector/facevector.vec",
        "-num", str(num_files),
        "-w", str(img_size),
        "-h", str(img_size)
    ]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    print(result.stderr.decode())
