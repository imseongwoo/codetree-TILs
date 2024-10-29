n,k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n+1)
ans = 0
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for i in range(n,1,-1):
    for j in range(1,i):
        if prefix_sum[i]-prefix_sum[j] == k:
            ans += 1

for a in prefix_sum:
    if a == k:
        ans += 1

print(ans)