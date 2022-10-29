# 인자 전달 용이하게끔
Pillar =[[]] # 기둥
Bar = [[]] # 보

def checkPillar(x, y):
    # 바닥면 설치 가능 or 바로 아래에 기둥이 있는 경우
    if y == 0 or Pillar[x][y-1]:
        return True
    # 보 위에 설치 가능
    if (x > 0 and Bar[x-1][y]) or Bar[x][y]:
        return True
    return False
def checkBar(x,y):
    # 바로 밑에 기둥이 있을 경우 or 오른쪽 바로 아래에 있는 경우
    if Pillar[x][y-1] or Pillar[x+1][y-1]: # x+1 -> x==n일 경우 범위 벗어남-> 아래 n+2로 크기를 하나더 늘려준다.
        return True
    # 양쪽(왼쪽, 오른쪽)에 보가 있는 경우
    if x>0 and Bar[x-1][y] and Bar[x+1][y]:
        return True
    # 나머지는 보 설치 불가
    return False
def canDelete(x,y):
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            if Pillar[i][j] and checkPillar(i,j) == False:
                return False # 삭제 불가
            if Bar[i][j] and checkBar(i,j)==False:
                return False
    return True # 삭제 가능

def solution(n, build_frame):
    global Pillar,Bar
    Pillar=[[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for x,y,kind,cmd in build_frame:
        if kind==0: # 기둥
            if cmd==1: # 설치
                if checkPillar(x,y): # 설치할 수 있는 지 체크
                    Pillar[x][y]=1 # 기둥 설치
            else:
                Pillar[x][y]=0
                if not canDelete(x,y):
                    Pillar[x][y]=1
        else: # 보 일 경우
            if cmd ==1:
                if checkBar(x,y):
                    Bar[x][y]=1
            else:
                Bar[x][y]=0
                if not canDelete(x,y):
                    Bar[x][y]=1

    answer = []
    for x in range(n+1):
        for y in range(n+1):
            if Pillar[x][y]:
                answer.append([x,y,0])
            if Bar[x][y]:
                answer.append([x,y,1]) # 보는 1


    return answer