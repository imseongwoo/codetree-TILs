n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, number):
    stack = [(x, y)]
    visited[x][y] = True
    block_size = 0
    
    while stack:
        x, y = stack.pop()
        block_size += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == number:
                visited[nx][ny] = True
                stack.append((nx, ny))
    
    return block_size

visited = [[False] * n for _ in range(n)]

exploding_blocks = 0
max_block_size = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = dfs(i, j, visited, grid[i][j])
  
            if block_size >= 4:
                exploding_blocks += 1
   
            max_block_size = max(max_block_size, block_size)

print(exploding_blocks, max_block_size)