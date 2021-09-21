com = int(input())
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
course = [[0] * (com+1) for _ in range(com+1)]
result = 0
for idx in data:
    course[idx[0]][idx[1]] = course[idx[1]][idx[0]] = 1
S = [1]
visited = [0] * (com+1)
while S:
    v = S.pop()
    if not visited[v]:
        visited[v] = 1
        for t in range(1, com+1):
            if not visited[t] and course[v][t]:
                S.append(t)
for check in visited:
    if check == 1:
        result += 1
print(result - 1)