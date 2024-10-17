from collections import deque

def bfs(grid, n):
    # 네 방향 (위, 아래, 왼쪽, 오른쪽) 이동을 위한 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 거리 테이블을 -1로 초기화 (이동할 수 없는 경우를 의미)
    distance = [[-1] * n for _ in range(n)]
    
    # BFS를 위한 큐 초기화
    queue = deque()
    
    # 비를 피할 수 있는 장소 (숫자 3)에서 BFS 시작
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                queue.append((i, j, 0))  # (행, 열, 거리)
    
    # BFS 수행
    while queue:
        x, y, dist = queue.popleft()
        
        # 이미 방문한 곳은 무시
        if distance[x][y] != -1:
            continue
        
        # 현재 위치의 거리를 기록
        distance[x][y] = dist
        
        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 1 and distance[nx][ny] == -1:
                queue.append((nx, ny, dist + 1))
    
    return distance

def solve_rain_avoidance(n, grid):
    # 각 위치에서 비를 피할 수 있는 장소까지의 최소 거리를 구함
    distance_from_shelter = bfs(grid, n)
    
    result = []
    
    # 결과 생성: 사람이 있는 위치에 대해 최소 거리를 계산
    for i in range(n):
        row_result = []
        for j in range(n):
            if grid[i][j] == 2:
                # 사람이 있는 위치에 대해 결과 출력 (비 피할 수 있는 장소까지의 거리)
                row_result.append(distance_from_shelter[i][j])
            else:
                # 사람이 없는 위치는 0으로 출력
                row_result.append(0)
        result.append(row_result)
    
    return result

# 입력 처리
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 계산
result = solve_rain_avoidance(n, grid)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))