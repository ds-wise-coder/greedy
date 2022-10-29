import itertools # 순열
import math


def solution(n, weak, dist):
    # n: 외벽의 길이, weak: 취약지점, dist: 각각의 친구가 이동할 수 있는 거리
    # 취약지점 개수
    weak_size = len(weak)
    # 계산 용이
    weak = weak+[w + n for w in weak]
    min_cnt = math.inf
    for start in range(weak_size):
        for d in itertools.permutations(dist, len(dist)):
            cnt =1 # 친구
            pos = start # 친구의  시작점
            for i in range(1, weak_size): # 취약지점 방문 체크
                # 시작위치(0)는 친구 1의 시작점이므로 방문 할 필요x -> 1부터 방문
                next_pos=start+i # 다음 방문
                diff = weak[next_pos]-weak[pos] # 거리
                # 거리 > 이동할 수 있는 거리
                if diff>d[cnt-1]: # 인덱스 0
                    pos = next_pos
                    cnt +=1
                    # 초과된 상태
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                min_cnt=min(min_cnt, cnt)
    if min_cnt == math.inf:
        return -1

    answer = min_cnt
    return answer