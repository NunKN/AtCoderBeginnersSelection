A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
a = min(A, X//500)
for i in range(a+1):
    b = min(B, (X - 500*i)//100) 
    for j in range(b+1):
        if (X - 500*i - 100*j)/50 <= C: 
            count+=1
print(count)


'''
�ȉ��A�l�����B

500x + 100y + 50z = X �ƂȂ�A(x, y, z)�̑g�ݍ��킹�̐������߂�
(x, y, z)�ɂ͐���������B
0 <= x <= A
0 <= y <= B
0 <= z <= C

a = min(A, X//500)�Ƃ��āA
500�~�̖����́A0~a

x = i (i��0~a)�̎��A
100y + 50z = X - 500i

b = min(B, (X - 500i)/100)�Ƃ��āA
100�~�̖����́A0~b

y = j(j��0~b)�̎��A
50z = X - 500i - 100u

(X - 500i - 100u)/50���AC�ȉ��ł��邩���d�v�B
if (X - 500i - 100j)/50�� < C:
	count+=1
'''

