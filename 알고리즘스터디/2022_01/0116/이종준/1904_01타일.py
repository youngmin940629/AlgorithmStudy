# 그저 피보나치...? 메모리초과 주의
def fibo(n):
    for i in range(2, n + 1):
        # dp에 저장할 숫자를 미리 15746으로 저장해서 메모리초과 방지
        dp.append((dp[i-1] + dp[i-2]) % 15746)
N = int(input())
dp = [1, 1]
fibo(N)
print(dp[N])