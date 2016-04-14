# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    a = line.find(":")
    num = line[a+1:]
    num = float(num)
    total = total + num
    count = count + 1    
print "Average spam confidence:",total / count
