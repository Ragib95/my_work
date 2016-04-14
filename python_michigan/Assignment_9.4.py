#Read file and figure out greatest no of mail sent by whom.
name = raw_input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)
sender = dict()

#make full dictionary with email key and its no. of occurence.
for line in handle:
	line = line.rstrip()
	if line.startswith('From:'): continue
	if line.startswith('From'):
		words = line.split()
		sender[words[1]] = sender.get(words[1], 0) + 1

#find largest occurence of email id in dict.
highest_value = None
highest_key = None
for key,value in sender.items():
	if value == None or value > highest_value:
		highest_value = value
		highest_key = key

print highest_key, highest_value