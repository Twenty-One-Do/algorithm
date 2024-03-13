import heapq
def solution(n, edge):
    graph = {number:[] for number in range(1,n)}
    for e in edge:
        graph[e[0]].append(e[-1])
        graph[e[-1]].append(e[0])
    
    now = 1
    queue, visited = [], []
    while True:
        if now not in visited:
            visited.append(now)
            queue = graph[now] + queue
        now = queue.pop()
    return answer