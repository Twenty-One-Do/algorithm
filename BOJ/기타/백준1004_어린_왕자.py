'''
2
-5 1 12 1
7
1 1 8
-3 -1 1
2 2 2
5 5 1
-4 5 1
12 1 1
12 1 2
-5 1 5 1
1
0 0 2

3
0
'''
t = int(input())
res = []
for _ in range(t):
    s_x,s_y, e_x,e_y = map(int,input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        p_x,p_y,p_r = map(int, input().split())
        s_in = (s_x-p_x)**2+(s_y-p_y)**2 < p_r**2
        e_in = (e_x-p_x)**2+(e_y-p_y)**2 < p_r**2
        if (s_in or e_in) and not all([s_in,e_in]):
            cnt+=1
    res.append(cnt)
for r in res:
    print(r)
    