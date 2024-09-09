from itertools import combinations
from collections import deque

def bfs(grid, starts, n):
    visited = [[False] * n for _ in range(n)]
    queue = deque(starts)
    count = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    
    for r, c in starts:
        visited[r][c] = True
        count += 1
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                count += 1
                queue.append((nr, nc))
    
    return count

def max_reachable(n, k, m, grid, starting_points):
    stones = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1]
    
    max_reach = 0

    for stone_comb in combinations(stones, m):
        new_grid = [row[:] for row in grid]
        
        for r, c in stone_comb:
            new_grid[r][c] = 0

        reach = bfs(new_grid, starting_points, n)

        max_reach = max(max_reach, reach)
    
    return max_reach


n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starting_points = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

print(max_reachable(n, k, m, grid, starting_points))