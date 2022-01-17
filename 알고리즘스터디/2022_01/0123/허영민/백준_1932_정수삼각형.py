n = int(input())
arr = []
result = []
for i in range(1,n+1):
    arr.append(list(map(int,input().split())))
    result.append([0]*i)
result[0][0] = arr[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            result[i][j] = result[i-1][j] + arr[i][j]
        elif j == i:
            result[i][j] = result[i-1][i-1] + arr[i][i]
        else:
            result[i][j] = arr[i][j] + max(result[i-1][j], result[i-1][j-1])
print(max(result[-1]))