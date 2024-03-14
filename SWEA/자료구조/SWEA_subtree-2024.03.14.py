T = int(input())

for test_case in range(1, T + 1):
    e, n = map(int,input().split())
    edges = list(map(int,input().split()))
    tree = {n:[] for n in set(edges)}
    for i in range(e):
        tree[edges[i*2]].append(edges[i*2+1])

    queue = [n]
    cnt = 0
    while queue:
        cnt+=1
        now = queue.pop()
        queue = tree[now]+queue
    print(f'#{test_case} {cnt}')