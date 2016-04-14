#rename files of folder
import os
import re
def rename_files():
	folder = raw_input('Enter location of folder: ')
	file_list =  os.listdir(folder)
	os.chdir(folder)
	
	for i in file_list:
		name = re.findall('([a-z].+)', i)
		#print name
		#print os.getcwd()

		os.renames(i, name[0])

rename_files()