from collections import deque

n, turn = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 위치
ans_x = sx
ans_y = sy

for _ in range(turn):
    max_num = -1  # 비교를 위한 초기 값 설정 (불가능한 작은 값)
    visited = [[False]*n for _ in range(n)]  # 방문 여부를 체크하기 위한 배열
    
    q = deque()
    q.append([ans_x, ans_y])  # BFS의 시작점은 현재 위치
    visited[ans_x][ans_y] = True  # 시작 위치를 방문 처리
    
    # 이동할 최종 위치를 추적
    new_x, new_y = ans_x, ans_y  # 이동할 곳이 없으면 현재 위치 유지
    
    while q:
        now_x, now_y = q.pop()
        
        # 상하좌우 4방향 탐색
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            
            # 유효한 범위 안에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않았고, 현재 위치보다 작은 숫자가 있는 경우만 탐색
                if not visited[nx][ny] and ground[nx][ny] < ground[ans_x][ans_y]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    
                    # 이동할 최댓값을 우선 선택하고, 동일한 값일 경우 행과 열을 기준으로 선택
                    if ground[nx][ny] > max_num:
                        max_num = ground[nx][ny]
                        new_x, new_y = nx, ny
                    elif ground[nx][ny] == max_num:
                        if new_x > nx:  # 행을 우선
                            new_x, new_y = nx, ny
                        elif new_x == nx and new_y > ny:  # 같은 행일 경우 열을 우선
                            new_x, new_y = nx, ny

    # 최종 위치를 갱신
    ans_x, ans_y = new_x, new_y

# 최종 위치 출력 (1-based 인덱스로 변환)
print(f'{ans_x+1} {ans_y+1}')