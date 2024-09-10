from collections import deque
from itertools import combinations
from copy import deepcopy


def bfs(arr, start):
    global n
    visited = [[0] * n for _ in range(n)]
    queue = deque(start)
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for r, c in start:
        visited[r][c] = 1
        cnt += 1

    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1 and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                queue.append((nx,ny))
    return cnt

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start = []
stones = []
ans = 0

for _ in range(k):
    r, c = map(int, input().split())
    start.append((r - 1, c - 1))

# 돌 있는 좌표 저장
for a in range(n):
    for b in range(n):
        if arr[a][b] == 1:
            stones.append((a, b))

# m개의 돌을 치울 경우의 수에 따라 bfs 처리
for stone_comb in combinations(stones, m):
    new_arr = deepcopy(arr)

    for r, c in stone_comb:
        new_arr[r][c] = 0

    temp = bfs(new_arr, start)
    ans = max(ans, temp)

print(ans)