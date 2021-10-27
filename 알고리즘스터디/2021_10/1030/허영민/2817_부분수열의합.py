def partsum(st,a,b,check):
    global cnt
    if a == b:
        if check == K:
            cnt += 1
            return
        else:
            return
    if check >= K:
        return
    else:
        for i in range(st, len(data)):
            if not visited[i]:
                visited[i] = 1
                partsum(i, a+1,b,check+data[i])
                visited[i] = 0


for tc in range(int(input())):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = 0
    for count in range(1, len(data)-1):
        visited = [0] * len(data)
        partsum(0, 0,count,0)
    print('#{} {}'.format(tc+1, cnt))