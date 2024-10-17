n = int(input())
dic = {}

def add(k,v):
    dic[k] = v
    

def remove(k):
    dic.pop(k)

def find(k):
    if k in dic:
        print(dic[k])
    else:
        print(None)



for _ in range(n):
    query = list(input().split())
    command = query[0]

    if command == "add":
        add(query[1], query[2])
    elif command == "remove":
        remove(query[1])
    else:
        find(query[1])