from Sources.watchman.lib.FileWatcher import FileWatcher

from main import FileWatcher

def lof():
    exec("""
import sys 

print(f"Python version: {sys.version}")
""")

def lod():
    exec("""
print("Hello")
""")


watcher = FileWatcher([
    "./a.txt",
    lof,
    lod
])

watcher.watch()