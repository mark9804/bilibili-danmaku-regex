# coding:utf-8
import re


def generatexmlbyline(text):
    with open(generateFile, 'a') as file_xml:
        if re.search(r'\\|\^|\||\$|\*|\+|\?|\{|\}|\.|\(|\)|\[|\]|\\s', text) is not None:
            file_xml.write('\t<item enabled="true">r=' + text.strip('\n') + '</item>\n')
        else:
            file_xml.write('\t<item enabled="true">t=' + text.strip('\n') + '</item>\n')

textFile = 'B站弹幕屏蔽正则'
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
