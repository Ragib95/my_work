# Uses python2
n = int(raw_input())
a = [int(x) for x in raw_input().split()]
assert(len(a) == n)

#result = 0

#for i in range(0, n):
#    for j in range(i+1, n):
#        if a[i]*a[j] > result:
#            result = a[i]*a[j]

#print result
max1 = 0
max2 = 0
for i in a:
	if i > max1:
		max1 = i

a.remove(max1)
for i in a:
	if i > max2:
		max2 = i		
#print max1
#print a
#print max2

print max1*max2