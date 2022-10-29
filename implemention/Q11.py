# - 뱀은 몸길이를 먼저 늘린 후 이동 → 이동한 칸에 사과가 있다면 꼬리 움직이지 않음

#                                                  이동한 칸에 사과가 없다면 꼬리가 위치한 칸을 비움


# - 주어지는 뱀의 방향 변환 정보는 게임 시작 시간으로부터 X초이고, X초가 지난 후에 방향을 변환함

#   ex. 8 D, 10 D, 11D, 13L이 주어진 경우

#       8초동안 오른쪽으로 진행 (초기 방향 설정이 오른쪽이므로)

#       → D (오른쪽으로 방향 회전 : 아래 방향)

#       → 2초 동안 아래 방향으로 진행

#       → D (오른쪽으로 방향 회전 : 왼쪽 방향)

#       → 1초 동안 왼쪽 방향으로 진행

#       → D (오른쪽으로 방향 회전 : 위쪽 방향)

#       → 2초 동안 위쪽 방향으로 진행 (왼쪽으로 방향 회전 : 왼쪽 방향)

# - 종료 조건은 벽 또는 자기 자신의 몸과 부딪힐 경우

#   → 입력 예시 2와 같이 방향 변환이 끝났는데 자기 자신의 몸과 부딪히지 않은 경우에는

#      마지막에 제시한 방향으로 쭉 진행하고 벽에 부딪히면 게임이 종료됨

#   ex. 예시 2의 경우 위의 방향 변환 정보를 다 수행하고도 자신의 몸과 부딪히지 않아 게임이 종료되지 않으므로

#       최종 방향인 왼쪽 방향으로 계속 진행하고 왼쪽 벽에 부딪히면 게임이 종료됨

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
maps = [[0] * (n+1) for _ in range(n+1)] # 사과의 위치가 있는 n*n의 지도정보
for _ in range(k):#사과의 위치
    x,y = map(int,input().split())
    maps[x][y] = 2 # 사과 위치 좌표 2, 뱀 몸통 1, 아무것도 없을 시 0
info = {} #뱀의 방향변환 정보(시간이 key, 전환방향이 value로 들어 있는 딕셔러니)
l = int(input())
for _ in range(l):# 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
    sec, direct = input().split()
    info[int(sec)] = direct
time = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x, y = 1, 1
maps[y][x] = 1
d = 0
snakes = deque([(1, 1)])#(뱀이 차지하고 있는 좌표가 들어 있는 deque/ 사과를 먹지 못하면 꼬리부터 없애야 하므로 popleft)

while True:
    nx, ny = x+dx[d], y+dy[d]
    # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
    if nx<=0 or ny<=0 or nx>n or ny>n or (nx,ny) in snakes:
        break
    # 사과를 먹지 못하면 꼬리 없애기
    if maps[ny][nx]!=2:
        a,b = snakes.popleft()
        maps[b][a]=0
    x, y = nx, ny
    maps[y][x] = 1
    snakes.append((nx, ny))
    time+=1
	
    # 시간에 해당하는 방향전환 정보가 있을 경우
    if time in info.keys():
        if info[time] == "D":
            d = (d+1)%4
        else:
            nd = 3 if d==0 else d-1
            d = nd
print(time+1)
