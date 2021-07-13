"""
This is a programmatical way to access the cache log data
"""

import os

CACHE_FILE = "cache.txt"

class LogApi():
    def __init__(self) -> None:
        if os.path.exists(CACHE_FILE):
            self.api_data = open(CACHE_FILE).read()
        else:
            self.api_data = "NULL"
    
    def get_api_data(self):
        return self.api_data.split("\n")