def parse_config(config):
  _ReturnConfig = []

  for configuration in config:
    _ReturnConfig.append(configuration.split("="))

  return _ReturnConfig