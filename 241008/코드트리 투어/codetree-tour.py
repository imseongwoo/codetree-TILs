# 1. 0번 도시에서 출발
# 2. revenue - cost가 최대인 상품
# 3. cost는 현재 여행 상품의 출발지로부터 dest까지 도달하기 위한 최단거리
# 4. 도달하는 것이 불가능 or 최단거리 값이 revenue보다 클 경우 판매 불가 상품
# 5. 판매 가능 삼품 중 우선순위가 높은 상품의 id 출력 후 제거 판매 가능 상품 없으면 -1

import heapq

INF = float('inf')
graph = []
distance = []
N, M = 0, 0
pq = []

isDeleted = [0] * 30001


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
    profit = revenue - distance[dest]
    heapq.heappush(pq, (-profit, id, revenue, dest))

def removeProduct(id):
    isDeleted[id] = 1

def sellProduct():
    ans = -1
    temp = []
    while pq:
        profit, id, revenue, dest = heapq.heappop(pq)
        profit = -profit
        if isDeleted[id]:
            continue
        elif profit < 0:
            heapq.heappush(pq, (-profit, id, revenue, dest))
            for item in temp:
                heapq.heappush(pq, item)
            break
        else:
            ans = id
            isDeleted[id] = 1
            break
        temp.append((-profit, id, revenue, dest))
    else:
        for item in temp:
            heapq.heappush(pq, item)
    print(ans)


def modifyDijkstraStartNode(s):
    dijkstra(s)
    products = []
    while pq:
        products.append(heapq.heappop(pq))

    for profit, id, revenue, dest in products:
        if not isDeleted[id]:
            addProduct(id, revenue, dest)


def main():
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        t = query[0]

        if t == 100:
            # 건물 생성 함수 실행
            buildLand(query[1], query[2], query[3:])
            # 다익스트라 실행
            dijkstra(0)
        elif t == 200:
            # 상품 추가 함수
            id = query[1]
            revenue = query[2]
            dest = query[3]
            addProduct(id, revenue, dest)
        elif t == 300:
            # 상품 제거 함수
            id = query[1]
            removeProduct(id)
        elif t == 400:
            # 상품 판매 함수
            sellProduct()
        elif t == 500:
            # 출발지 변경 함수
            s = query[1]
            modifyDijkstraStartNode(s)


if __name__ == '__main__':
    main()