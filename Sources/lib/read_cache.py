import os
from Sources.lib.match_log import match_log

def read_cache():
    if os.path.exists("cache.txt"):
        f = open("cache.txt")

        print(match_log(f.read()))