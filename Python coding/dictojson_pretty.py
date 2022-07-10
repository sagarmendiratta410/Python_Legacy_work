# In Python JSON exists as a String only
# Using the Python JSON module or so called package

import json
data = { "key1": "value1", "key2": "value2" }

my_json = json.dumps(data, indent=4, separators=(",", " = "))
print(my_json)
print(type(my_json))

