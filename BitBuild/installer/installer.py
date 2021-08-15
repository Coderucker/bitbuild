import os
from pathlib import Path
import shutil
from BitBuild.util.get_os import get_os
from BitBuild.lib.version import version
import requests


def error_message():
    """
    Error message when no release asset has been found
    """
    raise BaseException(f"No releases found for version: {version}")

def installation():
    preferred_os = get_os()

    print("Installing Latest Binary Release")
    asset_url = dict(requests.get('https://api.github.com/repos/Bit-Build/bitbuild/releases/latest').json()).get("assets_url")

    print("Fetching Release Asset Url")
        
    browser_download_urls: list(str) = []
        
    assets_result = list(requests.get(asset_url).json()) if asset_url != None else error_message()

    for res in assets_result:
        browser_download_urls.append(res["browser_download_url"])

    for url in browser_download_urls:
        if url == str("build-artifact-" + preferred_os):
            download_request = requests.get(url)

    home = os.path.join(Path.home(), 'Applications', 'BitBuild')

    if not os.path.exists(home):
        if not os.path.exists(f"{Path.home()}\\Applications"):
            os.mkdir(f"{Path.home()}\\Applications")

            if not os.path.exists(f"{Path.home()}\\Applications\\BitBuild"):
                os.mkdir(f"{Path.home()}\\Applications\\BitBuild")
                    
    binary_path = os.path.join(home, "bitbuild.exe" if preferred_os == "windows" else "bitbuild")
        
    if os.path.exists(f"{Path.home()}/Applications/BitBuild/bitbuild.exe") != True:
        shutil.move("main.spec", binary_path)