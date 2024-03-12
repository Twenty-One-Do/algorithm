# # DFS의 풀이
# n, m = list(map(int,input().split()))
# maze= [[0 for _ in range(m+2)] for _ in range(n+2)]

# for i in range(n):
#     for s_i, s in enumerate(input()):
#         maze[i+1][s_i+1] = int(s)

# min_path = n*m - (n-2)*(m-2)
# minimum_path = n+m-1
# def get_path(x, y, trail):
#     global min_path
#     now_len = len(trail)
#     if min_path == minimum_path:
#         return
#     if x==n and y == m and min_path>now_len:
#         min_path = now_len
#         return
#     elif now_len>=min_path: # 가망없음
#         return
#     else:
#         for point in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
#             if point not in trail and maze[point[0]][point[1]] != 0:
#                 trail+=[point]
#                 get_path(*point, trail)
#                 trail.pop()

# get_path(1,1,[(1,1)])

# print(min_path)

#메모이제이션은?

n, m = list(map(int,input().split()))
maze= [[0 for _ in range(m+2)] for _ in range(n+2)]
shortest= [[float('inf') for _ in range(m+2)] for _ in range(n+2)]

for i in range(n):
    for s_i, s in enumerate(input()):
        maze[i+1][s_i+1] = int(s)

shortest[1][1] = 1

def get_path(x, y, is_visited):
    if x == y == 1:
        return shortest[1][1]
    elif maze[x][y] != 0: # 벽이 아니면
        candidates = []
        for point in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if point not in is_visited:
                is_visited.append((x,y))
                candidates.append(get_path(*point,is_visited))
                is_visited.pop()
            else:
                return shortest[point[0]][point[1]]

        shortest[x][y] = min(candidates)+1
        return shortest[x][y]
    else: # 벽이면
        return float('inf')
get_path(n,m, [])
print(shortest[n][m])

'''
4 6
110110
110110
111111
111101

5 5
11111
11111
11111
11111
11111
'''