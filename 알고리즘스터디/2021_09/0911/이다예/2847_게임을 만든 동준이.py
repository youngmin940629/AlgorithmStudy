import sys
sys.stdin = open('2847.txt', 'r')

N = int(input())
s_list = []
for i in range(N):
    score = int(input())
    s_list.append(score)

cnt = 0
for j in range(N-2, -1, -1):
    if s_list[j] >= s_list[j+1]:
        cnt += s_list[j] - s_list[j+1] + 1
        s_list[j] -= s_list[j] - s_list[j+1] + 1
print(cnt)
