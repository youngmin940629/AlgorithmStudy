def padoban(n):
    if n <= 5:
        arr = [0,1,1,1,2,2]
    else:
        arr = [0, 1, 1, 1, 2, 2] + [0] * (N - 5)
        for i in range(6, N+1):
            arr[i] = arr[i-1] + arr[i-5]
    return arr[n]

for tc in range(int(input())):
    N = int(input())
    print(padoban(N))