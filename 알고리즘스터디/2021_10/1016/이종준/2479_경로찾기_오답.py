# 시간초과 and 오답
# 뭔가 이상하다...다시해야할듯

import sys
sys.stdin = open('input.txt', 'r')


def dfs(v, target, k):
    global tmp
    if k >= tmp:
        return
    
    if v == target:
        if tmp > k:
            tmp = k
        for i in range(N + 1):
            if visited[i] == 1:
                tmp_list.append(i)

    visited[v] = 1
    for w in range(N + 1):
        if adj_list[v][w] == 1 and not visited[w]:
            dfs(w, target, k + 1)
    visited[v] = 0


N, K = map(int, input().split())
arr = []
arr.append([0] * K)
for _ in range(N):
    arr.append(list(map(int, input())))
A, B = map(int, input().split())

adj_list = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):    
    for j in range(1, N + 1):
        cnt = 0
        for k in range(K):
            if arr[i][k] != arr[j][k]:
                cnt += 1
        if cnt == 1:
            adj_list[i][j] = 1


tmp = 987654321
tmp_list = []
visited = [0] * (N + 1)

dfs(A, B, 0)

if not tmp_list:
    print(-1)
else:
    tmp_list.append(B)
    print(' '.join(map(str, tmp_list)))