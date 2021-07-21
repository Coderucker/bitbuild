import sys

from Sources.main import (DirectoryWatcher, FileWatcher)
from Sources.lib.read_config import read_config

sys_args = sys.argv.copy()

def main():
    config = read_config()
    config_type = config.get("type", "file")
    config_file = config.get("targets", "main.py")[0]
    config_on_change_command = config.get("targets", "python main.py")[1]
    config_on_delete_command = config.get("targets", "print('deleted')")[2]

    def get_count_index():
        if sys_args.count('--count') > 0:
            return sys_args.index('--count') + 1
        else:
            return True

    if config_type == "file":
        watcher = FileWatcher([config_file, config_on_change_command, config_on_delete_command])

        if sys_args.count('--count') > 0:
            watcher.watch(get_count_index())
        else:
            watcher.watch(condition=True)
    elif config_type == "dir":
        watcher = DirectoryWatcher(config=[config_file, config_on_change_command, config_on_delete_command])

        watcher.watch(get_count_index())
    else:
        print(f"No such configuration: {config_type}")

if __name__ == "__main__":
    main()
