import json

f = open('sample.json')

data = json.load(f)

with open("sample.json","r") as read_json:
    data = json.load(read_json)
    print(data)


print(" Data of Employees  \n", data['Employees'])
print(" Data of Employees  \n", data['Employees'][0]['name'])

print("\n Data of Employees \n" ,  data.get('Employees'))
print("\n key in dictionary " ,  data.keys())
print("\n Values of keys in dictionary " ,  data.values())
print("\n Data of Employees \n " ,  data.items())


print(type(data))

for i in data:
  print("Data of employees", i)

  
for i in data.values():
  print("Values of keys in dictionary",i)    

for i in data.values():
  print("Values of keys in dictionary",i[0]['name'])      

for i in data.keys():
  print("keys in dictionary", i)

for i,j in data.items():
    print("  keys and Values in dictionary", i[0],j) 

f.close()   