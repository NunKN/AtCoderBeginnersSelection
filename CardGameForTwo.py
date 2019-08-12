N = int(input())
lstr_a = input().split(" ")
lint_a = [int(n) for n in lstr_a]
lint_a_sort = sorted(lint_a, reverse = True)

scoreAlice = 0
scoreBob = 0

for i in range(len(lint_a_sort)):
    if i % 2 == 0:
        scoreAlice += lint_a_sort[i]
    if i % 2 == 1:
        scoreBob += lint_a_sort[i]
print(scoreAlice - scoreBob)



'''
偶奇で場合分け
①入力をリストで受け取りソートする
②大きい順にソートして、基数番目がAliceの得点、偶数番目がBobの得点
'''

