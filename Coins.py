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
以下、考え方。

500x + 100y + 50z = X となる、(x, y, z)の組み合わせの数を求める
(x, y, z)には制限がある。
0 <= x <= A
0 <= y <= B
0 <= z <= C

a = min(A, X//500)として、
500円の枚数は、0~a

x = i (iは0~a)の時、
100y + 50z = X - 500i

b = min(B, (X - 500i)/100)として、
100円の枚数は、0~b

y = j(jは0~b)の時、
50z = X - 500i - 100u

(X - 500i - 100u)/50が、C以下であるかが重要。
if (X - 500i - 100j)/50が < C:
	count+=1
'''

