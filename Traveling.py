N = int(input())

t_list = [0]
x_list = [0]
y_list = [0]
A = 'Yes'

for i in range(N):
    ti, xi, yi = map(int, input().split())
    t_list.append(ti)
    x_list.append(xi)
    y_list.append(yi)
    if ((abs(x_list[i+1] - x_list[i]) + abs(y_list[i+1] - y_list[i]) > (t_list[i+1] - t_list[i]))):
        A = 'No'
        break
    if (x_list[i+1] + y_list[i+1] - t_list[i+1])%2 != 0:
        A = 'No'
        break

print(A)


'''
以下、考え方。

1<=i<=Nのiに対して
ti秒時点で、(xi, yi)にいることが可能が判定する

1回の試行を考えると、
t秒後に、(x,y)にいることが可能かどうかは、
①x+y<=tかどうか
②x+yとtの偶奇が一致するかどうか
で、判定できる。

ti時点で(xi, yi)にいることが可能かどうかは、
(x(i)-x(i-1))+(y(i)-y(i-1)) <= t(i) - t(i-1)かどうか
x(i)+y(i)とt(i)の偶奇が一致するか
で、判断できる

'''

