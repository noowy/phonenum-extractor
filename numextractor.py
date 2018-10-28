# -*- coding: utf-8 -*-
import sys
import re

def extractNums(filename):
	textFile = str(open(filename).read())
	pattern = r"(?:\+7|8)[0-9\s\-\(\)]{10,16}"
	phone_re = re.compile(pattern)
	numbers = phone_re.findall(textFile)
	return numbers

def printExtractedNums(filename):
	numbers = extractNums(filename)
	pattern = r"(?:\+7|8)(?:(?:\s|\(|\s\()([0-9]{3})(?:\s|\))|([0-9]{3}))"
	code_re = re.compile(pattern)
	pattern = r"(?:(?:\s|\(|\s\()([0-9]{3})(?:\s|\))|([0-9]{3}))"
	code_dict_re = re.compile(pattern)
	phone_codes = unicode(open("C:\\Homemade Software\\Python\\phone_codes.txt").read())
	output_string1 = u""
	output_string2 = u""
	start_pos = 29
	mark = 0
	for i in range (0, len(numbers)):
		code = code_re.findall(numbers[i])
		for j in range (0, len(phone_codes)):
			if code[0][0] == phone_codes[j:j+3] or code[0][1] == phone_codes[j:j+3]:
				output_string1 = numbers[i]
				output_string2 = phone_codes[start_pos:j]
				start_pos = j + 3
				mark = 1
				break 
			elif code_dict_re.search(phone_codes[j:j+3]):
				start_pos = j + 3
		if mark == 0:
			print u"Код данного номера не соответствует кодам операторов"
			continue
		print output_string2 + output_string1
		mark = 0 
	return 0

def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')
	if len(sys.argv) != 3:
		print 'usage: ./labwork5.py --extract filename'
		sys.exit(1)

	option = sys.argv[1]
	filename = sys.argv[2]
	if option == '--extract':
		printExtractedNums(filename)
	else:
		print 'unknown option: ' + option		
		sys.exit(1)

if __name__ == '__main__':
	main()