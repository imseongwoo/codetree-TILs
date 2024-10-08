import heapq

INF = float('inf')
graph = []
distance = []
N, M = 0, 0
pq = []

isDeleted = {}  # Use a dictionary to handle arbitrary IDs
packages = {}   # Store all products
S = 0           # Starting city

def buildLand(n, m, arr):
    global N, M, graph
    N = n
    M = m
    graph = [[INF] * N for _ in range(N)]
    for i in range(N):
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
    packages[id] = (revenue, dest)  # Store the product
    if distance[dest] == INF:
        return
    profit = revenue - distance[dest]
    if profit < 0:  # Include products with profit >= 0
        return
    heapq.heappush(pq, (-profit, id, revenue, dest))

def removeProduct(id):
    isDeleted[id] = True

def sellProduct():
    ans = -1

    while pq:
        profit, id, revenue, dest = heapq.heappop(pq)
        if isDeleted.get(id, False):
            continue
        else:
            ans = id
            isDeleted[id] = True  # Mark as sold
            break
    print(ans)

def modifyDijkstraStartNode(s):
    global S
    S = s
    dijkstra(S)
    pq.clear()
    for id, (revenue, dest) in packages.items():
        if not isDeleted.get(id, False):
            if distance[dest] == INF:
                continue
            profit = revenue - distance[dest]
            if profit < 0:
                continue
            heapq.heappush(pq, (-profit, id, revenue, dest))

def main():
    import sys
    input_lines = sys.stdin.read().split()
    q = int(input_lines[0])
    idx = 1

    for _ in range(q):
        t = int(input_lines[idx])
        idx += 1

        if t == 100:
            n = int(input_lines[idx])
            m = int(input_lines[idx + 1])
            idx += 2
            needed_numbers = 3 * m
            arr = []
            for _ in range(needed_numbers):
                arr.append(int(input_lines[idx]))
                idx += 1
            buildLand(n, m, arr)
            S = 0
            dijkstra(S)
        elif t == 200:
            id = int(input_lines[idx])
            revenue = int(input_lines[idx + 1])
            dest = int(input_lines[idx + 2])
            idx += 3
            addProduct(id, revenue, dest)
        elif t == 300:
            id = int(input_lines[idx])
            idx += 1
            removeProduct(id)
        elif t == 400:
            sellProduct()
        elif t == 500:
            s = int(input_lines[idx])
            idx += 1
            modifyDijkstraStartNode(s)

if __name__ == '__main__':
    main()