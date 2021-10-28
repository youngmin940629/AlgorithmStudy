import sys; sys.stdin=open('BOJ_2798_블랙잭.txt', 'r')

N, M = map(int, input().split())

arr = list(map(int,input().split()))

s = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            ans = arr[i] + arr[j] + arr[k]
            s.append(ans)

max_ = 300000
for i in range(len(s)):
    if 0 <= M - s[i] <= max_:
        max_ = abs(s[i] - M)
        idx = i
print(s[idx])
# p=[0]*3
# v = [0]*N

# def comb(N, m, k):
#     if m == k:
#         print(p)
#         return
#     else:
#         for i in range(N):
#             if v[i] == 0:
#                 v[i] = 1
#                 p[k] = arr[i]
#                 comb(N,m,k+1)
#                 v[i]=0
# comb(N,3,0)