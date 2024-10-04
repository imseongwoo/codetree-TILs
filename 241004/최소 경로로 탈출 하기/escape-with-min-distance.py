from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def bfs():

    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1 and arr[nx][ny] != 0 :
                dist[nx][ny] = dist[qx][qy] + 1
                visited[nx][ny] = 1
                q.append((nx,ny))


q.append((0,0))
visited[0][0] = 1
bfs()

if dist[n-1][m-1] != 0:
    print(dist[n-1][m-1])
else:
    print(-1)