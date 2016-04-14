sentence = raw_input()
new = ''
for word in sentence:
	#if word != '.' and word != ' ' and word != 'y' and word !='z' :
	#	word = chr(ord(word) + 2)
	#new = new + word
	if word == 'y':
		word = 'a'
		new = new + word
	elif word == 'z':
		word = 'b'
		new = new + word	
	elif word == '.' or word == ' ' or word == "'" or word=='(' or word==')':
		new = new + word
	else:
		word = chr(ord(word) + 2)
		new = new + word
print '\n', new
