n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
herb = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

herb_dx = [-1, -1, 1, 1]
herb_dy = [-1, 1, -1, 1]

ans = 0

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 나무 성장
def grow_tree():
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:  # 나무가 있는 경우만 처리
                cnt = 0
                for a in range(4):
                    nx = i + dx[a]
                    ny = j + dy[a]
                    if is_range(nx, ny) and arr[nx][ny] > 0:  # 주변에 나무가 있을 때만 카운트
                        cnt += 1
                arr[i][j] += cnt

# 나무 번식
def breed_tree():
    global arr
    narr = [row[:] for row in arr]  # 배열 복사
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:  # 나무가 있는 경우
                cnt = 0
                breed_xy = []
                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if is_range(nx, ny) and arr[nx][ny] == 0 and herb[nx][ny] == 0:  # 빈 칸이면서 제초제가 없는 칸
                        cnt += 1
                        breed_xy.append((nx, ny))
                if cnt > 0:  # 번식할 칸이 있을 때만
                    breed_n = arr[i][j] // cnt
                    for x, y in breed_xy:
                        narr[x][y] += breed_n
    arr = narr

# 제초제 투하
def throw_herb():
    global ans
    max_herb_cnt = 0
    max_x, max_y = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:  # 나무가 있는 칸만 계산
                herb_n = arr[i][j]
                # 대각선으로 제초제 확산
                for a in range(4):
                    nx, ny = i, j
                    for _ in range(k):
                        nx, ny = nx + herb_dx[a], ny + herb_dy[a]
                        if not is_range(nx, ny) or arr[nx][ny] == -1:  # 범위를 벗어나거나 벽에 부딪히면 멈춤
                            break
                        herb_n += arr[nx][ny] if arr[nx][ny] > 0 else 0  # 나무가 있는 경우에만 카운트
                        if arr[nx][ny] == 0:  # 빈 칸일 때 확산 멈춤
                            break

                if max_herb_cnt < herb_n:  # 박멸된 나무 수가 최대일 경우
                    max_herb_cnt = herb_n
                    max_x = i
                    max_y = j

    ans += max_herb_cnt

    # 제초제 뿌리기
    if arr[max_x][max_y] > 0:
        arr[max_x][max_y] = 0  # 해당 칸 나무 제거
        herb[max_x][max_y] = c  # 제초제 남은 기간 설정

    for a in range(4):  # 대각선 방향으로 제초제 확산
        nx, ny = max_x, max_y
        for _ in range(k):
            nx, ny = nx + herb_dx[a], ny + herb_dy[a]
            if not is_range(nx, ny) or arr[nx][ny] == -1:  # 범위를 벗어나거나 벽이면 멈춤
                break
            if arr[nx][ny] == 0:  # 빈 칸일 경우 제초제만 뿌리고 확산 멈춤
                herb[nx][ny] = c
                break
            arr[nx][ny] = 0  # 나무 제거
            herb[nx][ny] = c  # 제초제 뿌리기

# 제초제 기간 1년 감소
def delete_herb():
    for i in range(n):
        for j in range(n):
            if herb[i][j] > 0:
                herb[i][j] -= 1

# 시뮬레이션 진행
for _ in range(m):
    grow_tree()      # 1단계: 나무 성장
    breed_tree()     # 2단계: 나무 번식
    delete_herb()    # 3단계: 제초제 기간 감소
    throw_herb()     # 4단계: 제초제 투하

print(ans)