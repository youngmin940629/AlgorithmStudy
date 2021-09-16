import sys; sys.stdin = open('BOJ_1244_스위치끄고켜기.txt', 'r')

N = int(input())

arr = list(map(int, input().split()))
n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())

    if a == 1:
        for j in range(1, N//b + 1):
            arr[b * j - 1] += 1
            arr[b * j - 1] = arr[b * j - 1] % 2
    else:
        for k in range(b-1, -1, -1):
            if arr[-(N - b + 1) - k:-(N - b + 1) + k + 1] == arr[b - k - 1 : b + k]:
                for l in range(b-k-1, b+k):
                    arr[l] += 1
                break
    for j in range(N):
        arr[j] = arr[j] % 2
for i in range(N):
    print(arr[i], end=' ')