object1 = {"a":{"b":{"c":"d"}}}
# key = a/b/c
object2 = {"x":{"y":{"z":"a"}}}
# key = x/y/z
# value = a


import json

print(type(object1))
print(type(object1['a']))


print("\n Value of key a is " ,  object1['a'])
print("\n Value of key a is " ,  object1.get('a'))
print("\n key in dictionary " ,  object1.keys())
print("\n Values of keys in dictionary " ,  object1.values())
print("\n key in dictionary " ,  object1.items())
print("\n Value of key b is " ,  object1['a']['b'])
print("\n Value of key c is " +  object1['a']['b']['c'])