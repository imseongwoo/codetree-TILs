n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]

dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(n):
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] < arr[x][y]:
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
max_val = []
for i in range(n):
    max_val.append(max(dp[i]))
print(max(max_val))