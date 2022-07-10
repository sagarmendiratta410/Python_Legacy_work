import json

my_json = '''{
   "employee": [

      {
         "id": "01",
         "name": "Amit",
         "department": "Sales"
      },

      {
         "id": "04",
         "name": "sunil",
         "department": "HR"
      }
   ]
}'''

print(type(my_json))

dic = json.loads(my_json)
print(dic)
print(dic.items())
print(dic.values())
print(dic.keys())
print(dic['employee'])
print(dic.get('employee'))