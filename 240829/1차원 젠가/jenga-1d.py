n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

len_arr = n

def cut_arr(si, ei):
    global len_arr, arr
    temp = []
    for i in range(si, ei+1):
        arr[i] = 0

    for a in arr:
        if a:
            temp.append(a)

    len_arr = len(temp)
    for i in range(len_arr):
        arr[i] = temp[i]

    cnt = len(arr) - len_arr
    for _ in range(cnt):
        arr.pop()

for _ in range(2):
    s, e = map(int, input().split())
    cut_arr(s-1, e-1)

print(len_arr)
for i in range(len_arr):
    print(arr[i])