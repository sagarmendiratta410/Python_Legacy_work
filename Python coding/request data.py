import requests
import json



x = requests.get("https://automateinfra.com/")

print(x.status_code)


y = requests.post('https://httpbin.org/post', json={'id':1, 'roll':"spicy"})
print("Status code: ", y.status_code)
print(y.json())