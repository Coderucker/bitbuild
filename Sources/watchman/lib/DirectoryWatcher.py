import time
from datetime import datetime
from Sources.watchman.src.iterate import iterate
from Sources.watchman.src.list_dir import list_dir
from Sources.watchman.src.remove_file import remove_file
from Sources.colormania.colormania import useColor

class DirectoryWatcher:
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
                exit()
            except FileNotFoundError:
                print(f"No file was found named: {self.file}")
            except:
                continue