def BFS(x, n=1):
    for i in range(N+1):
        if arr[x][i] == 1:
            if visited[i] == -1 or n < visited[i]:
                visited[i] = n
                BFS(i, n+1)

N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]

T1, T2 = map(int, input().split())
for e in range(int(input())):
    i, j = map(int, input().split())
    arr[i][j], arr[j][i] = 1, 1

visited = [-1] * (N+1)
BFS(T1)

print(visited[T2])