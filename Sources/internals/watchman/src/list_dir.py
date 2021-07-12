import os

def list_dir(directory):
    content = []

    for scan_res in os.scandir(directory):
        content.append(scan_res.path)

    return content