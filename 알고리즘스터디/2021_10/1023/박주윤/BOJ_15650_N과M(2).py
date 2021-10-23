import sys; sys.stdin = open('BOJ_15650_N과M(2).txt', 'r')

def comb(k, start):
    global ans
    if k == m:
        ans+=(pick)
        return

    for i in range(start, n):
        pick.append(arr[i])
        comb(k + 1, i + 1)
        pick.pop()


n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
pick = []
ans = []

comb(0,0)
for i in range(0,len(ans),m):
    for j in range(m):
        print(ans[j+i], end=' ')
    print()




