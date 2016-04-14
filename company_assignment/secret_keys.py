#John works in the cyber security cell. 
#He wants to generate secret keys following a pattern. 
#The pattern consists of the characters 'X' and 'Y'
#where X means increasing and 'Y' means decreasing. 
#Help him devise an algorithm to generate the secret 
#key which is the minimum number encoded following that pattern.
pattern = raw_input('Enter the pattern: ')
#Restriction due to digits can't repeat
if len(pattern) > 8: 
	exit('error! pattern length exceeded 8 char')

count = 1
j = 0
keys = ['1']
#Generate secret key
for i in pattern:
	if i == 'Y':
		count += 1
		keys[j] = str(count) + keys[j]
	elif i == 'X':
		keys.append(None)
		count += 1
		j += 1
		keys[j] = str(count)
		continue
	#Error if pattern contain other than X & Y.
	else:
		exit('error! re-check pattern')
		
secret_keys = ''.join(keys)
print int(secret_keys)