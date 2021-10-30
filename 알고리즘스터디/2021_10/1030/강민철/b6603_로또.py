import sys;sys.stdin = open('6603.txt')

def comb(n, m, s, k):
    if k == m:
        print(*ans)
    else:
        for i in range(s, n-m+1+k):
            ans[k] = arr[i+1]
            comb(n, m, i+1, k+1)

while True:
    arr = list(map(int, input().split()))
    if not arr[0]: break
    K = arr[0]
    ans = [0] * 6
    comb(K, 6, 0, 0)
    print()