from xml.dom import minidom

mydoc = minidom.parse('items-gear.xml')

elements = mydoc.getElementsByTagName('element')

# print(elements.attributes['name'].value)

print(len(elements))

for element in elements:
    strItem = "<item id=\"" + element.attributes['id'].value + "_FORMULAE\">" + element.attributes['name'].value + "</item>"
    print(strItem)