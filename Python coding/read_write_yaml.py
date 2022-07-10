import yaml
from pprint import pprint

with open('apache.yml', 'r') as new_file:
     verify_apache = yaml.safe_load(new_file)
pprint(verify_apache)

with open('apache.yml', 'w') as new_file2:
     verify_apache2 = yaml.dump(verify_apache, new_file2)
pprint(verify_apache2)
