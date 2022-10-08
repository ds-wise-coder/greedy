'''
볼링공 개수: N
볼링공 최대 무게 : M
볼링공 고르는 경우의 수?
'''
from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        if weight[i] != weight[j]:
            cnt += 1
print(cnt)

'''
5 3
1 3 2 3 2


8 5
1 5 4 3 2 4 5 2
'''
