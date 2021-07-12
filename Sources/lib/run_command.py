import subprocess
from Sources.lib.parse_config import (
  parse_config as parse
  )

def run_command(command):
  config = open(".auto-make.json").read()
  parsed = parse.parse_config(config)

  # Printing the status of the run
  print(f"Running command {command} -> {parsed[command]}")
  output = subprocess.run(parsed[command].split(" "), capture_output=True)

  return output.stdout.decode("utf-8")