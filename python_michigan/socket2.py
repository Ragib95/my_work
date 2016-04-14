import urllib
import re
fhand = urllib.urlopen('http://www.py4inf.com')

for line in fhand:
	line = line.strip()
	add = re.findall('(http:).+\S', line)
	print add
