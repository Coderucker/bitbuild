import requests

def download(link_for_file: str, path: str):
    """
    This is a function utility to download files from internet.
    Mainly used for downloading binaries from GitHub Releases.
    """
    
    req_content = requests.get(link_for_file).content

    f = open(path, "wb")

    f.write(req_content)