n = int(input())

d = [0]*(n+1)
d[0], d[1] = 1, 2

for i in range(2, n+1):
    d[i] = (d[i-1]*2 + d[i-2]*3) % 1000000007
    for j in range(i-3, -1, -1): 
        d[i] = (d[i] + d[j]*2) % 1000000007

print(d[n])