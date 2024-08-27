from copy import deepcopy

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
r, c = map(int, input().split())

bomb_range = arr[r - 1][c - 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def inBomb(x, y, cx, cy, bomb_range):
    return (x == cx or y == cy) and abs(x - cx) + abs(y - cy) < bomb_range


for i in range(n):
    for j in range(n):
        if inBomb(i, j, r - 1, c - 1, bomb_range):
            arr[i][j] = 0

new_arr = deepcopy(arr)

# 중력 적용
for j in range(n):
    # 한 열씩 처리합니다.
    empty_row = n - 1  # 가장 아래부터 숫자를 채워나갑니다.
    for i in range(n - 1, -1, -1):
        if arr[i][j] != 0:
            new_arr[empty_row][j] = arr[i][j]
            empty_row -= 1

    # 남은 칸은 0으로 채웁니다.
    for i in range(empty_row, -1, -1):
        new_arr[i][j] = 0

# 결과 출력
for row in new_arr:
    print(' '.join(map(str, row)))