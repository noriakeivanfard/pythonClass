import xml.etree.ElementTree as ET
tree = ET.parse('file.xml')
root = tree.getroot()
for child in root.iter('child'):
    print(child.tag, child.attrib)
    
for element in root.iter('element'):
    print(element.text)

new_element = ET.SubElement(root, 'new_element')
new_element.text = 'book'
tree.write('output.xml')
