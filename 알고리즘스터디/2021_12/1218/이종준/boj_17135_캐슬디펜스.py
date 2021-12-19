N, M, D = map(int, input().split())

def arrange_archers():
    tmp_map = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp_map[i][j] = my_map[i][j]
    tmp_map.append([0] * M)

    cnt = 0
    flag = True
    while flag:
        # 공격하고 카운트 올리기
        # 맨 왼쪽부터 체크해버리기?
        # 맵 재배치
        # 적 남아있는지 확인
        # 고려해야 할 점: 궁수는 한번에 동시에 공격 => 꼭 처치하는 적이 셋이 아닐 수도 있음
        for i in range(N):
            for j in range(M):
                if tmp_map[i][j] == 1:
                    break
    return cnt
    

def comb_archers(k, s):
    global ans
    if k == 3:
        tmp_ans = arrange_archers()
        if  tmp_ans > ans:
            ans = tmp_ans
    for i in range(s, M):
        pick.append(i)
        comb_archers(k + 1, i + 1)
        pick.pop()

ans = 0
my_map = [list(map(int, input().split())) for _ in range(N)]
pick = []
comb_archers(0, 0)
print(ans)