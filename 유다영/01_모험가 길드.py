# 공포도가 x인 모험가는 반드시 x명 이상 구성한 모험가 그룹에 참여해야 여행을 떠남
# 최대 몇개의 모험가 그룹?

n = int(input())


scary = list(map(int, input().split()))
scary.sort()

member = 0
group = 0
for s in scary:
    member += 1
    if member >= s: # 공포수보다 멤버의 수가 많을때
        group += 1
        member = 0

print(group)


'''
5
2 3 1 2 2
'''