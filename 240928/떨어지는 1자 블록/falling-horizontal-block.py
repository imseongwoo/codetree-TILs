n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k -= 1
final_row = n-1

for row in range(n - 1):
    for i in range(k, k + m):
        if arr[row][i] == 1:
            final_row = row - 1
            break
    else:
        final_row = row


for i in range(k, k + m):
    arr[final_row][i] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()