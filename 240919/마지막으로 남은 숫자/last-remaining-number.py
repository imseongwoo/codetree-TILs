import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []
for a in arr:
    heapq.heappush(pq, -a)

while len(pq) >= 2:
    a = -heapq.heappop(pq)
    b = -heapq.heappop(pq)

    if a == b:
        continue
    else:
        heapq.heappush(pq, b-a)

if pq:
    print(-pq[0])
else:
    print(-1)