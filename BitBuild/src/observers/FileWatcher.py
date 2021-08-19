# Importing exit() function from sys module to avoid TypeError in the executable build by Pyinstaller 
from sys import exit

import os
import time
from datetime import datetime
from typing import Union
from subprocess import check_output

from BitBuild.colormania.colormania import useColor
from BitBuild.src.events.events import Events_File

class FileWatcher(Events_File):
    """
    API used by BitBuild to watch and detect changes inside files
    """

    def __init__(self, config: list[str, str, str]) -> None:
        super().__init__()
        self.config = config[0]
        self.on_modified = config[1]
        self.on_deleted = config[2]

    def watch(self, condition: Union[bool, int, None]):
        exit_code = 0
        red = "135"
        green = "73"
        blue = "23"

        def caller(callback):
            if type(callback) == str:
                print(check_output(callback.split(" ")).decode("utf-8"))
            else:
                callback()

        def _watch():
            if type(condition) == bool:
                while condition or True:
                    started = False
                    current_time = useColor(datetime.now(), red, green, blue)

                    try:
                        f = open(self.config).read()

                        time.sleep(0.35)

                        started = True

                        if open(self.config).read() != f:
                            # Printing the change
                            print(f"[{current_time}]: {self.config} -> File has Changes")

                            # calling action func
                            caller(self.on_modified)
                    except KeyboardInterrupt:
                        exit_code = 0
                        exit()
                    except FileNotFoundError:
                        if started:
                            print(f"[{current_time}]: File was deleted -> {self.config}")
                            exit_code = 0
                            break
                        else:
                            print(f"[{current_time}]: File was not found -> {self.config}")
                            print(f"Process exited with code 1")
                            break
                    except UnicodeDecodeError:
                            print(f"Failed to decode file {self.config}")
                            exit_code = 1
                            break
                    except PermissionError:
                        print(f"Permission denied to access file -> {self.config}")
                        break
                    except:
                        continue
            else: 
                _condition = 0
                # Until a condition
                while condition != _condition:
                    started = False
                    current_time = useColor(datetime.now(), red, green, blue)

                    try:
                        f = open(self.config).read()

                        time.sleep(0.35)

                        started = True

                        if open(self.config).read() != f:
                            # Printing the change
                            print(f"[{current_time}]: {self.config} -> File has Changes")

                            # calling action func
                            caller(self.on_modified)

                            # Increment _condition
                            _condition += 1
                    except KeyboardInterrupt:
                        exit_code = 0
                        exit()
                    except FileNotFoundError:
                        if started:
                            print(f"[{current_time}]: File was deleted -> {self.config}")
                            exit_code = 0
                            break
                        else:
                            print(f"[{current_time}]: File was not found -> {self.config}")
                            print(f"Process exited with code 1")
                            break
                    except UnicodeDecodeError:
                            print(f"Failed to decode file {self.config}")
                            exit_code = 1
                            break
                    except PermissionError:
                        print(f"Permission denied to access file -> {self.config}")
                        break
                    except:
                        continue

        # Out of the while loop to prevent printing on this message
        print(f"[{useColor(datetime.now(), red, green, blue)}] Watching out for changes in file -> {self.config}")
        # Start Watching
        _watch()
        
        # Implement delete event here
        if not os.path.exists(self.config):
            try:
                caller(self.on_deleted)
            except:
                # Pass if no delete event
                pass

        print(f"Process exited with code {exit_code}")
