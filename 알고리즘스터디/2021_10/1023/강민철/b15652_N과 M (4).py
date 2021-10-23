import sys;sys.stdin = open('15652.txt')

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = [0] * M

def mcomb(n, m, s, k):
    if k == m:
        print(*ans)
    else:
        for i in range(s, N):
            ans[k] = arr[i]
            mcomb(N, M, i, k+1)

mcomb(N, M, 0, 0)