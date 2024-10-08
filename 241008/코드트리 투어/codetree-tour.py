import heapq
import sys

INF = float('inf')
graph = []
distance = []
N, M = 0, 0
pq = []

isDeleted = [0] * 30005
packages = {}  # Dictionary to store all packages
S = 0  # Starting city

def buildLand(n, m, arr):
    global N, M, graph
    N = n
    M = m
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for i in range(m):
        u, v, w = arr[i * 3], arr[i * 3 + 1], arr[i * 3 + 2]
        graph[u][v] = min(graph[u][v], w)
        graph[v][u] = min(graph[v][u], w)

def dijkstra(start):
    global distance
    distance = [INF] * N
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in range(N):
            if graph[now][i] != INF:
                cost = dist + graph[now][i]

                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

def addProduct(id, revenue, dest):
    packages[id] = (revenue, dest)
    if distance[dest] == INF:
        return
    profit = revenue - distance[dest]
    if profit < 0:
        return
    heapq.heappush(pq, (-profit, id, revenue, dest))

def removeProduct(id):
    isDeleted[id] = 1

def sellProduct():
    ans = -1

    while pq:
        profit, id, revenue, dest = heapq.heappop(pq)
        if isDeleted[id]:
            continue
        elif -profit < 0:
            break
        else:
            ans = id
            break

    print(ans)

def modifyDijkstraStartNode(s):
    global S
    S = s
    dijkstra(S)
    # Clear the priority queue
    pq.clear()
    # Re-add all packages
    for id, (revenue, dest) in packages.items():
        if not isDeleted[id]:
            if distance[dest] == INF:
                continue
            profit = revenue - distance[dest]
            if profit <= 0:
                continue
            heapq.heappush(pq, (-profit, id, revenue, dest))

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        query = list(map(int, sys.stdin.readline().split()))
        t = query[0]

        if t == 100:
            # Build the land
            buildLand(query[1], query[2], query[3:])
            # Run Dijkstra from city 0
            S = 0  # Starting city is 0
            dijkstra(S)
        elif t == 200:
            # Add product
            id = query[1]
            revenue = query[2]
            dest = query[3]
            addProduct(id, revenue, dest)
        elif t == 300:
            # Remove product
            id = query[1]
            removeProduct(id)
        elif t == 400:
            # Sell product
            sellProduct()
        elif t == 500:
            # Change starting city
            s = query[1]
            modifyDijkstraStartNode(s)

if __name__ == '__main__':
    main()