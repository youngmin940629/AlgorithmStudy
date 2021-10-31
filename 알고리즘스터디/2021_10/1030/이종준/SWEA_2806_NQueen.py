dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs():
    

def queen(k):
    global ans

    if k == N:
        arr = [[0] * N for _ in range(N)]

        for j in range(N):
            arr[j][pick[j]] = 1

        visit = [[0] * N for _ in range(N)]

        for k in range(N):
            for l in range(N):
                if arr[k][l] == 1 and not visit[k][l]:
                    visit[k][l] = 1
                    # check()

        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        pick.append(i)
        queen(k + 1)
        pick.pop()
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * N
    pick = []
    ans = 0
    queen(0)
    print('#{} {}'.format(tc, ans))