import json

path_to_file = input("Enter path to file: ")

with open(path_to_file) as f:
	data = json.load(f)

print(data)
