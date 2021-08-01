from sys import exit

import time
from datetime import datetime
from typing import Callable, Union
from subprocess import check_output

from BitBuild.colormania.colormania import useColor
from BitBuild.src.iterate import iterate
from BitBuild.src.list_dir import list_dir
from BitBuild.src.get_unique import get_unique
from BitBuild.src.concat_array import concat_arrays

class DirectoryWatcher:
    def __init__(self, config: list[str, str, str]) -> None:
        self.config = config[0]
        self.on_created = config[1]
        self.on_deleted = config[2]

    def watch(self, condition: Union[bool, int]):
        red = "255"
        green = "255"
        blue = "200"

        # Function to call Callables
        def caller(callback: Callable):
            if type(callback) == str:
                print(check_output(callback.split(" ")).decode("utf-8"))
            else:
                callback()

        print(f"[{useColor(datetime.now(), red, green, blue)}]: Watching out for changes in folder -> {self.config}")

        if type(condition) == bool:
            while condition or True:
                current_time = useColor(datetime.now(), red, green, blue)
                try:
                    dir_content = list_dir(self.config)

                    time.sleep(0.35)

                    if len(dir_content) < len(list_dir(self.config)):
                        print(f"""[{current_time}]: New File Created!""")
                        
                        changes = useColor(
                            message=get_unique(concat_arrays(dir_content, list_dir(self.config))), 
                            red="255", 
                            green="145",
                            blue="67")
                        print(f"""Changes: {changes}""")

                        # Call on_created event
                        caller(self.on_created)

                    elif len(dir_content) > len(list_dir(self.config)):
                        print(f"""[{current_time}]: One File has been Removed!""")

                        changes = useColor(
                            message=get_unique(concat_arrays(dir_content, list_dir(self.config))), 
                            red="255", 
                            green="145",
                            blue="67")
                        print(f"""Changes: {changes}""")

                        # Call deleted event
                        caller(self.on_deleted)

                except KeyboardInterrupt:
                    exit()
                except NotADirectoryError:
                    print(f"Error: Provided targeted value {self.config} is not a directory")
                    exit()
                except FileNotFoundError:
                    print(f"No file was found named: {self.config}")
                    exit()
                except:
                    pass
        else:
            _condition = 0

            while condition != _condition:
                current_time = useColor(datetime.now(), red, green, blue)
                try:
                    dir_content = list_dir(self.config)

                    time.sleep(0.35)

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
                except:
                    pass
