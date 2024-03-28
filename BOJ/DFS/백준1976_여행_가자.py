'''
5
5
0 1 0 0 0
1 0 0 0 0
0 0 0 1 0
0 0 1 0 1
0 0 0 1 0
3 5 4 2 1

NO

5
5
0 0 0 0 0
0 0 1 0 0
0 1 0 1 0
0 0 1 0 1
0 0 0 1 0
1 1 1 1 1
'''

def find_path(now, target, visited):
    global mat
    if mat[now-1][target-1] or now == target:
        return 1
    else:
        for node, is_connected in enumerate(mat[now-1]):
            if is_connected:
                node += 1
                if node not in visited:
                    visited.add(node)
                    res = find_path(node, target, visited)
                    if res:
                        return 1
        return 0

n = int(input())
t = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))
plan = list(map(int,input().split()))
is_path = True

for i in range(0,t-1):
    if not find_path(plan[i], plan[i+1], set([])):
        is_path = False
        break

if is_path:
    print('YES')
else:
    print('NO')
    