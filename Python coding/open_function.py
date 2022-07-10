myfile = open('test.txt')
content = myfile.read()
print(content)
print(len(content))
myfile.close()   # Always close your file so that it doesnt consume memory