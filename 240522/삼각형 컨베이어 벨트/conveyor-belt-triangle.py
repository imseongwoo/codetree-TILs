from collections import deque

n, t = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
arr = first + second + third
arr = deque(arr)

for _ in range(t):
    arr.appendleft(arr.pop())
arr = list(arr)

for i in range(n):
    print(arr[i], end=' ')
print()
for i in  range(n, 2*n):
    print(arr[i], end=' ')
print()
for i in  range(2*n, 3*n):
    print(arr[i], end=' ')