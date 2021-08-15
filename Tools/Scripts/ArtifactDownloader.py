import os
from sys import platform
import requests
import random

class ArtifactDownloader:
    def __init__(self, url) -> None:
        self.artifact_url = url
        # Run Download
        self.download()

    def fetch_data(self):
        self.fetched_data = requests.get(self.artifact_url)


    def download(self):
        # Fetch data
        self.fetch_data()

        if not os.path.exists(f"{os.getcwd()}/dist"):
            os.mkdir(f"{os.getcwd()}/dist")
        else:
            os.mkdir(f"{os.getcwd()}/dist{random.random()}")
        
        preferred_executable_name = "bitbuild.exe" if platform == "win32" else "bitbuild"
        
        output_file = open(f"{os.getcwd()}/dist/{preferred_executable_name}", "wb")

        output_file.write(self.fetched_data)