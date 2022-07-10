import json

dictionary = {
    "name" : "sagar",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}


with open("sample.json","w") as opening_file:
    json.dump(dictionary,opening_file)