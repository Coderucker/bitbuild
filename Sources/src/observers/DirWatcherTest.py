import time
from datetime import datetime
from typing import Callable, Union
from subprocess import check_output
import random

from Sources.colormania.colormania import useColor
from Sources.src.list_dir import list_dir

class DirectoryWatcher:
    def __init__(self, config: list[str, str, str]) -> None:
        self.config = config[0]
        self.on_created = config[1]
        self.on_deleted = config[2]

    def watch(self):
        red = "255"
        green = "255"
        blue = "200"
        
        condition = 10

        print(f"[{useColor(datetime.now(), red, green, blue)}]: Watching out for changes in folder -> {self.config}")
        _condition = 0

        while condition != _condition:
            current_time = useColor(datetime.now(), red, green, blue)
            print("Condition: ", _condition)
            try:
                dir_content = list_dir(self.config)

                time.sleep(0.35)

                if _condition % 2 == 0:
                    dir_content.pop()
                elif _condition % 2 == 1:
                    dir_content.append(f"{random.random()}_file_text")

                if len(dir_content) < len(list_dir(self.config)):
                    print(f"""[{current_time}]: New File Created!""")

                    # Call on_created event
                    if type(self.on_created) == str:
                        print(check_output(self.on_created.split(" ")).decode("utf-8"))
                    else:
                        self.on_created()

                    # Increment Condition
                    _condition += 1
                elif len(dir_content) > len(list_dir(self.config)):
                    print(f"""[{current_time}]: One File has been Removed!""")

                    # Call deleted event
                    if type(self.on_created) == str:
                        print(check_output(self.on_deleted.split(" ")).decode("utf-8"))
                    else:
                        self.on_deleted()

                    # Increment Condition
                    _condition += 1
            except KeyboardInterrupt:
                exit()                
            except FileNotFoundError:
                print(f"No file was found named: {self.config}")
