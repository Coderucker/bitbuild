from lib.util.parse_cache import parse_cache
from src.constants import CACHE_FILE

class Cache:
    def __init__(self) -> None:
        self.cache_file = CACHE_FILE

    def generate_cache(self, text):
        f = open(self.cache_file, "a")

        return f.write(text)
    
    def clean_cache(self):
        f = open(self.cache_file, "w")

        return f.write("")

    def get_cache_data(self) -> list:
        f = open(self.cache_file).read()

        return parse_cache(f)