# 1744ms / 29200KB

N, M = map(int, input().split())
# 출력할 리스트
pick = []

arr = [i for i in range(1, N + 1)]

def perm(k):
    if k == M:
        print(' '.join(map(str, pick)))
        return
    
    for i in range(N):
        pick.append(arr[i])
        perm(k + 1)
        pick.pop()

perm(0)