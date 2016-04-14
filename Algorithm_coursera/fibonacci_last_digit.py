# Uses python2
n = int(raw_input())
calc_fib = []
for i in range(0,n+1):
	calc_fib.append(0)
	if i <= 1:
		calc_fib[i] = i
	else:
		a = i-1
		b = i-2
		calc_fib[i] = (calc_fib[a] + calc_fib[b]) % 10
print calc_fib[n] % 10		