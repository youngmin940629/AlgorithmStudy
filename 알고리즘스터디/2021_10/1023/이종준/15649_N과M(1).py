# 232ms / 29200KB

N, M = map(int, input().split())
# 출력할 리스트
pick = []
# 방문체크
visited = [0] * (N + 1)

arr = [i for i in range(1, N + 1)]

def perm(k):
    if k == M:
        print(' '.join(map(str, pick)))
        return
    
    for i in range(N):
        if not visited[arr[i]]:
            visited[arr[i]] = 1
            pick.append(arr[i])
            perm(k + 1)
            visited[arr[i]] = 0
            pick.pop()

perm(0)