#Gives us permutation of the string such that no character appears in its original position.

from itertools import permutations

string = raw_input('Enter the string: ')

#List of total permutation.
perms = list()
for k in [''.join(p) for p in permutations(string)]:
	if k not in perms:
		perms.append(k)

#List of permutation with character appears in its original position.
reapeated = list()
for p in perms:
	for i in range(0, len(string)):
		if p[i] == string[i]:
			if p not in reapeated:
				reapeated.append(p)
		else:
			continue
	
#List of total permutation of the string such that no character appears in its original position.
for i in perms:
	if i not in reapeated:
		print  i
		exit()
	else:
		continue

print 'Not possible'