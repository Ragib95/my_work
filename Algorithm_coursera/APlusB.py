# Uses python2

num = raw_input()
num = num.split()
a = int(num[0])
b = int(num[1])
if 0 <= a <= 9 and 0 <= b <= 9:
	print a + b
else:
	print 'error'