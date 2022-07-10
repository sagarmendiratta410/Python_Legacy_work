import pathlib
from pprint import pprint
path = pathlib.Path("test.txt")
cont = path.read_text()
cont1 = path.write_text("LOG:information technology")
print(cont)
# cont1 provides the number of indexes used in the text "LOG:information technology"
print(cont1)  