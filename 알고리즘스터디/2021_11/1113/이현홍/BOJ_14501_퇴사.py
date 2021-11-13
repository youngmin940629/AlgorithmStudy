N = int(input())

# 마지막날 처리 위해 하루 추가, 끝 일은 0
T = [1] * (N+1)
P = [0] * (N+1)

for i in range(N):
    T[i], P[i] = map(int, input().split())

mxW = 0
# 인덱스 0일차, 일 0 시작
def work(d=0, s=0):
    # 업무 초과 리턴
    if d > N: return
    else:
        global mxW
        if mxW < s: mxW = s
        # 주어진 일을 할 때
        work(d+T[d], s+P[d])
        # 안 하고 다음날
        work(d+1, s)

# 함수 실행
work()
print(mxW)

    