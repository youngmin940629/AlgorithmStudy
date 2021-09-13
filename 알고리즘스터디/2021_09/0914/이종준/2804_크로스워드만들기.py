'''
BANANA PIDZAMA
'''
data = list(input().split())
N = len(data[0])
M = len(data[1])
crossword = [['.'] * N for _ in range(M)]

idx_N = 0
idx_M = 0
breaker = False
# 구글링했음...이중 for문 탈출하는 방법 => 변수와 bool 활용
for i in range(N):
    for j in range(M):
        if data[0][i] == data[1][j]:
            idx_N = i
            idx_M = j
            breaker = True
            break
    if breaker:
        break

for i in range(N):
    crossword[idx_M][i] = data[0][i]
for j in range(M):
    crossword[j][idx_N] = data[1][j]

for i in range(M):
    for j in range(N):
        print(crossword[i][j], end='')
    print()