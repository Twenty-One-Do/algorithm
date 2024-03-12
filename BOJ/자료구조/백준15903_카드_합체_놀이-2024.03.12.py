import heapq
n, m = list(map(int,input().split()))
values = list(map(int,input().split()))
heapq.heapify(values)
for _ in range(m):
    res = heapq.heappop(values)+heapq.heappop(values)
    heapq.heappush(values, res)
    heapq.heappush(values, res)

print(sum(values))
