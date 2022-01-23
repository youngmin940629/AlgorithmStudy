import sys;sys.stdin = open('2565.txt')

def bin_search(arr, x):
    s, e = 0, len(arr)
    while s < e:
        mid = (s + e) // 2
        if arr[mid] < x:
            s = mid + 1
        else:
            e = mid
    return s

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = tuple(map(int, input().split()))

arr = list(map(lambda x:x[1], sorted(arr)))
dp = [0] * N
lis = [0]

for i in range(N):
    idx = bin_search(lis, arr[i])
    if idx >= len(lis):
        lis.append(arr[i])
    else:
        lis[idx] = arr[i]
    dp[i] = idx

print(N-max(dp))