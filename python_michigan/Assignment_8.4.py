#Read file and split it.

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
    lines = line.rstrip()
    word = lines.split()
    #print word
    for wd in word:
    	if wd in lst:
    		continue
    	lst.append(wd)
lst.sort()
print lst