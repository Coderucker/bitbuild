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
            RUN_COUNT = 0
            for i in range(0, len(sys.argv)):
                if sys.argv[i] == "--count" or sys.argv[i] == "-c":
                    RUN_COUNT = sys.argv[i + 1]

            watcher.watch(RUN_COUNT)

        except ValueError:
            watcher.watch(True)
    elif config_type == "dir":
        watcher = DirectoryWatcher(config=[config_file, config_on_change_command, config_on_delete_command])

        watcher.watch(condition=True)

if __name__ == "__main__":
    main()
