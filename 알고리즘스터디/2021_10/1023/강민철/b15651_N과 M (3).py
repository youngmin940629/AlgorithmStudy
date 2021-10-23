import sys;sys.stdin = open('15651.txt')

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = [0] * M

def power(n, m, k):
    if k == m:
        print(*ans)
    else:
        for i in range(N):
            ans[k] = arr[i]
            power(n, m, k+1)

power(N, M, 0)