def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            # 회전 x
            if rot == 0:
                arr[r + i][c + j] += key[i][j]
            # 회천 o
            elif rot == 1:
                arr[r + i][c + j] += key[n - 1 - j][i]  # 열 증가시 행 위로 올라감
            elif rot == 2:
                arr[r + i][c + j] += key[n - 1 - i][n - 1 - j]
            else:
                arr[r + i][c + j] += key[j][n - 1 - i]


def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False

    return True


def solution(key, lock):
    # 모든 경우의 수 -> 자물쇠에 맞는 열쇠가 있다면 True 반환
    # answer = True
    # 자물쇠를 가운데두고 열쇠를 이동해가며 맞춰봄
    # 맨 왼쪽 위를 0,0 이라고 했을 때 열쇠가 그로부터 떨어진 거리 = offset
    # 최소 하나 이상은 자물쇠와 겹쳐야 함 -> 열쇠 길이 - 1
    offset = len(key) - 1
    # 행의 좌표 : r
    for r in range(offset + len(lock)):  # offset에서 자물쇠 길이를 더한 값
        # 열의 좌표: c
        for c in range(offset + len(lock)):
            # 열쇠 회전
            for rot in range(4):
                # 열쇠, 자물쇠의 최대 길이 = 20
                # 20 * 3 - 2(최소 하나씩 겹쳐야 함) = 58
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]
                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True

    return False