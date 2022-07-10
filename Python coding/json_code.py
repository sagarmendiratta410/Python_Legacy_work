import json
from pprint import pprint

with open('file.json', 'r') as opened_file:
    policy = json.load(opened_file) 
    pprint(policy)

policy['c'] = '3'  
pprint(policy)

with open('file.json', 'w') as opened_file1:
    policy2 = json.dump(policy, opened_file1)
pprint(policy2)

with open('file.json', 'r') as opened_file2: # Opens a Json File
    policy3 = json.load(opened_file2) 
    pprint(policy3)

