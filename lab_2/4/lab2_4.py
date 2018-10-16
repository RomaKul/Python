import re
from collections import Counter
import xml.etree.ElementTree as ET

root = ET.Element("data")
child = ET.SubElement(root, "text")

a=open("a.txt").readlines()

mass=[]
tupl=[]
for i, line in enumerate(a,1):
  line =line.split()
  for j, word in enumerate(line,1):
    word=word.rstrip('\n' '.' ',' ';')
    mass.append(word[-3:])
    tupl.append((word, i, j))
cnt = Counter(mass)

text=''

for(end, count) in cnt.most_common():
  text +="end of word= {0} it appears {1} times ".format(end, count)
  pattern=r"(.)*{0}$".format(end)
  for (word, i, j) in tupl:
    if(re.match(pattern,word)):
      text+="(word= {0}, line= {1}, place= {2})".format(word, i, j)

  ET.SubElement(child,"").text = text



tree = ET.ElementTree(root)
tree.write("2_4.xml", encoding='utf-8')