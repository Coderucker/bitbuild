import time
from Sources.lib.backened.LogApi import LogApi

while True:
    time.sleep(1)
    print(LogApi().get_api_data())