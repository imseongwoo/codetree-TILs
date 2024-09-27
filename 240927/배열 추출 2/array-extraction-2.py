import heapq

n = int(input())
pq = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(pq, (abs(x), x))

    else:
        if not pq:
            print(0)
            continue
        _, v = heapq.heappop(pq)
        print(v)