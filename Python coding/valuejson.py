import json
samplejson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(samplejson)
print(data["key2"])