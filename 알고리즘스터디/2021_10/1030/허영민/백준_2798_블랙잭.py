N, M = map(int, input().split())
arr = list(map(int,input().split()))
result = 0
visited = [0] * N
def black(x, check):
    global result
    if check > M:
        return
    if x == 3:
        if (M - check) >= 0 and check >= result:
            result = check
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                black(x+1,check+arr[i])
                visited[i] = 0
black(0,0)
print(result)