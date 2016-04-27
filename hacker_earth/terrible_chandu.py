def rev_of_str(string):
	S = len(string)
	arr = [None]*S
#	print len(arr)
	for i in string:
		S = S - 1
		arr[S] = i
	print ''.join(arr)
	
T = int(raw_input())
for i in range(T):
	rev_of_str(raw_input())