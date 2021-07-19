import os
import time
from datetime import datetime

from Sources.colormania.colormania import useColor
from Sources.lib.events.events import Events_File

class FileWatcher(Events_File):
    def __init__(self, config: list[str, str, str]) -> None:
        super().__init__()
        self.config = config

    def watch(self):
        red = "135"
        green = "73"
        blue = "23"

        # Out of the while loop to prevent printing on this message
        print(f"[{useColor(datetime.now(), red, green, blue)}] Watching out for changes in file -> {self.config[0]}")
        while True:
            started = False
            current_time = useColor(datetime.now(), red, green, blue)

            try:
                f = open(self.config[0]).read()

                time.sleep(0.35)

                started = True

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
                if started:
                    print(f"[{current_time}]: File was deleted -> {self.config[0]}")
                    break
                else:
                    print(f"[{current_time}]: File was not found -> {self.config[0]}")
                    print(f"Process Exited with code 1")
                    break
            except UnicodeDecodeError:
                    print(f"Failed to decode file {self.config[0]}")
                    break
            except:
                continue
        
        # Implement delete event here
        if not os.path.exists(self.config[0]):
            try:
                self.config[2]()
            except:
                # Pass if no delete event
                pass
