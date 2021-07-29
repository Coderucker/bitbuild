import json
from json.decoder import JSONDecodeError

def parse_config(config) -> json.loads:
  try:
    parsed: json.loads = json.loads(config)
    return parsed
  except JSONDecodeError:
    print("An Error Occured while decoding JSON File")
    return
