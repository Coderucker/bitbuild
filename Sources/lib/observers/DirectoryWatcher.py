import time
from datetime import datetime
from typing import Union
from subprocess import check_output

from Sources.colormania.colormania import useColor
from Sources.src.iterate import iterate
from Sources.src.list_dir import list_dir

class DirectoryWatcher:
    def __init__(self, config: list[str, str, str]) -> None:
        self.config = config[0]
        self.on_created = config[1]
        self.on_deleted = config[2]

    def watch(self, condition: Union[bool, int]):
        red = "255"
        green = "255"
        blue = "200"

        print(f"[{useColor(datetime.now(), red, green, blue)}]: Watching out for changes in folder -> {self.config}")

        if type(condition) == bool:
            while condition or True:
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

                    elif len(dir_content) > len(list_dir(self.config)):
                        print(f"""[{current_time}]: One File has been Removed!""")

                        # Call deleted event
                        if type(self.on_created) == str:
                            print(check_output(self.on_deleted.split(" ")).decode("utf-8"))
                        else:
                            self.on_deleted()

                except KeyboardInterrupt:
                    exit()
                except FileNotFoundError:
                    print(f"No file was found named: {self.config}")
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
