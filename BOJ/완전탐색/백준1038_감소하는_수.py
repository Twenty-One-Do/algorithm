'''
18

42
'''
from itertools import combinations
n = int(input())
count, digit, find = 1, 0, False
if n == 0:
    print(0)
else:
    while not find:
        digit+=1
        if digit == 11:
            print(-1)
            break
        for f_num in range(1,10):
            combi_list = sorted(list(combinations(range(0,f_num), digit-1)),key=lambda x: x[::-1])
            for combi in combi_list:
                
                if count == n:
                    print(str(f_num)+''.join(list(map(str,combi))[::-1]))
                    find = True
                    break
                else:
                    count+=1
            if find: break