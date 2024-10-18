# 변수 선언 및 입력
n, m = tuple(map(int ,input().split()))
arr = list(map(int, input().split()))


def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_idx


def upper_bound(target):
    left, right = 0, n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_idx


for _ in range(m):
    x = int(input())
    count = upper_bound(x) - lower_bound(x)

    print(count)