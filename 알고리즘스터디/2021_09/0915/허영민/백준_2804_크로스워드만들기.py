data = list(input().split())
result = list(['.'] * len(data[0]) for _ in range(len(data[1])))
N, M = len(data[0]), len(data[1])
a_idx = 0
b_idx = 0
break_cnt = 0
for idx_1 in range(N):
    for idx_2 in range(M):
        if data[0][idx_1] == data[1][idx_2]:
            col_idx, row_idx = idx_1, idx_2
            break_cnt = 1
            break
    if break_cnt == 1:
        break
for idx in range(N):
    result[row_idx][idx] = data[0][idx]
for idx in range(M):
    result[idx][col_idx] = data[1][idx]
for i in range(M):
    print(''.join(map(str, result[i])))