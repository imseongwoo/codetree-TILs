n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

visited_nums = []

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num

def simulate():
    global curr_x, curr_y
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y
            return True

    return False

visited_nums.append(a[curr_x][curr_y])
while True:
    greater_number_exist = simulate()
    
    if not greater_number_exist:
        break
    
    visited_nums.append(a[curr_x][curr_y])

for num in visited_nums:
    print(num, end=' ')