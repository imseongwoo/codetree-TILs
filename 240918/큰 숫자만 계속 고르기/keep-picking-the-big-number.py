import heapq

pq = []
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for a in arr:
    heapq.heappush(pq, -a)

for _ in range(m):
    max_num = heapq.heappop(pq)
    heapq.heappush(pq, max_num + 1)

print(-pq[0])