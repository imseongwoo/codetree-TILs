def max_of_min_path(matrix, N):
    # DP 테이블 초기화
    dp = [[0] * N for _ in range(N)]
    
    # 첫 번째 셀 초기화
    dp[0][0] = matrix[0][0]
    
    # 첫 번째 행 채우기 (오직 왼쪽에서 올 수 있음)
    for j in range(1, N):
        dp[0][j] = min(dp[0][j-1], matrix[0][j])
    
    # 첫 번째 열 채우기 (오직 위에서 올 수 있음)
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][0], matrix[i][0])
    
    # 나머지 DP 테이블 채우기
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(
                min(dp[i-1][j], matrix[i][j]),  # 위에서 오는 경우
                min(dp[i][j-1], matrix[i][j])   # 왼쪽에서 오는 경우
            )
    
    # 결과는 우하단에 저장됨
    return dp[N-1][N-1]

# 입력 처리
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산 및 출력
result = max_of_min_path(matrix, N)
print(result)