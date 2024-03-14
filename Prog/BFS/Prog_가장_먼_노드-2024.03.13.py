'''
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
'''
def solution(n, edge):
    graph = {number:[] for number in range(1,n+1)}
    shortest = [float('inf') for _ in range(n)]
    for e in edge:
        graph[e[0]].append(e[-1])
        graph[e[-1]].append(e[0])

    shortest[0] = 1
    queue = [1]
    while queue:
        now = queue.pop()
        for node in graph[now]:
            if shortest[now-1] + 1 < shortest[node-1]:
                shortest[node-1] = shortest[now-1] + 1
                queue = [node] + queue
    answer = shortest.count(max(shortest))
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])