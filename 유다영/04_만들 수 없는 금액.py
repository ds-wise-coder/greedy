'''
n개의 동전
만들 수 없는 양의 정수 금액 중 최솟값?
'''

n = int(input())

coin = list(map(int, input().split()))
coin.sort()

min_coin = 1

for c in coin:
    if min_coin >= c:
        min_coin += c
        print(min_coin)
    else:  # 만들 수 없는 양의 정수보다 동전이 더 클 때 종료
        break

print(min_coin)

'''
5
3 2 1 1 9
'''
