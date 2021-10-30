import sys;sys.stdin = open('2817.txt')

def solve(n, s, r):
    global cnt
    if r > K:
        return
    if r == K:
        cnt += 1
    for i in range(s, n):
        r += arr[i]
        solve(n, i+1, r)
        r -= arr[i]

for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    solve(N, 0, 0)
    print(f'#{tc+1} {cnt}')