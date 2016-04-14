#Read file and figure out the distribution by hour of the day for each of the messages
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hrs = dict()
for line in handle:
	line = line.rstrip()
	if line.startswith('From:'): continue
	elif line.startswith('From'):
		word = line.split()
		time  = word[5].split(':')
		#appending in dict
		hrs[time[0]] = hrs.get(time[0], 0) +1

#Sorting and printing
for key, value in sorted(hrs.items()):
	print key , value
