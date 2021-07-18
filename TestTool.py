#coding:utf-8

import regex

regexPlainText = 'B站弹幕屏蔽正则.txt'

matchCompiled = {}
matchPlainText = {}

with open(regexPlainText, 'r') as file_plaintext:
	lineNum = 1
	for line in file_plaintext:
		if line != '':
			matchCompiled[lineNum] = regex.compile(line.rstrip('\n'))
			matchPlainText[lineNum] = line.rstrip('\n')
		lineNum += 1

def testRegex(string):
	stringMatched = False
	result = []
	notInXmlList = []
	for key, value in dict.items(matchCompiled):
		if regex.match(value, string) is not None:
			stringMatched = True
			tempResult = '命中第' + str(key) + '条正则：' + str(matchPlainText[key])
			if regex.search(r'\(\?\<?\!', str(matchPlainText[key])) is not None:
				notInXmlList.append(str(key))
			else:
				tempResult += ''
			result.append(tempResult)
		else:
			pass
	if len(notInXmlList) != 0:
		for i in notInXmlList:
			result.insert(len(tempResult), str('第' + str(i) + '条正则不在XML文件中'))
	if stringMatched == False:
		result = ['该弹幕没有被正则捕获']
	return result

while True:
	testResult = testRegex(input('输入需要测试的弹幕：'))
	for i in testResult:
		print(i)
	print('')