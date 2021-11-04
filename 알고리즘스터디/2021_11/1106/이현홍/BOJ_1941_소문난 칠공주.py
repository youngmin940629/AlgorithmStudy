dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# n:선택한 자리 수 a: 파벌
def seat(n=1, a=1):
    if n == 7:
        if a > 3:
            tmp = S[:]
            tmp.sort()
            if not tmp in ans:
                ans.append(tmp)
    else:
        # 배열 S전체에 추가할 수 있는 경우의 수 찾기
        for s in S:
            r, c = s            
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < 5 and 0 <= nc < 5:
                    if V[nr][nc] == 0:
                        S.append((nr, nc))
                        V[nr][nc] = 1
                        seat(n+1, a+arr[nr][nc])
                        S.pop()
                        V[nr][nc] = 0



arr = [[0] * 5 for _ in range(5)]
for r in range(5):
    s = input()
    for c in range(5):
        if s[c] == 'S': arr[r][c] = 1

V = [[0]*5 for _ in range(5)]
S = []
ans = []

for r in range(5):
    for c in range(5):
        if arr[r][c] == 1:
            #시작점을 포함한 모든 경우의 수는 수행 완료 → 시작점은 V 초기화 안 함
            V[r][c] = 1
            S.append((r, c))
            seat()
            S.pop()

print(len(ans))