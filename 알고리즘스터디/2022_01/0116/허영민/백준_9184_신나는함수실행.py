def function(x,y,z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return function(20,20,20)
    if dp[x][y][z]:
        return dp[x][y][z]
    if x < y < z:
        dp[x][y][z] = function(x,y,z-1) + function(x,y-1,z-1) - function(x,y-1,z)
        return dp[x][y][z]
    dp[x][y][z] = function(x-1,y,z) + function(x-1,y-1,z) + function(x-1,y,z-1) - function(x-1,y-1,z-1)
    return dp[x][y][z]



dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print('w({}, {}, {}) = {}'.format(a,b,c,function(a,b,c)))