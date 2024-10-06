# 1. 남쪽으로 한 칸 내려가기
# 2. 남쪽으로 못가면 서쪽으로 회전한후 한칸 내려가기
# 3. 서쪽으로 회전 못하면 동쪽으로 회전하고 한칸 내려가기
# 4. 갈 수 있는 가장 남쪽의 칸으로 이동, 만약 골렘의 몸 일부가 숲을 벗어난 상태면 맵을 초기화하고 다음 값 탐색
# 5. 출구가 다른 골렘과 인접하고 있다면 다른 골렘으로 이동 가능

from collections import deque

r, c, k = map(int, input().split())
arr = [[0] * c for _ in range(r + 3)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
isExit = [[False] * c for _ in range(r + 3)]
answer = 0


def canGo(x, y):
    return (0 <= y - 1 and y + 1 < c and 0 <= x - 1 and x + 1 < r + 3 and
            arr[x - 1][y - 1] == 0 and arr[x - 1][y] == 0 and arr[x - 1][y + 1] == 0 and
            arr[x][y - 1] == 0 and arr[x][y] == 0 and arr[x][y + 1] == 0 and
            arr[x + 1][y] == 0)


def inRange(x, y):
    return 3 <= x < r + 3 and 0 <= y < c


def down(x, y, d, id):
    if canGo(x + 1, y):
        # 아래로 내려가는 경우
        down(x + 1, y, d, id)
    elif canGo(x + 1, y - 1):
        # 왼쪽 아래의 경우
        down(x + 1, y - 1, (d + 3) % 4, id)
    elif canGo(x + 1, y + 1):
        # 오른쪽 아래의 경우
        down(x + 1, y + 1, (d + 1) % 4, id)
    else:
        if not inRange(x - 1, y - 1) or not inRange(x + 1, y + 1):
            resetMap()
        else:
            arr[x][y] = id
            for i in range(4):
                arr[x + dx[i]][y + dy[i]] = id
            isExit[x + dx[d]][y + dy[d]] = True
            global answer
            answer += bfs(x, y) - 3 + 1


def resetMap():
    for i in range(r + 3):
        for j in range(c):
            arr[i][j] = 0
            isExit[i][j] = False


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[False] * c for _ in range(r + 3)]
    visited[x][y] = True
    result = x

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if inRange(nx, ny) and not visited[nx][ny] and (
                    arr[nx][ny] == arr[cur_x][cur_y] or (isExit[cur_x][cur_y] and arr[nx][ny] != 0)):
                queue.append((nx, ny))
                visited[nx][ny] = True
                result = max(result, nx)
    return result


for id in range(1, k + 1):
    y, d = map(int, input().split())
    down(0, y - 1, d, id)
print(answer)