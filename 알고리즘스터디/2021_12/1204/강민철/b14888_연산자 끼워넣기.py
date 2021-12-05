import sys;sys.stdin = open('14888.txt')

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
maxi = -1000000001
mini = 1000000001

def perm(lev, acc):
    if lev >= N:
        global maxi, mini
        maxi = max(maxi, acc)
        mini = min(mini, acc)
    if not lev:
        perm(lev+1, nums[lev])
    for i in range(4):
        if not ops[i]: continue
        ops[i] -= 1
        if i == 0:
            perm(lev+1, acc+nums[lev])
        elif i == 1:
            perm(lev + 1, acc - nums[lev])
        elif i == 2:
            perm(lev + 1, acc * nums[lev])
        else:
            if acc < 0:
                perm(lev + 1, -(abs(acc) // nums[lev]))
            else:
                perm(lev + 1, acc // nums[lev])
        ops[i] += 1

perm(0, 0)
print(maxi, mini)