from itertools import permutations

string = raw_input('Enter the string: ')

sender = dict()
for i in string:
	sender[i] = sender.get(i, 0) + 1
#print sender

#List of total permutation.
perms = list()
for k in [''.join(p) for p in permutations(string)]:
	if k not in perms:
		#perms.append(k)
		for i in range(0, len(string)):
			if k[i] == string[i]:
				continue
			else:
				perms.append(k)

print len(perms)
print 
#for i in perms:
#	if i not in reapeated:
#		#rearranged.append(i)
#		print  i
#		exit()
#	else:
#		continue
#if len(rearranged) == 0:
#	exit('Not possible')
#print 'Total possible valid rearrangements:',len(rearranged)
#print rearranged[0]