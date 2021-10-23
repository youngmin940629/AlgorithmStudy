import sys;sys.stdin = open('15650.txt')

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = [0] * M

def comb(n, m, s, k):
    if k == m:
        print(*ans)
    else:
        for i in range(s, N-m+1+k):
            ans[k] = arr[i]
            comb(n, m, i+1, k+1)


comb(N, M, 0, 0)