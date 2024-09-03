# grid 입력
grid = [
    list(map(int, input().split()))
    for _ in range(4)
]
# order 입력
order = input()

# 함수들
# do_merge(o)
def do_merge(o):
    # 오른쪽으로 밀었다면,
    if o == 'R':
        # 전체 행을 조사
        for i in range(4):
            # 각 행에서
            for j in range(3, 0, -1):
                # 앞뒤가 같은 부분이 있으면,
                if grid[i][j] == grid[i][j-1]:
                    # 해당 부분은 2배가 되고,
                    grid[i][j] = grid[i][j] * 2
                    # 다음 부분은 0이됨
                    grid[i][j-1] = 0
                    # 다시 밀기
                    push(o)
    
 
    elif o == 'L':
        # 전체 행을 조사
        for i in range(4):
            # 각 행에서
            for j in range(3):
                # 앞뒤가 같은 부분이 있으면,
                if grid[i][j] == grid[i][j+1]:
                    # 해당 부분은 2배가 되고
                    grid[i][j] = grid[i][j] * 2
                    # 다음 부분은 0이 됨
                    grid[i][j+1] = 0
                    # 다시 밀어주기
                    push(o)
    
    # 위로 밀었다면,
    elif o == 'U':

        # 전체 열을 조사
        for i in range(4):
            # 각 열에서
            for j in range(3):
                # 앞 뒤가 같은 부분이 있으면
                if grid[j][i] == grid[j+1][i]:
                    # 해당 부분은 2배가 되고
                    grid[j][i] = grid[j+1][i] * 2
                    # 다음 부분은 0이 됨
                    grid[j+1][i] = 0
                    # 다시 밀어주기
                    push(o)
    
    # 아래쪽으로 밀었다면
    else:
        # 모든 열을 조사
        for i in range(4):
            # 각 열에서
            for j in range(3, 0, -1):
                # 앞 뒤가 같은 것을 찾으면
                if grid[j][i] == grid[j-1][i]:
                    # 해당 위치는 2배가 되고
                    grid[j][i] = grid[j][i] * 2
                    # 다음 위치는 0이 됨
                    grid[j-1][i] = 0
                    # 다시 밀어주기
                    push(o)


# 함수들
def push(o):
    
    # 오른쪽으로 밀 경우
    if o == 'R':
        # 전체 행을 조사
        for i in range(4):
            
            # temp
            temp = []
            
            # 해당 열에서
            for j in range(3, -1, -1):
                # 숫자가 있으면
                if grid[i][j]:
                    # temp에 추가
                    temp.append(grid[i][j])
            
            # shortage
            shortage = 4 - len(temp)
            for _ in range(shortage):
                temp.append(0)
            
            # grid의 각 행을 바꿔주기
            for j in range(4):
                grid[i][j] = temp[3-j]
    
    # 왼쪽으로 밀 경우
    elif o == 'L':
        # 전체 행을 조사
        for i in range(4):

            # temp
            temp = []

            # 해당 열에서
            for j in range(4):
                # 숫자가 있으면
                if grid[i][j]:
                    # temp에 추가
                    temp.append(grid[i][j])
            
            # shortage
            shortage = 4 - len(temp)
            for _ in range(shortage):
                temp.append(0)
            
            # grid 교체
            for j in range(4):
                grid[i][j] = temp[j]
    
    # 위로 밀 경우
    elif o == 'U':

        # 전체 열을 조사
        for i in range(4):
            
            # temp 
            temp = []
            
            # 해당행에서
            for j in range(4):
                # 숫자가 존재하면
                if grid[j][i]:
                    # temp에 추가
                    temp.append(grid[j][i])
            
            # shortage
            shortage = 4 - len(temp)
            for _ in range(shortage):
                temp.append(0)

            # grid 바꿔주기
            for j in range(4):
                grid[j][i] = temp[j]

    # 아래로 밀 경우
    else:

        # 모든 열을 조사
        for i in range(4):

            # temp
            temp = []

            # 각 행에서
            for j in range(3, -1, -1):
                # 숫자가 존재한다면
                if grid[j][i]:
                    # temp에 추가
                    temp.append(grid[j][i])
            
            # shortage
            shortage = 4 - len(temp)
            for _ in range(shortage):
                temp.append(0)
            
            # grid 바꿔주기
            for j in range(4):
                grid[j][i] = temp[3-j]


push(order)


do_merge(order)


for i in range(4):
    for j in range(4):
        print(grid[i][j], end= ' ')
    print()