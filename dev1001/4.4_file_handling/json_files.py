import json

with open('config.json') as f:
  data = json.load(f) # parses json into python dict/list
  print(f'Username: {data["username"]}')
  print(f'Recent files: {data["recent_files"][0]}')

# modifying the in-memory Python data structures
data['recent_files'].append('new_file.txt')

with open('updated_config.json', 'w') as f:
  json.dump(data, f, indent=4)