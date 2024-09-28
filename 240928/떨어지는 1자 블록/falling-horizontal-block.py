n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k -= 1  # 시작 열을 0 기반 인덱스로 조정
final_row = n - 1  # 블록이 맨 아래에 떨어진다고 가정

# 블록이 멈출 행을 찾는 로직
for row in range(n - 1):
    can_fall = True
    for i in range(k, k + m):
        if arr[row + 1][i] == 1:  # 블록이 장애물에 부딪히는지 확인
            final_row = row
            can_fall = False
            break
    if not can_fall:
        break

# 블록을 그리드에 배치
for i in range(k, k + m):
    arr[final_row][i] = 1

# 최종 그리드 상태 출력
for i in range(n):
    print(' '.join(map(str, arr[i])))