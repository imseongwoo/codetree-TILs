import heapq

n = int(input())
pq = []
for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(pq, x)
    else:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)