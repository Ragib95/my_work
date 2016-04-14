#rename files of folder
import os
import re
def rename_files():
	folder = raw_input('Enter location of folder: ')
	files =  os.listdir(folder)
	for i in files:
		name = re.findall('([a-z].+)', i)
		print name[0]

rename_files()	 
