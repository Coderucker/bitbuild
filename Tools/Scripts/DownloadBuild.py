import sys
import requests
from sys import platform as __os_platform

def get_os() -> str:
    """
    Get the type of Operating System.
    """
    os_name = str(__os_platform)

    if os_name == "win32":
        return "windows"
    elif os_name == "darwin":
        return "macos"
    else:
        return "linux"

args = sys.argv.copy()
# Removing first element which shows the python program path which we does not need :)
args.pop(0)

REQUEST_URL = "https://api.github.com/repos/Bit-Build/bitbuild/actions/artifacts"

artifact_json_response = dict(requests.get(REQUEST_URL).json()).get("artifacts", None)

artifact_donwload_file = open("bit-build-installer.zip", "wb")

# Get last three artifacts which will have "linux", "windows" and "macos" build
for artifact in artifact_json_response:
    if str(artifact.get("name", None)).count("-installer-") != -1 and str(artifact.get("name")).count(get_os()):
        request_content = requests.get(artifact.get("archive_download_url")).content

        artifact_donwload_file.write(request_content)
        print(request_content)
        # Break because we only need the latest build
        break