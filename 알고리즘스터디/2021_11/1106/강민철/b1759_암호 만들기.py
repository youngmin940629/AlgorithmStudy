import sys;sys.stdin = open('1759.txt')

L, C = map(int, input().split())
p = list(map(ord, input().split()))
p.sort()
p = list(map(chr, p))

st = {'a', 'e', 'i', 'o' ,'u'}

arr = [0] * L
def comb(n, r, k, s):
    if k >= r:
        cnt = 0
        for j in range(r):
            if arr[j] in st:
                cnt += 1
        if cnt >= 1 and r-cnt >= 2:
            print(''.join(arr))
        return
    for i in range(s, n-r+k+1):
        arr[k] = p[i]
        comb(n, r, k+1, i+1)

comb(C, L, 0, 0)