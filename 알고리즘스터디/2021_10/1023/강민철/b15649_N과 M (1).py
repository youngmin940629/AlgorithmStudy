import sys;sys.stdin = open('15649.txt')

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
used = [0] * N
ans = [0] * M

def perm(n, m, k):
    if k == m:
        print(*ans)
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                ans[k] = arr[i]
                perm(n, m, k+1)
                used[i] = 0

perm(N, M, 0)