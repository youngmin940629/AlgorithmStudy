def my_set(idx, sum):
        global cnt
        
        # idx가 수열의 최대 길이보다 길거나 같아지면 return
        if idx >= N:
            return

        # tmp에 합 저장, K와 같아지면 카운트하기
        tmp = sum + arr[idx]
        if tmp == K:
            cnt += 1
            
        # 1개, 2개, ... 이런 식으로 합을 늘려나가는 방법
        my_set(idx + 1, sum)
        my_set(idx + 1, tmp)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0    

    my_set(0, 0)
    print(cnt)