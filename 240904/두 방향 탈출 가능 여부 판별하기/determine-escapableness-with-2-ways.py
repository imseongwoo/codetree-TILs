n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]
cnt = 1

def dfs(x, y):
    global cnt
    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and visited[nx][ny] == 0:
            answer[nx][ny] = cnt
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx, ny)


visited[0][0] = 1
dfs(0, 0)

if answer[n-1][m-1]:
    print(1)
else:
    print(0)