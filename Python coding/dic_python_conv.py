import json
data = { "key1": "value1", "key2": "value2" }

print(data)
print(type(data))

my_json = json.dumps(data)
print(my_json)
print(type(my_json))
