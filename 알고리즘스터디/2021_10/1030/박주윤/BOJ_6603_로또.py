while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    N = len(arr)

    for n in range(1, N-5):
        for m in range(n+1, N-4):
            for l in range(m+1, N-3):
                for k in range(l+1, N - 2):
                    for j in range(k+1, N - 1):
                        for i in range(j+1, N):
                            print(arr[n], arr[m], arr[l], arr[k], arr[j], arr[i])
    print()
'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''