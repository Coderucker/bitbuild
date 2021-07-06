from util import parse_conf

def parse_config(config):
  _config = parse_conf.parse_config(config)

  ReturnConfig = {}

  for configuration in _config:
    ReturnConfig[configuration[0]] = configuration[1]
  
  return ReturnConfig