n = int(input())
arr = []
answer = -1
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i+2 >= n:
            continue
        if j+2 >= n:
            continue
        temp = 0

        for a in range(i,i+3):
            for b in range(j,j+3): 
                temp += arr[a][b]
        
        if temp > answer:
            answer = temp
print(answer)