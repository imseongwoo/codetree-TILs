from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[] for _ in range(n)] for _ in range(n)]
dp[0][0].append([arr[0][0]])

for b in range(1, n):
    temp = deepcopy(dp[0][b - 1])
    for path in temp:
        path.append(arr[0][b])
    dp[0][b] = temp

for a in range(1, n):
    temp_top = deepcopy(dp[a - 1][0])
    for path in temp_top:
        path.append(arr[a][0])
    dp[a][0] = temp_top

for a in range(1, n):
    for b in range(1, n):
        temp_from_top = deepcopy(dp[a - 1][b])
        for path in temp_from_top:
            path.append(arr[a][b])

        temp_from_left = deepcopy(dp[a][b - 1])
        for path in temp_from_left:
            path.append(arr[a][b])

        dp[a][b] = temp_from_top + temp_from_left
ans = []
for path in dp[n - 1][n - 1]:
    ans.append(abs(max(path)-min(path)))

print(min(ans))