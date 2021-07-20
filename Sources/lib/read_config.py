import os
from pathlib import Path

from Sources.constants import CONFIG_SUPPORTED_EXTENSIONS
from Sources.lib.parse_config import parse_config

def read_config():
    search_path = Path(os.getcwd())

    for ext in CONFIG_SUPPORTED_EXTENSIONS:
        search_result = search_path.glob(ext)

        for res in search_result:
            try:
                parsed = parse_config(open(res).read())

                return parsed
            except FileNotFoundError:
                print("No config file found")

                print("Falling back to default settings")
                print("Watcher Type -> file")
                print("Watcher Target -> main.py")

                # Returning to default config
                return {
                    "type": "file",
                    "targets": [
                        "main.py",
                        "python main.py"
                    ]
                }
