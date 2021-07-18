from Sources.watchman.lib.DirectoryWatcher import DirectoryWatcher
from main import DirectoryWatcher

def lof():
    exec("""
import sys 

print(f"Python version: {sys.version}")
""")

def lod():
    exec("""
print("Hello")
""")


watcher = DirectoryWatcher([
    "./",
    lof
])

watcher.watch()