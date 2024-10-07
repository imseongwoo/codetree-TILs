from collections import deque

N_large = 5  # 고대 문명 전체 격자 크기입니다.
N_small = 3  # 회전시킬 격자의 크기입니다.

# 격자의 범위 안에 있는지 확인하는 함수입니다.
def in_range(y, x):
    return 0 <= y < N_large and 0 <= x < N_large

# 현재 격자에서 sy, sx를 좌측상단으로 하여 시계방향 90도 회전을 cnt번 시행했을때 결과를 return 합니다.
def rotate(board, sy, sx, cnt):
    result = [row[:] for row in board]
    for _ in range(cnt):
        # 시계방향으로 90도 회전
        tmp = result[sy + 0][sx + 2]
        result[sy + 0][sx + 2] = result[sy + 0][sx + 0]
        result[sy + 0][sx + 0] = result[sy + 2][sx + 0]
        result[sy + 2][sx + 0] = result[sy + 2][sx + 2]
        result[sy + 2][sx + 2] = tmp
        tmp = result[sy + 1][sx + 2]
        result[sy + 1][sx + 2] = result[sy + 0][sx + 1]
        result[sy + 0][sx + 1] = result[sy + 1][sx + 0]
        result[sy + 1][sx + 0] = result[sy + 2][sx + 1]
        result[sy + 2][sx + 1] = tmp
    return result

# 유물 획득 점수를 계산하는 함수
def cal_score(board):
    score = 0
    visit = [[False for _ in range(N_large)] for _ in range(N_large)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(N_large):
        for j in range(N_large):
            if not visit[i][j]:
                q, trace = deque([(i, j)]), deque([(i, j)])
                visit[i][j] = True
                while q:
                    cur = q.popleft()
                    for k in range(4):
                        ny, nx = cur[0] + dy[k], cur[1] + dx[k]
                        if in_range(ny, nx) and board[ny][nx] == board[cur[0]][cur[1]] and not visit[ny][nx]:
                            q.append((ny, nx))
                            trace.append((ny, nx))
                            visit[ny][nx] = True
                if len(trace) >= 3:
                    score += len(trace)
                    while trace:
                        t = trace.popleft()
                        board[t[0]][t[1]] = 0
    return score

# 비어있는 곳에 새로운 조각을 채우는 함수
def fill(board, que):
    for j in range(N_large):
        for i in reversed(range(N_large)):
            if board[i][j] == 0:
                board[i][j] = que.popleft()

def main():
    # 입력 받기
    K, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N_large)]
    q = deque(map(int, input().split()))

    # 최대 K번 탐사 과정
    for _ in range(K):
        maxScore = 0
        maxScoreBoard = None

        # 회전 후 최대 점수 찾기
        for cnt in range(1, 4):
            for sx in range(N_large - N_small + 1):  # sx = 0,1,2
                for sy in range(N_large - N_small + 1):
                    rotated = rotate(board, sy, sx, cnt)
                    score = cal_score(rotated)  # Pass the rotated board directly
                    if maxScore < score:
                        maxScore = score
                        maxScoreBoard = rotated

        if maxScoreBoard is None:
            break
        board = maxScoreBoard  # Set board to the rotated board with max score

        while True:
            fill(board, q)
            newScore = cal_score(board)
            if newScore == 0:
                break
            maxScore += newScore

        print(maxScore, end=" ")

if __name__ == '__main__':
    main()