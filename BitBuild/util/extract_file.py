from pathlib import Path
from zipfile import ZipFile

def extract_file(file: str):
    """
    Extract Zip Files.
    """

    with ZipFile(file, 'r') as zip:
        # Extracting files
        zip.extractall()