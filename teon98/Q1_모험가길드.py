"""
공포도를 오름차순 한 후, 그룹을 만들 수 있는 조건에 맞는지 부합하는지 확인한다.
"""

N = int(input())
fears = list(map(int, input().split()))
fears.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in fears: #공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화

print(result)