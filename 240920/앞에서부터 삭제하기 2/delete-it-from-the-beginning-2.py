import heapq

n = int(input())
arr = list(map(int, input().split()))
average = []

for k in range(n - 2):
    pq = []
    tmp = arr[k + 1:n]
    for a in tmp:
        heapq.heappush(pq, a)
    avg = (sum(pq) - pq[0]) / (len(pq) - 1)
    heapq.heappush(average, -avg)

print(f"{-average[0]:.2f}")