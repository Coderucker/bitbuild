from main import FileWatcher

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


watcher = FileWatcher([
    "./current_task",
    adde,
    "node -v"
])

watcher.watch(3)
