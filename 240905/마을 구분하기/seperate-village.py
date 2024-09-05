n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
town_member = []
member = 1

def dfs(x, y):
    global town_member
    global member

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and visited[nx][ny] != 1:
            member += 1
            visited[nx][ny] = 1
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] != 1:
            visited[i][j] = 1
            member = 1
            dfs(i,j)
            town_member.append(member)

print(len(town_member))
town_member.sort()
for a in town_member:
    print(a)