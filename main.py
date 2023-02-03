import json
import os

path_to_file = os.environ['PATH_TO_FILE']

with open(path_to_file) as f:
	data = json.load(f)

print(data)
