N = int(input())
pop = [0] + list(map(int, input().split()))
arr = [[0]*(N+1) for _ in range(N+1)]

# arr, 양방향
for r in range(1,N+1):
    l = list(map(int, input().split()))
    for c in l[1:]:
        arr[r][c], arr[c][r] = 1, 1

# 기본 값 -1
result = -1

# BFS 단, 리스트 내의 값에서만 이동 가능
def bfs(s, e, lst):
    visited[s] = 1
    for i in range(1, N+1):
        if arr[s][i] == 1 and visited[i] == 0 and i in lst:
            if i == e:
                global flag
                flag = 1
            else: bfs(i, e, lst)

# 리스트 검증 함수
def vf(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            global visited, flag
            visited = [0] * (N+1)
            flag = 0
            bfs(lst[i], lst[j], lst)
            if flag == 0: return 0
    return 1


             
# 두 그룹으로 나누어 완전 탐색
L = []
R = []
def sc(n=2):
    if n == N+1:
        l = [1, ]       # 중복을 피하기 위해 1이 포함된 그룹은 항상 L그룹, 반대는 R 그룹
        r = []
        for i in range(2, N+1):
            if V[i] == 1: r.append(i)
            else: l.append(i)
        if r == []: return
        L.append(l)
        R.append(r)         # L과 R은 한 세트
    else:
        sc(n+1)
        V[n] = 1
        sc(n+1)
        V[n] = 0

if N == 2:
    print(abs(pop[1]-pop[2]))   # 선거구가 2개 뿐이면 바로 답 출력
else:
    V = [0] * (N+1)
    V[1] = 1
    sc()                        # 두 그룹으로 나누고

    for i in range(len(L)):
        if vf(L[i]) and vf(R[i]):       # L, R 쌍이 모두 유효하면
            sum_l, sum_r = 0, 0
            for l in L[i]:
                sum_l += pop[l]
            for r in R[i]:
                sum_r += pop[r]
            s = abs(sum_l-sum_r)
            if result == -1 or result > s:      # L그룹 인구 합과 R그룹 인구 합 구하기
                result = s
    print(result)