N, M = map(int, input().split())

arr = list(map(int, input().split()))

# 카드 세 장 뽑아서 저장할 리스트
pick = []

# 최대 합을 저장할 변수
max_sum = 0

def comb(k, s):
    global max_sum
    
    # 세 장 뽑았을 때
    if k == 3:
        # 리스트의 요소들의 합과 max_sum을 비교
        tmp = sum(pick)
        if tmp <= M and tmp > max_sum:
            max_sum = tmp
        return
    
    for i in range(s, N):
        pick.append(arr[i])
        comb(k + 1, i + 1)
        pick.pop()

# 함수 실행
comb(0, 0)

# 답 출력
print(max_sum)