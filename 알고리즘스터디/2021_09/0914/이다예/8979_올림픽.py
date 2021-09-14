import sys
sys.stdin = open('8979.txt', 'r')

N, K = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]
rank = 1

for i in range(N):
    if data[i][0] == K:
        idx = i

for j in range(N):
    if data[j][1] > data[idx][1]:
        rank += 1
    elif data[j][1] == data[idx][1]:
        if data[j][2] > data[idx][2]:
            rank += 1
        elif data[j][2] == data[idx][2]:
            if data[j][3] > data[idx][3]:
                rank += 1
print(rank)