import os
from typing import Literal
from PIL import Image
from params import img_size
from .utils import clear_folder, copy_files_content


def preprocess_imgs(src: str, dest: str, format: Literal['BMP', 'JPEG']):
    formats_extension = {
        'BMP': '.bmp',
        'JPEG': '.jpg'
    }

    for filename in os.listdir(src):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img_path = os.path.join(src, filename)
            with Image.open(img_path) as img:
                # img = img.convert('L')
                img = img.resize((img_size, img_size))

                output_path = os.path.join(
                    dest, os.path.splitext(filename)[0] + formats_extension[format])

                img.save(output_path, format)


def run():
    clear_folder('tmp')
    clear_folder('tmp/negative')
    clear_folder('tmp/positive')
    clear_folder('tmp/positive/rawdata')

    preprocess_imgs('raw_negatives', 'tmp/negative', 'JPEG')
    preprocess_imgs('raw_positives', 'tmp/positive/rawdata', 'BMP')

    with open("tmp/negative/bg.txt", 'w') as bg_file:
        for filename in os.listdir('tmp/negative'):
            bg_file.write(f'{filename}\n')

    copy_files_content('misc', 'tmp')
    copy_files_content('misc', 'tmp/positive')
