import time
from datetime import datetime
from Sources.internals.watchman.lib.Cache import CACHE_FILE, Cache
from Sources.internals.watchman.src.iterate import iterate
from Sources.internals.watchman.src.list_dir import list_dir
from Sources.internals.watchman.src.remove_file import remove_file
from Sources.internals.colormania.colormania import useColor

class DirectoryWatcher:
    # Init cache class
    CACHE = Cache()
    def __init__(self, directory) -> None:
        self.directory = directory

    def watch(self):
        current_time = useColor(datetime.now(), "255", "255", "200")

        print(f"[{current_time}]: Watching out for changes in folder -> {self.directory}")
        while(True):
            try:
                dir_content = list_dir(self.directory)

                time.sleep(0.35)

                if len(dir_content) != len(list_dir(self.directory)):
                    comparison = list_dir(self.directory)
                    print(f"""
[{current_time}]: New File or Folder Removed or Created!    
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