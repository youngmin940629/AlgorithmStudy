M, N = map(int,input().split())
def sequence(st,end,arr,num):
    if st == end:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, num+1):
            tmp = arr[:]
            if arr:
                if i >= arr[-1]:
                    tmp.append(i)
                    sequence(st + 1, end, tmp, num)
            else:
                tmp.append(i)
                sequence(st+1, end, tmp, num)
sequence(0,N,[],M)