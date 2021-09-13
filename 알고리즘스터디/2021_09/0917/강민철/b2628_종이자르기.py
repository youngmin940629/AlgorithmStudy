R, C = map(int, input().split())
N = int(input())
row = [0, C]
col = [0, R]
for _ in range(N):
    a, b = map(int, input().split())
    if a:
        col.append(b)
    else:
        row.append(b)
row.sort()
col.sort()
max_row = 0
max_col = 0
for i in range(1, len(row)):
    if row[i] - row[i-1] > max_row:
        max_row = row[i] - row[i-1]
for i in range(1, len(col)):
    if col[i] - col[i-1] > max_col:
        max_col = col[i] - col[i-1]

print(max_row * max_col)