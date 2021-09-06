def BFS(V, n):
    visited[n] = 1
    for i in range(1, V+1):
        if arr[n][i] == 1 and visited[i] == 0:
            BFS(V, i)
            global cnt
            cnt += 1

V = int(input())
E = int(input())
arr = [[0] * (V+1) for _ in range(V+1)]

for i in range(1, E+1):
    r, c = map(int, input().split())
    arr[r][c] = arr[c][r] = 1

visited = [0] * (V+1)
cnt = 0
BFS(V,1)

print(cnt)
