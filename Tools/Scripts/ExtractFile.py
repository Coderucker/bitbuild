import sys
import pathlib
import zipfile

args = sys.argv.copy()
# Removing first element which shows the python program path which we does not need :)
args.pop(0)

# Extract file
try:
    file_index = args.index("--file") + 1
except ValueError:
    print("No zip files specified to extract!")
    sys.exit()

try:
    file_exact_path = pathlib.Path(args[file_index]).absolute()

    with zipfile.ZipFile(args[file_index], 'r') as compressed_file:
        compressed_file.extractall()
    # Finish outputting file
except FileNotFoundError:
    print("ERROR: No files found named:", args[file_index])
except FileExistsError:
    print("ERROR: No files exists named:", args[file_index])