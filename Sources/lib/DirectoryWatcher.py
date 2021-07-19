import time
from datetime import datetime

from Sources.colormania.colormania import useColor
from Sources.src.iterate import iterate
from Sources.src.list_dir import list_dir

class DirectoryWatcher:
    def __init__(self, config: list[str, str]) -> None:
        self.config = config[0]
        self.on_created = config[1]
        self.on_deleted = config[2]
        self.on_modified = config[3]

    def watch(self):
        red = "255"
        green = "255"
        blue = "200"

        def _watch():
            current_time = useColor(datetime.now(), red, green, blue)
            try:
                dir_content = list_dir(self.config[0])

                time.sleep(0.35)

                if len(dir_content) < len(list_dir(self.config[0])):
                    print(f"""[{current_time}]: New File Created!""")

                    # Call on_created event
                    self.on_created()
                elif len(dir_content) > len(list_dir(self.config[0])):
                    print(f"""[{current_time}]: One File has been Removed!""")

                    # Call deleted event
                    self.on_deleted()
            except KeyboardInterrupt:
                exit()
            except FileNotFoundError:
                print(f"No file was found named: {self.config[0]}")
            except:
                pass

        print(f"[{useColor(datetime.now(), red, green, blue)}]: Watching out for changes in folder -> {self.config}")
        while True:
            _watch()
