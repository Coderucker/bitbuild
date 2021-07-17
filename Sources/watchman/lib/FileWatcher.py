import time
from datetime import datetime

from Sources.colormania.colormania import useColor
from Sources.watchman.lib.events.events import Events_File
from Sources.watchman.src.remove_file import remove_file


class FileWatcher(Events_File):
    def __init__(self, config) -> None:
        super().__init__()
        self.config = config

    def watch(self):
        current_time = useColor(datetime.now(), "135", "73", "23")

        # Out of the while loop to prevent printing on this message
        print(f"[{current_time}] Watching out for changes in file -> {self.config[0]}")

        while True:
            try:
                f = open(self.config[0]).read()

                time.sleep(0)

                if open(self.config[0]).read() != f:
                    # Printing the change
                    print(f"[{current_time}]: {self.config[0]} -> File has Changes")

                    # calling action func
                    if not type(self.config[1]) == str:
                        self.config[1]()
                    else:
                        exec(self.config[1])
            except KeyboardInterrupt:
                exit()
            except FileNotFoundError:
                print(f"[{current_time}]: File was not found -> {self.config[0]}")
                print("Process exited with code 1")
                break

            except:
                continue
