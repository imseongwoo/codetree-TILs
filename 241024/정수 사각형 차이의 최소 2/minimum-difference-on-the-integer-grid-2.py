from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[] for _ in range(n)] for _ in range(n)]
dp[0][0].append(arr[0][0])  

for b in range(1, n):
    temp = deepcopy(dp[0][b-1])  
    temp.append(arr[0][b])       
    dp[0][b] = temp             

for a in range(1, n):
    temp_top = deepcopy(dp[a-1][0])  
    temp_top.append(arr[a][0])       
    dp[a][0] = temp_top              

for a in range(1, n):
    for b in range(1, n):
        temp_from_top = deepcopy(dp[a-1][b])    
        temp_from_left = deepcopy(dp[a][b-1])  
        
        temp_from_top.append(arr[a][b])
        temp_from_left.append(arr[a][b])
        
        if max(temp_from_top) - min(temp_from_top) < max(temp_from_left) - min(temp_from_left):
            dp[a][b] = temp_from_top
        else:
            dp[a][b] = temp_from_left

final_path = dp[n-1][n-1]

min_val = min(final_path)
max_val = max(final_path)

print(max_val - min_val)