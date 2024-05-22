from collections import deque

n, t = map(int, input().split())
up = list(map(int, input().split()))
down = list(map(int, input().split()))
arr = up + down
arr = deque(arr)

for _ in range(t):
    arr.appendleft(arr.pop())
arr = list(arr)

for i in range(n):
    print(arr[i], end=' ')
print()
for i in  range(n, 2*n):
    print(arr[i], end=' ')