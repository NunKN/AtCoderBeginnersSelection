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
�ȉ��A�l�����B

N = int(input())
A = int(input())
B = int(input())

N�͊��m
n = 0 - 1 �Ƃ���
n = a*10^4 + b*10^3 + c*10^2 + d*10^1 + e �Ə����B
a = (N)//10^4
b = (N - a*10^4)//10^3
c = (N - a*10^4 - b*10^3)//10^2
d = (N - a*10^4 - b*10^3 - c*10^2)//10^1
e = (N - a*10^4 - b*10^3 - c*10^2 - d*10^1)//10^0

a + b + c + d ��A - B�Ȃ�Acount+=1

'''

