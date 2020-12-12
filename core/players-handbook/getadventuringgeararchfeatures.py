import xml.etree.ElementTree as ET
tree = ET.parse('items-gear.xml')
root = tree.getroot()

for element in root.iter('element'):
    itemName = element.get('name')
    itemId = element.get('id')
#    print(itemName, itemId)
    itemSetter = element.find("./setters/set[@name='cost']")
    itemCost = itemSetter.text
    itemCurrency = itemSetter.get('currency')
    # itemCostCurrency = itemCostInfo.get('currency')
#    print(itemCost, itemCurrency)

    
    strItem = "<element type=\"Archetype Feature\" name=\"" + itemName + "\" source=\"Player’s Handbook\" id=\"" + itemId + "_FORMULAE\">"
    strItem = strItem + "\n\t<supports>Favored Formulae Item</supports>"
    strItem = strItem + "\n\t<description />"
    strItem = strItem + "\n\t<sheet><description>Cost: " + itemCost + itemCurrency + "</description></sheet>"
    strItem = strItem + "\n</element>"
    print(strItem)