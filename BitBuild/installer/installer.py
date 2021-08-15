import os
from pathlib import Path
import requests
import shutil

from BitBuild.util.get_os import get_os
from BitBuild.lib.version import version
from BitBuild.util.download import download
from BitBuild.util.extract_file import extract_file

def error_message():
    """
    Error message when no release asset has been found
    """

    raise BaseException(f"No releases found for version: {version}")


def exists_bitbuild() -> bool:
    file_type = "bitbuild.exe" if get_os() == "windows" else "bitbuild"

    if os.path.exists(f"{Path.home()}\\Applications\\BitBuild\\{file_type}"):
        print("Already Downloaded")
        return True
    else:
        return False
    

def installation():
    """
    The installer function to fetch the executable from github releases and download it.
    """

    if exists_bitbuild() != True:
        preferred_os = get_os()

        print("Installing Latest Binary Release")
        assets_url = dict(requests.get('https://api.github.com/repos/Bit-Build/bitbuild/releases/latest').json()).get("assets_url")

        print(assets_url)

        print("Fetching Release Asset Url")
            
        assets_result = list(requests.get(assets_url).json()) if assets_url != None else error_message()

        zip_download_path = f"download_{get_os()}.zip"
        # Returns if windows .exe based name or just the name
        file_type = "bitbuild.exe" if get_os() == "windows" else "bitbuild"
        zip_downloaded_path = file_type

        for res in assets_result:
            browser_download_url = res["browser_download_url"]

            download(browser_download_url, zip_download_path)

        home = os.path.join(Path.home(), 'Applications', 'BitBuild')

        if not os.path.exists(home):
            if not os.path.exists(f"{Path.home()}\\Applications"):
                os.mkdir(f"{Path.home()}\\Applications")

                if not os.path.exists(f"{Path.home()}\\Applications\\BitBuild"):
                    os.mkdir(f"{Path.home()}\\Applications\\BitBuild")
                        
        binary_path = os.path.join(home, "bitbuild.exe" if preferred_os == "windows" else "bitbuild")
            
        if os.path.exists(f"{Path.home()}/Applications/BitBuild/{file_type}") != True:
            shutil.move(zip_downloaded_path, binary_path)