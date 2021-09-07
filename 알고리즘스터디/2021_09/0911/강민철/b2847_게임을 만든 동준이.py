N = int(input())
arr = list()
for i in range(N):
    arr.append(int(input()))

res = 0
for i in range(N-2,-1,-1):
    if arr[i] >= arr[i+1]:
        res += arr[i]-arr[i+1]+1
        arr[i] -= arr[i]-arr[i+1]+1
print(res)