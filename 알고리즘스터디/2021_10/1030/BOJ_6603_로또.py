def num(n=1, m=0):  # 0번은 개수
    if m == 6:      # 6개 골라지면 출력
        print(" ".join(A))
    else:
        for i in range(n, N-4+m):
            A[m] = nums[i]
            num(i+1, m+1)   # 고른 다음 것부터 고르기

while True:
    nums = input()
    if nums == '0': break
    else: nums = nums.split()
    N = int(nums[0])
    A = [0]*6
    num()
    print()
