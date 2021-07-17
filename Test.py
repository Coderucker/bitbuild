from Sources.watchman.lib.FileWatcher import FileWatcher
from main import FileWatcher

def lof():
    exec("""
import sys 

print(f"Python version: {sys.version}")
""")

def lod():
    exec("""
import sys

print(sys.path)
""")


watcher = FileWatcher([
    "./a.txt",
    lof
])

watcher.watch()