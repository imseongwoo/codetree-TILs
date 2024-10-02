import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, arr, dp, n):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny, arr, dp, n) + 1)
    
    return dp[x][y]

def find_max_steps(n, arr):
    dp = [[-1] * n for _ in range(n)]
    
    max_steps = 0
    for i in range(n):
        for j in range(n):
            max_steps = max(max_steps, dfs(i, j, arr, dp, n))
    
    return max_steps

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(find_max_steps(n, arr))