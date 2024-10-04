from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
arr = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

q = deque()


def bfs():
    while q:
        qx, qy = q.popleft()

        for i in range(8):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1:
                arr[nx][ny] = arr[qx][qy] + 1
                visited[nx][ny] = 1
                q.append((nx, ny))


q.append((r1, c1))
visited[r1][c1] = 1
bfs()

if r1 == r2 and c1 == c2:
    print(0)
elif arr[r2][c2] == 0:
    print(-1)
else:
    print(arr[r2][c2])