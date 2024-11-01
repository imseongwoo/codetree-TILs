n, q = map(int, input().split())
arr = list(map(int, input().split()))
num = 1000001
check = [0] * num
prefix_sum = [0] * num

for a in arr:
    check[a] = 1

for i in range(1, num):
    prefix_sum[i] = prefix_sum[i-1] + check[i]

for _ in range(q):
    a, b = map(int, input().split())
    ans = -1
    if check[a] == 0 and check[b] == 0:
        ans = prefix_sum[b] - prefix_sum[a]
    else:
        ans = prefix_sum[b] - prefix_sum[a] + 1
    print(ans)