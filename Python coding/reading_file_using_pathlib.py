import pathlib
from pprint import pprint


path = pathlib.Path("test.txt")  # WAY 1
cont = path.read_text()
cont1 = path.write_text("LOG:info")
print(cont)
print(cont1)

