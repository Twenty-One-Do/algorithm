'''
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
'''
def solution(n, edge):
    answer = 0
    games = {number:[] for number in range(1,n+1)}
    for res in edge:
        games[res[0]].append(res[1])
        games[res[1]].append(-res[0])
    visited = []
    queue = []
    for player in range(1,n+1):

        if player in visited:
            continue

        queue.append(player)
        while queue:
            now = queue.pop()
            for next in games[now]:
                if next > 0:
                    pass
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])