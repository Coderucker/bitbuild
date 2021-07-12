import time
from datetime import datetime
from src.list_dir import list_dir
from src.iterate import iterate

class DirectoryWatcher:
    def __init__(self, directory) -> None:
        self.directory = directory

    def watch(self):
        print(f"{datetime.now()}: Watching out for changes")
        while(True):
            dir_content = list_dir(self.directory)

            time.sleep(0.35)

            if len(dir_content) != len(list_dir(self.directory)):
                comparison = list_dir(self.directory)
                print(f"""
{datetime.now()}: New File or Folder Removed or Created!    
{iterate(comparison)}
                """)
            else:
                print(f"{datetime.now()}: No Changes Detected!")