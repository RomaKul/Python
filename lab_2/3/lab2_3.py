import xml.etree.ElementTree as ET
from collections import Counter

root = ET.Element("data")
child = ET.SubElement(root, "text")

a= open('a.txt')
q=a.read().split()
for i in range(0, len(q)):
    q[i]=q[i].rstrip('\n' '.' ',' ';')
cnt = Counter(q)

a.close()
for (word, count) in cnt.most_common():
    ET.SubElement(child,"Word").text = str(word)+ " appears: " + str(count) + " times"

tree = ET.ElementTree(root)
tree.write("2_2.xml", encoding='utf-8')