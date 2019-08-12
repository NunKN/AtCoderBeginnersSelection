in = input()
l_str_in = in.split(" ")
N = int(l_str_in[0])
A = int(l_str_in[1])
B = int(l_str_in])
count = 0
for n in range(N+1):
	a = (n)//10**4
	b = (n - a*10**4)//10**3
	c = (n - a*10**4 - b*10**3)//10**2
	d = (n - a*10**4 - b*10**3 - c*10**2)//10**1
	e = (n - a*10**4 - b*10**3 - c*10**2 - d*10**1)//10**0
	SUM = a + b + c + d + e
	if (SUM>=A and SUM<=B):
		count += n
print(count)


'''
以下、考え方。

N = int(input())
A = int(input())
B = int(input())

Nは既知
n = 0 - 1 として
n = a*10^4 + b*10^3 + c*10^2 + d*10^1 + e と書く。
a = (N)//10^4
b = (N - a*10^4)//10^3
c = (N - a*10^4 - b*10^3)//10^2
d = (N - a*10^4 - b*10^3 - c*10^2)//10^1
e = (N - a*10^4 - b*10^3 - c*10^2 - d*10^1)//10^0

a + b + c + d がA - Bなら、count+=1

'''

