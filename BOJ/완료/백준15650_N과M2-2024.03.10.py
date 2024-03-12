from itertools import combinations

n, m = list(map(int,input().split()))
res = []
for c in combinations(range(1,n+1),m):
    res.append(c)
res.sort(key=lambda x: x)
for r in res:
    print(*r)