import sys; sys.stdin = open('BOJ_15651_N과M.txt', 'r')
# def dol(n,m):
#     if m == 0:
#         return
#     for i in range(1, n+1):
#         dol(n,m-1)
#         print(i, end=' ')
# for _ in range(3):

#     dol(n,m)
#
# for _ in range(3):
#     n, m = map(int, input().split())
#     arr = [i for i in range(1,n+1)]
#
#
# def perm(k, n):
#
#     if k == n:
#         print(arr)
#         return
#
#     for i in range(k, n):
#         arr[i], arr[k] = arr[k], arr[i]
#         perm(k + 1, n)
#         arr[i], arr[k] = arr[k], arr[i]
#
#
#
# perm(0, m)

# def dol(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             for k in range(1, n+1):
#                 for l in range(1, n+1):
#                     for m in range(1, n+1):
#                         for n in range(1, n+1):
#                             for o in range(1, n+1):
#                                 print(i, end=' ')
#                             if m == 1:
#                                 return
#                             else:
#                                 print(j, end=' ')
#                                 if m == 2:
#                                     return
#                                 else:
#                                     print(k, end=' ')
#                                     if m == 3:
#                                         return
#                                     else:
#                                         print(l, end=' ')
#                                         if m == 4:
#                                             return
#                                         else:
#                                             print(m, end=' ')
#                                             if m == 5:
#                                                 return
#                                             else:
#                                                 print(n, end=' ')
#                                                 if m == 6:
#                                                     return
#                                                 else:
#                                                     print(o, end=' ')
# for i in range(3):
#     n, m = map(int, input().split())
#     while m == 0:
#         for i in range(1,n+1):
#             for j in range(1, n+1):
#                 for k in range(1, n+1):
#                     print(i, end=' ')
#                     print(j, end=' ')
#                     print(k, end=' ')
#                     print()
#                 print()
#             print()
#         print()
N, M = map(int, input().split())
maps=list(range(1, N+1))
def dfs(maps,visit ):
    if len(visit) == M:
        print(*visit)
        return
    elif len(maps)==0:
        return
    else:
        for i in range(0, len(maps)):
            visit2= visit[:]
            visit2.append(maps[i])
            dfs(maps[:], visit2)

for i in range(0, len(maps)):
    dfs(maps[:], [maps[i]])