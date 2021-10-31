import sys; sys.stdin = open('SWEA_2817_부분수열합.txt', 'r')

def dfs(idx, sum):
    global cnt
    visited[idx] = 1
    sum += arr[idx]
    if sum == M:
        cnt += 1
    for i in range(idx,N):
        if not visited[i]:
            dfs(i, sum)
            visited[i] = 0

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    visited = [0] * N
    for i in range(N):
        dfs(i,0)
    print('#{} {}'.format(tc,cnt))
# for i in range(N):
#     ans += arr[i]
#     if ans == M:
#         cnt += 1
#     if ans !=  M:
#         ans -= arr[i]
#         continue