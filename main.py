import sys

from BitBuild.main import (DirectoryWatcher, FileWatcher, DirWatcherTests, FileWatcherTests)# Imports Include test files too
from BitBuild.src.read_config import read_config
from BitBuild.installer.installer import installation

sys_args = sys.argv.copy()

def main():
    try:
        config = read_config()
        config_type = config.get("type")
        config_file = config.get("targets")[0]
        config_on_change_command = config.get("targets")[1]
        config_on_delete_command = config.get("targets")[2]

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
    except AttributeError:
        print("Error: Config not found :(")

if __name__ == "__main__":
    #main()
    installation()

# curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/swudots/swudo/releases/latest