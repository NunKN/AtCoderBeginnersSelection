Num = int(input())
ld = []
for i in range(Num):
    ld.append(int(input()))
ld_set = list(set(ld))
print(len(ld_set))


"""
考え方。
重複をなくして数を数える
"""