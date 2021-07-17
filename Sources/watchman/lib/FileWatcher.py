import time
from datetime import date, datetime
from Sources.watchman.lib.Cache import CACHE_FILE, Cache
from Sources.watchman.src.remove_file import remove_file
from Sources.colormania.colormania import useColor

class FileWatcher:
    # Init cache class
    CACHE = Cache()
    def __init__(self, file) -> None:
        self.file = file
    
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
            except KeyboardInterrupt:
                # Cleaning the log file
                self.CACHE.clean_cache()
                remove_file(CACHE_FILE)

                exit()
            except FileNotFoundError:
                # Cleaning the log file
                self.CACHE.clean_cache()
                remove_file(CACHE_FILE)
                
                print(f"No file named: {self.file}")
                break
            except: 
                # Cleaning the log file
                self.CACHE.clean_cache()
                remove_file(CACHE_FILE)
                    
                continue

    def get_cache_data(self):
        return self.CACHE.get_cache_data()