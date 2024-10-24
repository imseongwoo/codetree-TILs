n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# DP table to store min and max values for each cell
dp = [[(float('inf'), float('-inf')) for _ in range(n)] for _ in range(n)]

# Initialize the top-left corner
dp[0][0] = (arr[0][0], arr[0][0])

# Fill the first row (can only come from the left)
for b in range(1, n):
    min_val, max_val = dp[0][b - 1]
    dp[0][b] = (min(min_val, arr[0][b]), max(max_val, arr[0][b]))

# Fill the first column (can only come from the top)
for a in range(1, n):
    min_val, max_val = dp[a - 1][0]
    dp[a][0] = (min(min_val, arr[a][0]), max(max_val, arr[a][0]))

# Fill the rest of the DP table
for a in range(1, n):
    for b in range(1, n):
        # Min and max values from the top
        min_from_top, max_from_top = dp[a - 1][b]
        # Min and max values from the left
        min_from_left, max_from_left = dp[a][b - 1]
        
        # Calculate min and max values for the current cell
        new_min = min(min(min_from_top, min_from_left), arr[a][b])
        new_max = max(max(max_from_top, max_from_left), arr[a][b])
        
        dp[a][b] = (new_min, new_max)

# Get the result at the bottom-right corner
min_val, max_val = dp[n - 1][n - 1]
result = max_val - min_val
print(result)