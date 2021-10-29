def check(x,y,arr):
    if x == 6:
        print(' '.join(map(str, arr)))
        return
    elif (len(arr) + data[0] - y) >= 6:
        for i in range(y,data[0]):
            if not visited[i] and (len(arr) + data[0] - i) >= 6:
                visited[i] = 1
                check(x+1,i,arr + [lotto[i]])
                visited[i] = 0


while True:
    data = list(map(int, input().split()))
    visited = [0] * data[0]
    if data != [0]:
        n = data[0]
        lotto = [0] * data[0]
        for i in range(len(lotto)):
            lotto[i] = data[i+1]
        check(0,0,[])
        print()
    else:
        break