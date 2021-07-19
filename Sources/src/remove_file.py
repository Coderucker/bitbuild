import os

def remove_file(file: str):
    if os.path.exists(file):
        os.remove(file)