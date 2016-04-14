# Uses python2
num = [int(i) for i in raw_input().split()]
a = max(num[0],num[1])
b = min(num[0],num[1])		
#print a, b
while b > 0:
	c = a % b
	a = b
	b = c
print a	