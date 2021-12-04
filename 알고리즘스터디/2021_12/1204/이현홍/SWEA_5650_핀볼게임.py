dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = tuple(tuple(map(int, input().split())) for _ in range(N))

    # 웜홀 호출용
    wormhole = {}
    for r in range(N):
        for c in range(N):
            if 6 <= arr[r][c] <= 10:
                if wormhole.get(arr[r][c], -1) == -1: wormhole[arr[r][c]] = [(r, c)]
                else: wormhole[arr[r][c]] += [(r, c)]
    
    # 바깥 한 줄 씩 추가
    visited = [[[0]*4 for _ in range(N+2)] for _ in range(N+2)]

    result = 0
    for sr in range(N):
        for sc in range(N):
            for i in range(4):
                if arr[sr][sc] == 0:
                    r, c = sr, sc
                    d = i
                    p = 0
                    while True:
                        visited[r][c][d] = p
                        nr = r + dr[d]
                        nc = c + dc[d]
                        # 시작점 또는 블랙홀 만났을 시
                        if 0 <= nr < N and 0 <= nc < N:
                            if (nr, nc) == (sr, sc) or arr[nr][nc] == -1:
                                if result < p:
                                    result = p
                                break
                            # 블록 만났을 때 방향 전환
                            if 1 <= arr[nr][nc] <= 5:
                                p += 1
                                if arr[nr][nc] == 5: d = (d+2) % 4
                                else:
                                    if d == arr[nr][nc] -1 or (d+1) % 4 == arr[nr][nc] -1: d = (d+2) % 4
                                    elif d == (arr[nr][nc]+1) % 4: d = (d+1) % 4
                                    elif d == (arr[nr][nc]) % 4: d = (d+3) % 4
                            # 웜홀 만나면 다른 웜홀로 이동
                            elif 6 <= arr[nr][nc] <= 10:
                                idx = (wormhole[arr[nr][nc]].index((nr, nc)) + 1) % 2
                                nr, nc = wormhole[arr[nr][nc]][idx]
                        # 외부 벽 만날 시
                        else:
                            d, p = (d+2)%4, p+1
                        r, c = nr, nc

    print('#{} {}'.format(tc, result))