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
���ŏꍇ����
�@���͂����X�g�Ŏ󂯎��\�[�g����
�A�傫�����Ƀ\�[�g���āA��Ԗڂ�Alice�̓��_�A�����Ԗڂ�Bob�̓��_
'''

