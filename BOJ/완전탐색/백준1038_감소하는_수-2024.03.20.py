'''
18

42
'''
## iterrools 사용 구현
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


### 조합 직접 구현
# def get_combi(i, arr, r, tmp, res):
#     if r == 0:
#         res.append([])
#     else:
#         for idx in range(i, len(arr)):
#             tmp.append(arr[idx])
#             if len(tmp) == r:
#                 res.append(tmp.copy())
#             else:
#                 get_combi(idx+1, arr, r, tmp, res)
#             tmp.pop()

# n = int(input())
# count, digit, find = 1, 0, False
# if n == 0:
#     print(0)
# else:
#     while not find:
#         digit+=1
#         if digit == 11:
#             print(-1)
#             break
#         for f_num in range(1,10):
#             res = []
#             get_combi(0,range(0,f_num),digit-1,[], res)
#             combi_list = sorted(res, key=lambda x: x[::-1])
#             for combi in combi_list:
            
#                 if count == n:
#                     print(str(f_num)+''.join(list(map(str,combi))[::-1]))
#                     find = True
#                     break
#                 else:
#                     count+=1
#             if find: break


## 비트마스킹
# def get_combi(arr, r):
#     res = []
#     for i in range(2**len(arr)):
#         mask = bin(i).split('b')[-1].zfill(len(arr))
#         if mask.count('1') == r:
#             res.append([a for m, a in zip(mask,arr) if m == '1'])
#     return res

# n = int(input())
# count, digit, find = 1, 0, False
# if n == 0:
#     print(0)
# else:
#     while not find:
#         digit+=1
#         if digit == 11:
#             print(-1)
#             break
#         for f_num in range(1,10):

#             res = get_combi(range(0,f_num),digit-1)
#             combi_list = sorted(res, key=lambda x: x[::-1])
#             for combi in combi_list:
            
#                 if count == n:
#                     print(str(f_num)+''.join(list(map(str,combi))[::-1]))
#                     find = True
#                     break
#                 else:
#                     count+=1
#             if find: break