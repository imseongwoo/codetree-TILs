from collections import deque


def bfs(grid, starting_points, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * n for _ in range(n)]
    queue = deque(starting_points)
    for r, c in starting_points:
        visited[r][c] = True

    reachable_count = 0

    while queue:
        r, c = queue.popleft()
        reachable_count += 1

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and grid[new_r][new_c] == 0:
                visited[new_r][new_c] = True
                queue.append((new_r, new_c))

    return reachable_count


def main():
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    starting_points = []
    for _ in range(k):
        r, c = map(int, input().split())
        starting_points.append((r - 1, c - 1))

    result = bfs(grid, starting_points, n)
    print(result)

if __name__ == "__main__":
    main()