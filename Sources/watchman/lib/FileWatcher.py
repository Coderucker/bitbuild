import time
from datetime import datetime
from typing import Callable
from Sources.watchman.lib.events.events import Events_File
from Sources.watchman.src.remove_file import remove_file
from Sources.colormania.colormania import useColor

def log():
    print("Log")

class FileWatcher(Events_File):
    def __init__(self, file, modified_func) -> None:
        super().__init__(file)
        self.file = file
        self.modified_func = modified_func
    
    def watch(self):
        current_time = useColor(datetime.now(), "135", "73", "23")

        print(f"[{current_time}] Watching out for changes in file -> {self.file}")
        while(True):
            try:
                f = open(self.file).read()

                time.sleep(0.35)

                if open(self.file).read() != f:
                    # Printing the change
                    print(f"[{current_time}]: {self.file} -> File has Changes") 
                    
                    # Creating cache file
                    self.CACHE.generate_cache(f"[{datetime.now()}]: {self.file} -> File has Changes \n")

                    # Checking if modified func was defined
                    self.modified_func()
            except KeyboardInterrupt:

                exit()
            except FileNotFoundError:
                print(f"[{current_time}]: File was not found -> {self.file}")
                print("Process exited with code 1")
                break

            except: 
                continue