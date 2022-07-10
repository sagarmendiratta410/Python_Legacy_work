import json
data = { "key1": "value1", "key2": "value2" }

my_json = json.dumps(data, indent=4, separators=(",", " = "))
print(my_json)

object = {"a":{"b":{"c":"d"}}}
my_json2 = json.dumps(object, indent=4, separators=(",", " = "), key1="")
print(my_json2)