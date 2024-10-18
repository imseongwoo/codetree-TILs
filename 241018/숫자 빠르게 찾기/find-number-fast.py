n, m = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(num):
    idx = -1
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            idx = mid
            break
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    if idx != -1:
        idx += 1
    return idx

for _ in range(m):
    num = int(input())
    print(binary_search(num))