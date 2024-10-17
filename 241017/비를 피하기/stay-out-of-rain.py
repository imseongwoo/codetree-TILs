from collections import deque

n,h,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

shelter = []

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    visited = [[0]*n for _ in range(n)]


    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and (arr[nx][ny] == 0 or arr[nx][ny] == 2):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                if arr[nx][ny] == 3:
                    visited[nx][ny] = visited[x][y] + 1
                    return visited[nx][ny]

    return -1

for a in range(n):
    for b in range(n):
        if arr[a][b] == 2:
            cnt = bfs(a,b)
            ans[a][b] = cnt

for a in range(n):
    for b in range(n):
        print(ans[a][b],end=' ')
    print()