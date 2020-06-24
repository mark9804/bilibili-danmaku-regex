# coding:utf-8
from re import search


def generatexmlbyline(text):
    with open(generateFile, 'a') as file_xml:
        if search(r'\\|\^|\||\$|\*|\+|\?|\{|\}|\.|\(|\)|\[|\]|\\s', text) is not None:
            file_xml.write('  <item enabled="true">r=' +
                           text.strip('\n') + '</item>\n')
        else:
            file_xml.write('  <item enabled="true">t=' +
                           text.strip('\n') + '</item>\n')


textFile = 'B站弹幕屏蔽正则.txt'
generateFile = 'B站弹幕屏蔽正则.xml'
with open(generateFile, 'w') as file_xml:
    file_xml.write("<filters>\n")

with open(textFile, 'r') as file_plaintext:
    for line in file_plaintext:
        generatexmlbyline(line)
    file_plaintext.close()

with open(generateFile, 'a') as file_xml:
    file_xml.write('</filters>')
    file_xml.close()
