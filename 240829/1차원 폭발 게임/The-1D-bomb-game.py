n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

def check_bombs():
    global arr
    i = 0
    while i < len(arr):
        num = arr[i]
        cnt = 1
        while i + cnt < len(arr) and arr[i + cnt] == num:
            cnt += 1

        if cnt >= m:
            del arr[i:i + cnt] 
            return True  
        i += cnt
    return False  

while check_bombs():
    pass

print(len(arr))
for num in arr:
    print(num)