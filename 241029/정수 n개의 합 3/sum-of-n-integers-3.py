n, k = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(n)]
arr.insert(0, [0] * (n + 1))
prefix_sum = [[0]*(n+1) for _ in range(n+1)]
ans = -1

for i in range(1,n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i][j]

for i in range(1,n+2-k):
    for j in range(1, n+2-k):
        x1 = i
        y1 = j
        x2 = i+k-1
        y2 = j+k-1
        tmp = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
        ans = max(ans, tmp)
print(ans)