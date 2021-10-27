height = [int(input()) for _ in range(9)]
result = []
visited = [0] * 9
def hobit(x,check):
    if x == 7:
        if check == 100:
            for i in range(9):
                if visited[i]:
                    result.append(height[i])
            return
    if check > 100:
        return
    elif not result:
        for j in range(9):
            if not visited[j]:
                visited[j] = 1
                hobit(x+1, check+height[j])
                visited[j] = 0
    if not result:
        return
hobit(0,0)
result.sort()
for i in range(7):
    print(result[i])