input_list = input().split(' ')
N = int(input_list[0])
Y = int(input_list[1])
A = None
flag = False
for x in range(N+1):
    for y in range(N+1-x):
        if 10000*x + 5000*y + 1000*(N-x-y) == Y:
            A = str(x) + " " + str(y) + " " + str(N-x-y)
            print(A)
            flag = True
    if flag:
        break
if A is None:
    A = '-1 -1 -1'
    print(A)


'''
考え方。
単純に、(x, y, z)の全パターンをループして、Y円になればその組み合わせを出力するようにする。
'''
