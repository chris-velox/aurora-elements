import re
import xml.etree.ElementTree as ET

with open(r'discipline_lists.txt', "r") as list_file:
    spell_list = list_file.readlines()

tree = ET.parse('manifestations.xml')
root = tree.getroot()

for spell_name in spell_list:
    find_string = ".//*[@name='" + spell_name.rstrip() + "']/supports"
    print(find_string)
    manifestation = root.find(find_string)
    manifestation.text = manifestation.text + ", Telepath"
    print(manifestation.text)
    
tree.write('output.xml')