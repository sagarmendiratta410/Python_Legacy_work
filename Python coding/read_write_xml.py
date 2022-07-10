import xml.etree.ElementTree as ET   
tree = ET.parse('book.xml')   
root = tree.getroot()           
print(root.tag, root.attrib )

for child in root:                   
    print(child.tag, child.attrib)