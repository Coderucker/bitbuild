import os
import time
from datetime import datetime
from lib.util.Cache import Cache

class FileWatcher:
    # Init cache class
    CACHE = Cache()
    def __init__(self, file) -> None:
        self.file = file
    
    def watch(self):
        print("Watching out for changes!")
        while(True):
            try:
                f = open(self.file).read()

                time.sleep(0.35)

                if open(self.file).read() != f:
                    # Printing the change
                    print(f"{datetime.now()}: {self.file} -> File has Changes") 
                    
                    # Creating cache file
                    self.CACHE.generate_cache(f"{datetime.now()}: {self.file} -> File has Changes \n")
            except KeyboardInterrupt:
                # Cleaning the log file
                self.CACHE.clean_cache()

                # Removing the cache file
                if os.path.exists(self.CACHE.cache_file):
                    os.remove(self.CACHE.cache_file)

                exit()
            except FileNotFoundError:
                print(f"No file named: {self.file}")
                break
            except: 
                continue

    def get_cache_data(self):
        return self.CACHE.get_cache_data()