from collections import deque

def bfs():
    global end
    while q:
        cd, rst = q.popleft()
        cnt1 = 0
        for idx in range(K):
            if cd[idx] != code[end-1][idx]:
                cnt1 += 1
        if cnt1 == 1:
            rst.append(end)
            return rst
        else:
            for i in range(1, N+1):
                if i not in rst:
                    tmp_rst = rst[:]
                    cnt = 0
                    for idx in range(K):
                        if cd[idx] != code[i-1][idx]:
                            cnt += 1
                    if cnt == 1:
                        tmp_rst.append(i)
                        q.append((code[i-1], tmp_rst))
    return -1



N, K = map(int, input().split())
code = []
for _ in range(N):
    code.append(input())
st, end = map(int, input().split())
result = [st]
q = deque()
q.append((code[st-1], result))
print(' '.join(map(str, bfs())))