from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
fruit_pos = []
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * n for _ in range(n)]
ans = [[0] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if arr[a][b] == 2:
            fruit_pos.append((a, b))
            q.append((a, b))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                ans[nx][ny] = -1
                visited[nx][ny] = 1
            elif arr[nx][ny] == 1 and visited[nx][ny] == 0:
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx,ny))
                visited[nx][ny] = 1


for a in range(n):
    for b in range(n):
        if ans[a][b] == 0 and arr[a][b] == 0:
            ans[a][b] = -1
        elif ans[a][b] == 0 and arr[a][b] == 1:
            ans[a][b] = -2
        print(ans[a][b], end=' ')
    print()