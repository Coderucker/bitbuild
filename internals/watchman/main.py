from lib.DirectoryWatcher import DirectoryWatcher
from lib.FileWatcher import FileWatcher

watcher = FileWatcher("./tests/test.py")

FileWatcher.watch(watcher)