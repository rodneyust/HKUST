# -*- coding: utf8 -*-
#(a)
import os
import re
from lxml import etree
xml = etree.parse("blocklist.xml")
os.getcwd()
os.chdir("E:\\下载")
file_object = open('blocklist.xml','r')
a = file_object.readlines()
for i in a:
    if re.search(r'blockID="i.+[0-9]"',i)!=None or re.search(r'block="g.+[0-9]"',i)!=None:
      print(i)
#(b)
for i in a:
    if re.search(r'id=".+@.+"',i)!=None:
     result=re.search(r'id=".+@.+"',i).group(0)
     if "^" not in result and "/" not in result and "\\" not in result:
       print(i)
# root = xml.getroot()
# print(root)
# print(root.items())
# print(root.keys())
# print(root.get('lastupdate', ''))
# node= root.getchildren()
# print(node)

# with open('blocklist.xml','r') as f:
#     content = ''.join([i.strip() for i in f.readlines()])
# matches = re.findall('(?:>\n\s+)(.+\s+/>)', content)
# matches1 = re.findall('[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+ -]+(\.[a-zA-Z0-9_-]+)+',content )
# print(matches)
# print(matches1)
# print(xml.xpath('//emItems'))
# for node in root.xpath('//emItems'):
#     print(node.text)
# for emItems in root.xpath('//emItems'):
#     for corner in emItems.getchildren():
#         print(corner.text)
#for emItems in xml.xpath('//emItems'):

