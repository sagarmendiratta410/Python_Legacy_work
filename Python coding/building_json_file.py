import json

dic = {"a":"a1","b":"b1"}

with open('file.json', 'w') as json_file:
   json.dump(dic,json_file,indent = 4, sort_keys=True)
print("Successfully converted the dictionary named dic into file.json")