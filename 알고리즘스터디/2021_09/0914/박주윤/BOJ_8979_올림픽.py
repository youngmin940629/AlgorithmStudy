import sys; sys.stdin = open('BOJ_8979_올림픽.txt', 'r')

N, M = map(int, input().split())
num = []
lst = []
cnt = 1
for _ in range(N):
    A, B, C, D = map(int, input().split())
    num.append(A)
    lst.append(1000001000001*B+1000001*C+D)

for i in range(N):
    if M == num[i]:
        idx = i
        break
for i in range(N):
    if lst[i] > lst[idx]:
        cnt += 1
print(cnt)