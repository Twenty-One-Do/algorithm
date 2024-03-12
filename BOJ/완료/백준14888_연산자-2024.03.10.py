# OPERATORS = {0:lambda x, y: x + y, 
#              1:lambda x, y: x - y, 
#              2:lambda x, y: x * y, 
#              3:lambda x, y: x // y}

# def get_res(i):
#     global opers, values, _max, _min, n
#     if i == n-1:
#         res = values[0]
#         for oper, value in zip(opers, values[1:]):
#             res = OPERATORS[oper](res, value)

#         if _max < res:
#             _max = res
#         if _min > res:
#             _min = res
        
#     for j in range(i, n):
#         opers[i], opers[j] = opers[j], opers[i]
#         get_res(i+1)
#         opers[i], opers[j] = opers[j], opers[i]

# n = int(input())
# values = list(map(int,input().split()))
# opers = []
# for idx, o in enumerate(list(map(int,input().split()))):
#     opers+=[idx for _ in range(o)]
# _max,_min = 0, float('inf')
# get_res(0)
# print(_max)
# print(_min)

OPERATORS = {0:lambda x, y: x + y, 
             1:lambda x, y: x - y, 
             2:lambda x, y: x * y, 
             3:lambda x, y: x // y}

n = int(input())
values = list(map(int,input().split()))
opers = []
for idx, o in enumerate(list(map(int,input().split()))):
    opers+=[(idx, i) for i in range(o)]
_max,_min = -1e9, float('inf')

def get_res(oper_seq):
    global _max,_min
    if len(oper_seq) == n-1:
        res = values[0]
        for oper, value in zip(oper_seq, values[1:]):
            if oper[0] == 3 and res < 0:
                res = -OPERATORS[oper[0]](-res,value)
            else:
                res = OPERATORS[oper[0]](res,value)
        if _max<res:
            _max = res
        if _min > res:
            _min = res
        return

    for oper in opers:
        if oper not in oper_seq:
            can_i_append = True
            for compare in oper_seq:
                if compare[0] == oper[0] and compare[1] > oper[1]:
                    can_i_append = False
            if can_i_append:
                oper_seq.append(oper)
                get_res(oper_seq)
                oper_seq.pop()

get_res([])
print(_max)
print(_min)