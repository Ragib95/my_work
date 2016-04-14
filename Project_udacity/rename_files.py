#Rename file of folder.
import re

def rename_file(name):
	names = re.findall('([a-z].+)', name)
	return names

name = raw_input('Enter file name: ')
print rename_file(name)[0]	
