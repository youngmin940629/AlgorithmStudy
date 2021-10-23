# 84 ms / 29200 KB

# 조합
N, M = map(int, input().split())
pick = []
arr = [i for i in range(1, N + 1)]

def comb(k, s):
    if k == M:
        print(' '.join(map(str, pick)))
        return
    
    for i in range(s, N):
        pick.append(arr[i])
        comb(k + 1, i)
        pick.pop()

comb(0, 0)