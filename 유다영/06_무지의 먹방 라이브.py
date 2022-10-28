# 각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times
# 네트워크 장애가 발생한 시간 K초
# 몇 번 음식부터 다시 섭취하면 되는 지 return 하도록 solution 함수 완성

from operator import itemgetter


def solution(food_times, k):
    foods = []  # 음식을 먹는 데 필요한 시간, 음식의 번호를 함께 저장해서 정렬하기 위한 리스트 정의
    n = len(food_times)  # 음식의 총 개수
    for i in range(n):  # 음식의 개수 만큼 foods 리스트에 추가
        foods.append((food_times[i], i + 1))  # 시간, 음식 번호(1~n)
    foods.sort()  # 먹는 시간 순 오름차순 정렬

    # 이전 음식 시간과의 간격을 구함
    pretime = 0  # 이전 음식
    for i, food in enumerate(foods):  # 인덱스& vaule 필요
        diff = food[0] - pretime  # 그래프에서의 높이, 간격 차
        if diff != 0:
            spend = diff * n  # 소비한 시간 = diff * 남은 음식 개수
            # k에서 spend를 빼주기
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n  # 남은 시간을 남은 음식 개수로 나머지 연산
                # 남은 음식은 순서대로 먹어야 함.
                # foods[i:]: i~끝까지.
                sublist = sorted(foods[i:], key=itemgetter(1))  # 음식번호(인덱스 1)로 오름차순 정렬
                return sublist[k][1] # 인덱스 1: 음식 번호 반환
        n -= 1  # turn이 끝날때 마다 음식 하나를 다 먹은 것.
    return -1 # 더 섭취할 음식이 없다면


result = solution([3, 1, 2], 5)
print(result)
