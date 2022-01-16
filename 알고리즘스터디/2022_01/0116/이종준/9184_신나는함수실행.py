def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp_list[a][b][c]:
        return dp_list[a][b][c]
    if a < b and b < c:
        dp_list[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp_list[a][b][c]
    else:
        dp_list[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp_list[a][b][c]

# a, b, c 세 가지 숫자에 대해 => 3차원 배열
dp_list = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))