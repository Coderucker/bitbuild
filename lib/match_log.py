import re

def match_log(log):
    return re.search(":.*", log)