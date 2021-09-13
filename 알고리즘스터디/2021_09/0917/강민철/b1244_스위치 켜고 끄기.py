L = int(input())
arr = list(map(int ,input().split()))
N = int(input())
for _ in range(N):
    s, n = map(int, input().split())
    if s == 1:
        for i in range(n-1, L):
            if (i+1) % n == 0:
                arr[i] = int(not arr[i])
    else:
        arr[n-1] = int(not arr[n-1])
        l = r = n-1
        while l-1 >=0 and r+1 < L:
            l -= 1
            r += 1
            if arr[l] == arr[r]:
                arr[l] = int(not arr[l])
                arr[r] = int(not arr[r])
            else:
                break

nn = L
m = 0
while L > 0:
    L -= 20
    print(*arr[m:m+20])
    m += 20