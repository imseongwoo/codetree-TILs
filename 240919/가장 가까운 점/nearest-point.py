import heapq

n, m = map(int, input().split())
points = []
pq = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

for point in points:
    x = point[0]
    y = point[1]
    heapq.heappush(pq, ((abs(x) + abs(y)), x, y))

for _ in range(m):
    near_point = heapq.heappop(pq)
    temp_x = near_point[1] + 2
    temp_y = near_point[2] + 2
    heapq.heappush(pq, ((abs(temp_x) + abs(temp_y)), temp_x, temp_y))

print(pq[0][1], pq[0][2])