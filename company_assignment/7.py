NM = list(raw_input())
N = int(NM[0])
M = int(NM[2])

arr = [0]*N
for i in range(0,M):
	abk = list(raw_input())
	a = int(abk[0]) - 1
	b = int(abk[2]) - 1
	k = int(abk[4])

	for j in range(a,b+1):
		arr[j] += k

print max(arr)