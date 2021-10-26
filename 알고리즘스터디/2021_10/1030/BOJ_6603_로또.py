def num(n=1, m=0):
    if m == 6:
        print(" ".join(A))
    else:
        for i in range(n, N-4+m):
            A[m] = nums[i]
            num(i+1, m+1)

while True:
    nums = input()
    if nums == '0': break
    else: nums = nums.split()
    N = int(nums[0])
    A = [0]*6
    num()
    print()
