'''
<예제>
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
<정답>
5
1
'''
# T = int(input())
# res = []
# for _ in range(T):
#     x, y, n = list(map(int, input().split()))
#     field = [[0 for _ in range(x+2)] for _ in range(y+2)]
#     count, cabbage, is_visited = 0, [], []

#     for _ in range(n):
#         x, y = list(map(int, input().split()))
#         cabbage.append((x+1,y+1))
#         field[y+1][x+1] = 1

#     for c in cabbage:
#         if field[c[1]][c[0]] == 0:
#             continue
#         queue = []
#         target = c
#         while True:
#             x, y = target[0], target[1]
#             if field[y][x] != 0:
#                 field[y][x] = 0
#                 queue = [(x-1, y),(x+1, y),(x, y-1),(x, y+1)] + queue

#             if queue:
#                 target = queue.pop()
#             else:
#                 count+=1
#                 break
#     res.append(count)

# for r in res:
#     print(r)


# from collections import deque
# import sys

# diff = [(-1,0), (1,0), (0,-1), (0,1)]

# for _ in range(int(input())):
#     _, _, n = map(int, input().split())
#     count, cabbage = 0, []

#     for _ in range(n):
#         x, y = map(int, sys.stdin.readline().split())
#         cabbage.append((x,y))

#     queue = deque([])
#     while cabbage:
#         queue.appendleft(cabbage.pop())
#         while queue:
#             now = queue.pop()
#             for d in diff:
#                 new = (now[0]+d[0], now[1]+d[1])
#                 if new in cabbage: # 범인
#                     cabbage.remove(new) # 범인
#                     queue.appendleft(new)
#         count+=1
#     print(count)

from collections import deque
import sys

diff = [(-1,0), (1,0), (0,-1), (0,1)]

for _ in range(int(input())):
    x, y, n = map(int, input().split())
    count, cabbage = 0, []
    field = [[0]*(x+2) for _ in range(y+2)]

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        field[y+1][x+1] = 1
        cabbage.append((x+1,y+1))

    queue = deque([])
    while cabbage:
        start = cabbage.pop()
        if field[start[1]][start[0]] == 0:
            continue
        else:
            queue.appendleft(start)
            field[start[1]][start[0]] = 0
            while queue:
                now = queue.pop()
                for d in diff:
                    new = (now[0]+d[0], now[1]+d[1])
                    if field[new[1]][new[0]] != 0:
                        field[new[1]][new[0]] = 0 
                        queue.appendleft(new)
            count+=1
    print(count)