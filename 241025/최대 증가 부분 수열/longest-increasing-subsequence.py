n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(n):

    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp)+1)