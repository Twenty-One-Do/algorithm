'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

12
'''

m, n = map(int,input().split())
arr = [None for _ in range(m)]
for row in range(m):
    arr[row] = [1 if s == 'W' else -1 for s in input()]
    if row%2 == 1:
        arr[row] = [-1 * a for a in arr[row]]

min_change = float('inf')
for r in range(m-7):
    for c in range(n-7):
        w_sum, b_sum = 0, 0
        for i in range(8*8):
            tmp = arr[r+i//8][c+i%8]
            if i % 2 == 0:
                if tmp == 1:
                    b_sum+=1
                else:
                    w_sum+=1
            else:
                if tmp == 1:
                    w_sum+=1
                else:
                    b_sum+=1
        min_sum = min(w_sum, b_sum)
        if min_change > min_sum:
            min_change = min_sum

print(min_change)