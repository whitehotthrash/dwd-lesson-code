# Task: Read updated_config.json. Change the theme to "light" and add a new
#       key-value pair "font_size": 12. Write this modified data to a new
#       file user_prefs.json.

import json

with open('updated_config.json') as f:
  data = json.load(f) 

data['theme'] = 'light'
data['font_size'] = '12'

with open('user_prefs.json', 'w') as f:
  json.dump(data, f, indent=4)