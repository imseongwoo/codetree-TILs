def max_sum_of_two_rectangles(n, m, grid):
    def calculate_sum(x1, y1, x2, y2):
        return sum(grid[i][j] for i in range(x1, x2+1) for j in range(y1, y2+1))

    max_sum = float('-inf')

    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    sum1 = calculate_sum(x1, y1, x2, y2)

                    for x3 in range(n):
                        for y3 in range(m):
                            for x4 in range(x3, n):
                                for y4 in range(y3, m):

                                    if (x4 < x1 or x3 > x2 or y4 < y1 or y3 > y2):
                                        sum2 = calculate_sum(x3, y3, x4, y4)
                                        max_sum = max(max_sum, sum1 + sum2)

    return max_sum

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
grid = []
index = 2
for i in range(n):
    grid.append([int(data[index + j]) for j in range(m)])
    index += m

print(max_sum_of_two_rectangles(n, m, grid))