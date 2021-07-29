import json
from json.decoder import JSONDecodeError

def parse_config(config):
  try:
    parsed = json.loads(config)
    return parsed
  except JSONDecodeError:
    print("An Error Occured While Decoding")
    return
