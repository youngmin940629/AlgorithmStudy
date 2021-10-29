def queen(visit, x):
    global cnt
    if x == N:
        cnt += 1
        return
    for col in range(N):
        visit[x] = col
        for i in range(x):
            if visit[i] == visit[x]:
                break
            if abs(visit[i] - visit[x]) == (x-i):
                break
        else:
            queen(visit, x+1)



for tc in range(int(input())):
    N = int(input())
    cnt = 0
    visit = [0] * N
    queen(visit, 0)
    print('#{} {}'.format(tc+1,cnt))