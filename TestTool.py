#coding:utf-8

import regex
import os
import sys
import json

currentPath = os.path.realpath(__file__).rstrip('/TestTool.py')

regexPlainText = os.path.join(currentPath + '/B站弹幕屏蔽正则.txt')

def loadfile():
	global matchCompiled
	global matchPlainText
	with open(regexPlainText, 'r') as file_plaintext:
		lineNum = 1
		for line in file_plaintext:
			if line != '':
				matchCompiled[lineNum] = regex.compile(line.rstrip('\n'))
				matchPlainText[lineNum] = line.rstrip('\n')
			lineNum += 1

def initialize():
	global timeModified
	timeModifiedCheck = os.path.getmtime(regexPlainText)
	if timeModifiedCheck != timeModified:
		loadfile()
		timeModified = timeModifiedCheck
		print('正则文件已更新')
	else:
		pass

def testRegex(string, mode='single'):
	initialize() if mode == 'single' else False
	stringMatched = False
	result = []
	notInXmlList = []
	for key, value in dict.items(matchCompiled):
		if regex.search(value, string) is not None:
			stringMatched = True
			tempResult = '命中第' + str(key) + '条正则：' + str(matchPlainText[key])
			if regex.search(r'\(\?\<?\!', str(matchPlainText[key])) is not None:
				notInXmlList.append(str(key))
			else:
				tempResult += ''
			result.append(tempResult)
			matchedRules = len(result)
		else:
			pass
	if len(notInXmlList) != 0:
		for i in notInXmlList:
			result.insert(len(tempResult), str('第' + str(i) + '条正则不在XML文件中'))
	if stringMatched == False:
		matchedRules = 0
		if mode=='single':
			result = ['该弹幕没有被正则捕获']
		else:
			result = False
	return result, matchedRules


timeModified = os.path.getmtime(regexPlainText)

matchCompiled = {}
matchPlainText = {}

loadfile()
if len(sys.argv) == 1:
	while True:
		testString = input('输入需要测试的弹幕：')
		if testString != '':
			testResult, matched = testRegex(testString)
			for i in testResult:
				print(i)
			print('共命中' + str(matched) + '条正则\n')
		else:
			continue
else:
	danmakuPath = ''
	for i in sys.argv:
		if regex.search(r'.json$', i) is not None:
			matchingRules = {}
			danmakuPath = i
			print('正在分析' + danmakuPath + '：')
			with open(danmakuPath, 'r') as f:
				danmakus = f.read()
				f.close()
			jsonfile = json.loads(danmakus)
			for danmaku in jsonfile:
				testResult, matched = testRegex(danmaku['content'],mode='batch')
				if testResult is not False:
					matchingRules[danmaku['content']] = matched
			with open(os.path.join(currentPath + '/命中弹幕.csv'),'w') as f:
				f.write('弹幕内容,命中次数\n')
			with open(os.path.join(currentPath + '/命中弹幕.csv'),'a') as f:
				for key,value in dict.items(matchingRules):
					f.write(str(key.replace(',', '（英文逗号）')) + ',' + str(value) + '\n')
				f.close()
			print('共捕获' + str(len(matchingRules)) + '条弹幕；被捕获弹幕已移送至' + str(os.path.join(currentPath + '/命中弹幕.csv')))
	if danmakuPath == '':
		print('未找到需要分析的弹幕文件路径！')
		while True:
			testString = input('输入需要测试的弹幕：')
			if testString != '':
				testResult, matched = testRegex(testString)
				for i in testResult:
					print(i)
				print('共命中' + str(matched) + '条正则\n')
			else:
				continue