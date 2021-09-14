import sys
sys.stdin = open('1159.txt', 'r')

# 딕셔너리 활용

N = int(input())
f_dic = {}
for i in range(N):
    data = input()
    for j in range(len(data)):
        if data[0] not in f_dic:
            f_dic.setdefault(data[0]) # 키 값 추가해주기
            f_dic[data[0]] = 1
    else:
        f_dic[data[0]] = f_dic[data[0]] + 1

k_list=[]
fs_dic = sorted(f_dic.items()) # => 사전순으로 정렬, 리스트로 바뀜
for k in range(len(fs_dic)):
    if fs_dic[k][1] > 5:
        print(fs_dic[k][0], end='')
    else:
        k_list.append(fs_dic[k][0])
        if len(k_list) == len(fs_dic):
            print('PREDAJA')