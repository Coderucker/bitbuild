from os import TMP_MAX
import subprocess
import time
from util import (
  parse_config as parse, 
  read_config as read
  )

def run_command(command):
  config = read.read_config(".auto-make")
  parsed = parse.parse_config(config)

  print(f"[{time.time()}] Running command {command} -> {parsed[command]}")
  output = subprocess.run(parsed[command].split(" "), capture_output=True)
  return output.stdout.decode("utf-8")