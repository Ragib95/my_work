#Finding Numbers in a Haystack

import re
head = raw_input('Enter file name: ')
files = open(head)
total = 0
count = 0
for line in files:
	line = line.rstrip()
	#print line
	number = re.findall(('[0-9]+'), line)
	#print number
	for num in number:
		num = int(num)
		total = total + num
		count = count + 1
print total, count
