kim = [0] * 5
ann = []

for i in range(5):
    kim[i] = list(map(int, input().split()))

for _ in range(5):
    ann = ann + list(map(int, input().split()))


num = 0
for a in ann:
    num += 1                       # 부른 숫자 수
    for r in range(5):
        for c in range(5):
            if a == kim[r][c]:
                kim[r][c] = 0      # 부른 번호를 0으로 만듦
                break
    cnt = 0

    # 3줄 빙고 최소 조건 12개까진 아래 과정x
    if num < 12: continue

    # 가로
    for k in kim:
        if not sum(k):
            cnt += 1

    # 세로
    for c in range(5):
        tmp = 0
        for k in kim:
            tmp += k[c]
        if not tmp: cnt += 1

    # 대각
    lr = rl = 0
    for i in range(5):
        lr += kim[i][i]
        rl += kim[i][4-i]
    if lr == 0:
        cnt += 1
    if rl == 0:
        cnt += 1

    if cnt >= 3:
        print(num)
        break




