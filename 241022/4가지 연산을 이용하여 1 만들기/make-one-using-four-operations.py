from collections import deque

n = int(input())
visited = [0] * 10000002

q = deque()
q.append((n,0))
visited[n] = 1
operator = [1, -1, 2, 3]
cnt = 0

while q:
    num, level = q.popleft()

    if num == 1:
        print(level)
        break

    for i in range(4):
        new_num = 0
        if i==2 or i==3:
            if (num % operator[i]) == 0:
                new_num = num // operator[i]
            else:
                continue
        else:
            new_num = num + operator[i]
        if visited[new_num] == 0:
            q.append((new_num, level + 1))
            visited[new_num] = 1
    cnt += 1