from main import (DirectoryWatcherTest, FileWatcherTest)

def dele():
    exec("""
print("Deleted")
""")

def adde():
    exec("""
print("Added")
""")

def mode():
    exec("""
print("Modified")
    """)

DirectoryWatcherTest([
    "./",
    adde,
    mode
]).watch()

FileWatcherTest([
    "./current_task",
    adde,
    "node -v"
]).watch()