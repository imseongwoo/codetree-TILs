from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque()

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1 and arr[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1

q.append((0,0))
visited[0][0] = 1
bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)