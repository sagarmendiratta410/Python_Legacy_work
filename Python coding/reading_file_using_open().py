
myfile = open('test.txt')      # WAY 2
content = myfile.read()
print(content)
print(len(content))
myfile.close()   # Always close your file so that it doesnt consume memory


with open("test.txt",mode="r") as mynewfile:   # WAY 3   # if you open any binary file such as pdf keep w as rb 
    contents2 = mynewfile.read()
    print(contents2)

with open("test.txt",mode="w") as mynewfile:       # if you open any binary file such as pdf keep w as wb
    contents1 = mynewfile.write("Adding new Line")
    print(contents1)