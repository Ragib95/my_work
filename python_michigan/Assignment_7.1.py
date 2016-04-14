#Read file and print in uppercase
fname = raw_input("Enter file name: ")
fh = open(fname)
fh = fh.read()
fupper = fh.upper()
fupper = fupper.rstrip()
print fupper