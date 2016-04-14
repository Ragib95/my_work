# Uses python2
a, b = map(int, raw_input().split())
#print a, type(b)
calc_fib = []
for i in range(0,a+1):
	calc_fib.append(0)
	if i <= 1:
		calc_fib[i] = i
	else:
		x = i-1
		y = i-2
		calc_fib[i] = calc_fib[x] + calc_fib[y]
print calc_fib[a] % b		