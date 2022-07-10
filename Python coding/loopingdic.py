
my_dic = {"a":{"b":{"c":"d"}}}

print(type(my_dic))

for i in my_dic:
  print(i)
  print(my_dic[i])
  
for i in my_dic.values():
  print(i)    
for i in my_dic.keys():
  print(i)

for i,j in my_dic.items():
    print(i,j) 