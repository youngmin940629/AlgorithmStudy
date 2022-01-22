P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
l = 10

for n in range(int(input())):
    x = int(input())
    while l < x:
        l += 1
        P.append(P[l-4]+P[l-3])
    print(P[x-1])