def find_path(n, r, c, grid):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 상, 하, 좌, 우 순서
    result = []
    r, c = r - 1, c - 1 
    
    while True:
        result.append(grid[r][c])
        current_value = grid[r][c]
        found = False
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > current_value:
                r, c = nr, nc
                found = True
                break
        
        if not found:
            break
    
    return result


n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


result = find_path(n, r, c, grid)
print(" ".join(map(str, result)))