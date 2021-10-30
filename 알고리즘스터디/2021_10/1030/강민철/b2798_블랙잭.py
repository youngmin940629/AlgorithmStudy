import sys;sys.stdin = open('2798.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
minimum = 0
for i in range(3):
    minimum += arr[i]

def comb(n, m, s, k, sumation):
    global minimum
    if sumation > M:
        return
    if k == m:
        if sumation <= M and (sumation-M)**2 < (minimum-M)**2:
            minimum = sumation
    else:
        for i in range(s, n-m+1+k):
            sumation += arr[i]
            comb(n, m, i+1, k+1, sumation)
            sumation -= arr[i]

comb(N, 3, 0, 0, 0)
print(minimum)