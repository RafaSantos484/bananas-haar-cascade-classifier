import os
from typing import Literal
from PIL import Image
from params import img_size
from .utils import clear_folder, copy_folder_content


def preprocess_imgs(src: str, dest: str, format: Literal['BMP', 'JPEG']):
    formats_extension = {
        'BMP': '.bmp',
        'JPEG': '.jpg'
    }

    for filename in os.listdir(src):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img_path = os.path.join(src, filename)
            with Image.open(img_path) as img:
                img = img.convert('L')
                img = img.resize((img_size, img_size))

                output_path = os.path.join(
                    dest, os.path.splitext(filename)[0] + formats_extension[format])

                img.save(output_path, format)


def run():
    clear_folder('tmp')
    clear_folder('tmp/negatives')
    clear_folder('tmp/positives')
    clear_folder('tmp/positives/rawdata')

    preprocess_imgs('raw_negatives', 'tmp/negatives', 'JPEG')
    preprocess_imgs('raw_positives', 'tmp/positives/rawdata', 'BMP')

    copy_folder_content('misc/objectmaker', 'tmp/positives')
