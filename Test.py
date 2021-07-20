from main import DirectoryWatcher

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


watcher = DirectoryWatcher([
    "./",
    adde,
    "python --version"
])

watcher.watch(True)