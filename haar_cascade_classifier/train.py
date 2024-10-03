import os
import subprocess
from params import img_size, num_stages
from .utils import clear_folder


def run():
    # Creating a vector of positive images
    print("Creating a vector of positive images")
    clear_folder('tmp/vector')
    num_positives = len(os.listdir('tmp/positive/rawdata'))
    command = [
        "tmp/createsamples.exe",
        "-info", "tmp/positive/info.txt",
        "-vec", "tmp/vector/facevector.vec",
        "-num", str(num_positives),
        "-w", str(img_size),
        "-h", str(img_size)
    ]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    print(result.stderr.decode())

    # Haar-Training
    print("Haar-Training")
    clear_folder('tmp/cascades')
    num_negatives = len(os.listdir('tmp/negative'))
    command = [
        "tmp/haartraining.exe",
        "-data", "tmp/cascades",
        "-vec", "tmp/vector/facevector.vec",
        "-bg", "tmp/negative/bg.txt",
        "-npos", str(num_positives),
        "-nneg", str(num_negatives),
        "-nstages", str(num_stages),
        "-mem", "1024",
        "-mode", "ALL",
        "-w", str(img_size),
        "-h", str(img_size)
    ]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    print(result.stderr.decode())
