import sys

from Sources.main import (DirectoryWatcher, FileWatcher)
from Sources.lib.read_config import read_config

def main():
    config = read_config()
    config_type = config.get("type", "file")
    config_file = config.get("targets", "main.py")[0]
    config_on_change_command = config.get("targets", "python main.py")[1]
    config_on_delete_command = config.get("targets", "print('deleted')")[2]

    if config_type == "file":
        watcher = FileWatcher([config_file, config_on_change_command, config_on_delete_command])

        try:
            RUN_COUNT = sys.argv.index("--count") + 1

            watcher.watch(RUN_COUNT)

        except ValueError:
            watcher.watch(True)

main()