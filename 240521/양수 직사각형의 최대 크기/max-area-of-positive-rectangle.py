def largest_positive_rectangle(n, m, grid):
    max_area = -1  

    for start_row in range(n):
        for start_col in range(m):
            if grid[start_row][start_col] > 0:  
                for end_row in range(start_row, n):
                    for end_col in range(start_col, m):
                        all_positive = True
                        for i in range(start_row, end_row + 1):
                            for j in range(start_col, end_col + 1):
                                if grid[i][j] <= 0:
                                    all_positive = False
                                    break
                            if not all_positive:
                                break
                        if all_positive:
                            area = (end_row - start_row + 1) * (end_col - start_col + 1)
                            max_area = max(max_area, area)
    
    return max_area

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


result = largest_positive_rectangle(n, m, grid)

print(result)