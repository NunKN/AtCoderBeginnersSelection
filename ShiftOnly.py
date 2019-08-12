N = int(input())
A = map(int, input().split(" "))
count = 0
flag = False
while True:
	for i in range(N):
		if A[i] % 2 == 0:
			A[i] //= 2
		else :
			print(count)
			flag = True
			break
	count += 1
	if flag:
		break

