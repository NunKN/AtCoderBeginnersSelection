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
�ȉ��A�l�����B

1<=i<=N��i�ɑ΂���
ti�b���_�ŁA(xi, yi)�ɂ��邱�Ƃ��\�����肷��

1��̎��s���l����ƁA
t�b��ɁA(x,y)�ɂ��邱�Ƃ��\���ǂ����́A
�@x+y<=t���ǂ���
�Ax+y��t�̋���v���邩�ǂ���
�ŁA����ł���B

ti���_��(xi, yi)�ɂ��邱�Ƃ��\���ǂ����́A
(x(i)-x(i-1))+(y(i)-y(i-1)) <= t(i) - t(i-1)���ǂ���
x(i)+y(i)��t(i)�̋���v���邩
�ŁA���f�ł���

'''

