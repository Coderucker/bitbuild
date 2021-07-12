from lib.read_cache import read_cache
from lib.ignore_git import ignore_git
from internals.watchman.main import (DirectoryWatcher, FileWatcher)

read_cache()

def main():
    DirectoryWatcher("./").watch()

    # Making cache.txt file ignored by git
    ignore_git()

main()