import subprocess
from params import obj_size
from .utils import clear_folder, copy_folders_content, copy_files_content


def run():
    print("Creating the XML File")
    clear_folder('tmp/cascade2xml')
    copy_folders_content('tmp/cascades', 'tmp/cascade2xml/data')
    copy_files_content('misc', 'tmp/cascade2xml')

    command = [
        "tmp/cascade2xml/haarconv.exe",
        "tmp/cascade2xml/data",
        "result.xml",
        str(obj_size),
        str(obj_size),
    ]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    print(result.stderr.decode())
