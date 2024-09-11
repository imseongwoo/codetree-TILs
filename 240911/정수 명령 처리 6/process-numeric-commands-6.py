import heapq

n = int(input())
pq = []

for _ in range(n):
    command = input()

    if command.startswith("push"):
        x = int(command.split()[1])
        heapq.heappush(pq, -x)
    elif command == "pop":
        print(-heapq.heappop(pq))
    elif command == "size":
        print(len(pq))
    elif command == "empty":
        if not pq:
            print(1)
        else: print(0)
    else:
        print(-pq[0])