#TEST - Life, the Universe, and Everything
A = []
while True:
	num = int(raw_input())
	if 0 <= num < 100:
		if num == 42:
			break
		else:
			A.append(num)
	else:
		error

for i in A:
	print i