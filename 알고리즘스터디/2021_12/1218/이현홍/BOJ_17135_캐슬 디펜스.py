import sys
sys.stdin = open('s.txt', 'r')

N, M, D = map(int, input().split())
arr = [0] * N

# 인덱스 사용 쉽게끔 배열 순서 반대로 
for n in range(N-1, -1, -1):
    arr[n] = tuple(map(int, input().split()))

archer = []
V = []

# 궁수 위치 배열 archer에 추가
def sc(n=0, s=0):
    if n == M:
        if s == 3:
            archer.append(V[:])
    else:
        sc(n+1, s)
        V.append(n)
        sc(n+1, s+1)
        V.pop()
sc()

# 궁수 위치에 따른 죽인 적 수 출력 함수
def shoot(i, n=0):          # i: archer index, n: 턴
    if n == N: return 0
    target = arr[n:n+D]     # 각 턴에 공격 가능한 최대 거리는 배열의 n번째 줄부터 n+D번째 줄
    kill = 0

    for A in archer[i]:     # 궁수들에 대해서
        distance = 1000
        x = 0

        r = 0
        for t in target:
            for m in range(M):
                if t[m]:
                    d = r + 1 + abs(A-m)
                    if d < distance and n <= V[n+r][m]:     # 가장 가까운적 찾기
                        distance = d
                        x = (n+r, m)
                    elif d == distance and m < x[1] and n <= V[n+r][m]:     # 턴이 같다면 왼쪽 적 찾기
                        x = (n+r, m)
            r += 1
        
        if x != 0 and distance <= D:
            if V[x[0]][x[1]] == 100:    # 최초로 공격할 때만 킬 +1
                kill += 1
            V[x[0]][x[1]] = n           # visited 턴 넘버로 표시
    return kill + shoot(i, n+1)         # 다음 턴

result = 0
for i in range(len(archer)):
    V = [[100] * M for _ in range(N)]
    tmp = shoot(i)
    if result < tmp:
        result = tmp
print(result)