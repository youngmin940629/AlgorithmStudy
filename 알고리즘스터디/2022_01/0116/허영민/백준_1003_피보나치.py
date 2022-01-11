def fibonachi(n):
    result[0][0] = 1
    result[1][1] = 1
    for i in range(2,n+1):
        result[i][0] = result[i-1][0] + result[i-2][0]
        result[i][1] = result[i-1][1] + result[i-2][1]

N = int(input())
for _ in range(N):
    n = int(input())
    if n >= 2:
        result = [[0,0] for _ in range(n+1)]
        fibonachi(n)
        print(result[n][0], result[n][1])
    elif n == 1:
        print("0 1")
    elif n == 0:
        print("1 0")