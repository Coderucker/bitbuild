def read_config(path):
  data = open(path).read()

  return data.split("\n")