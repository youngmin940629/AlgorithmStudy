N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

visited = [0] * N

def func(cnt):
    for i in range(N):
        t = data[i][0]
        for j in range(i, i + t):
            if visited[j]:
                pass