N = int(input())
arr = [0] * (N+2)
arr[1], arr[2] = 1, 2

for i in range(3, N+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746

print(arr[N])