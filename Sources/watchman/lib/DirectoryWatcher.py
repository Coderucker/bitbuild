import time
from datetime import datetime

from Sources.colormania.colormania import useColor
from Sources.watchman.src.iterate import iterate
from Sources.watchman.src.list_dir import list_dir

class DirectoryWatcher:
    def __init__(self, config: list[str, str]) -> None:
        self.config = config[0]
        self.on_modified = config[1]

    def watch(self):
        current_time = useColor(datetime.now(), "255", "255", "200")

        print(f"[{current_time}]: Watching out for changes in folder -> {self.config}")
        while(True):
            try:
                dir_content = list_dir(self.config[0])

                time.sleep(0.35)

                if len(dir_content) != len(list_dir(self.config[0])):
                    print(f"""
[{current_time}]: New File or Folder Removed or Created! 
                    """)

                    # Call on_modified event
                    self.on_modified()
            except KeyboardInterrupt:
                exit()
            except FileNotFoundError:
                print(f"No file was found named: {self.file}")
            except:
                continue
