from Sources.main import FileWatcher

def lof():
    exec("""
import sys 

print(f"Python version: {sys.version}")
""")


watcher = FileWatcher("test.txt", lof)

watcher.watch()