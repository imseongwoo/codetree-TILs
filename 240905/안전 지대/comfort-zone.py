import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
safe_zone_num = 0
safe_zone_list = []


def make_safe_zone(k):
    global arr
    for i in range(n):
        for j in range(m):
            if arr[i][j] <= k:
                arr[i][j] = 0


def zero_safezone():
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                return True
    return False


def dfs(x, y, visited):
    global safe_zone_num
    global safe_zone_list

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and visited[nx][ny] != 1:
            visited[nx][ny] = 1
            dfs(nx, ny, visited)


k = 1
while zero_safezone():
    make_safe_zone(k)
    safe_zone_num = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visited[i][j] != 1:
                visited[i][j] = 1
                dfs(i, j, visited)
                safe_zone_num += 1
    safe_zone_list.append(safe_zone_num)
    k += 1

ans = safe_zone_list.index(max(safe_zone_list))
print(ans + 1, end=' ')
print(safe_zone_list[ans])