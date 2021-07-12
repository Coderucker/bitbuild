import time
from datetime import datetime
from internals.watchman.lib.Cache import CACHE_FILE, Cache
from internals.watchman.src.iterate import iterate
from internals.watchman.src.list_dir import list_dir
from internals.watchman.src.remove_file import remove_file

class DirectoryWatcher:
    # Init cache class
    CACHE = Cache()
    def __init__(self, directory) -> None:
        self.directory = directory

    def watch(self):
        print(f"[{datetime.now()}]: Watching out for changes in folder -> {self.directory}")
        while(True):
            try:
                dir_content = list_dir(self.directory)

                time.sleep(0.35)

                if len(dir_content) != len(list_dir(self.directory)):
                    comparison = list_dir(self.directory)
                    print(f"""
    [{datetime.now()}]: New File or Folder Removed or Created!    
    {iterate(comparison)}
                    """)

                    self.CACHE.generate_cache(f"""
    [{datetime.now()}]: New File or Folder Removed or Created!    
    {iterate(comparison)}
                    """)
            except KeyboardInterrupt:
                # Cleaning the cache file
                self.CACHE.clean_cache()
                remove_file(CACHE_FILE)
    
                exit()
            except FileNotFoundError:
                # Cleaning the cache file
                self.CACHE.clean_cache()
                remove_file(CACHE_FILE)

                print(f"No file named: {self.file}")
            except:
                # Cleaning the cache file
                self.CACHE.clean_cache()
                remove_file(CACHE_FILE)

                continue