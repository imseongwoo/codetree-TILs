n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = arr[0][0]

for j in range(1, n):
    dp[0][j] = dp[0][j - 1] + arr[0][j]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + arr[i][0]

for a in range(1, n):
    for b in range(1, n):
        dp[a][b] = max(dp[a][b - 1] + arr[a][b], dp[a - 1][b] + arr[a][b])
print(dp[n-1][n-1])