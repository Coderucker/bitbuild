from Sources.watchman.main import (DirectoryWatcher, FileWatcher)

def main():
    DirectoryWatcher("./").watch()


if __name__ == "__main__":
    main()