from itertools import combinations
from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

walls = []
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for a in range(n):
    for b in range(n):
        if arr[a][b] == 1:
            walls.append((a, b))

visited = [[0] * n for _ in range(n)]

def init_visited():
    for a in range(n):
        for b in range(n):
            visited[a][b] = 0

def bfs():
    init_visited()
    q = deque()
    q.append((r1, c1))
    visited[r1][c1] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

for wall_pos in combinations(walls, k):
    for x, y in wall_pos:
        arr[x][y] = 0
    bfs()
    ans.append(visited[r2][c2])
    for x, y in wall_pos:
        arr[x][y] = 1

num = 10001
for a in ans:
    if a != 0 and a < num:
        num = a

if num == 10001:
    print(-1)
else:
    print(num-1)