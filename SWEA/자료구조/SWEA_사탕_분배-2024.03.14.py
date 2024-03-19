'''
6
4 9 1
4 9 2
5 6 10000000
500 2001 2000000000
1 1 2000000
1 1000000000 2000000000

1
500 2000 2000000000
'''

# T = int(input())

# def search(log, value, k_num, root):
#     now = root
#     while True:
#         if now == value:
#             return log[now][0]
#         elif now < value:
#             next = log[now][-1]
#             if next == 0:
#                 log[now][-1] = value
#                 log[value] = [k_num,0,0]
#                 return None
#             else:
#                 now = next
#         else:
#             next = log[now][1]
#             if next == 0:
#                 log[now][1] = value
#                 log[value] = [k_num,0,0]
#                 return None
#             else:
#                 now = next

# for test_case in range(1, T + 1):
#     a, b, k = map(int,input().split())
#     sum_candy = a+b
#     is_zero = False
#     root = min(a,b)
#     log = {root:[0,0,0]}

#     for k_num in range(1, k+1):
#         if a == b:
#             is_zero = True
#             break
#         elif a>b:
#             a, b = a-b, 2*b
#         else:
#             a, b = 2*a, b-a
        
#         min_val = min(a,b)
        
#         cycle_start = search(log,min_val,k_num,root)
#         if cycle_start is not None:
#             break

#     if is_zero:
#         print(f'#{test_case} 0')
#     else:
#         if k != k_num:
#             log = list(log.keys())
#             min_val = log[cycle_start+k%k_num]

#         print(f'#{test_case} {min_val}')

def division(n, _sum):
    if n == 0:
        return 1
    result = division(n // 2, _sum)
    result = (result * result) % _sum
    if n % 2 == 1:
        result = (result * 2) % _sum
    return result


def find(a, b, k):
    _sum = a + b
    result = (division(k, _sum) * a) % _sum
    return min(result, _sum - result)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, k = map(int, input().split())
        print("#{} {}".format(i + 1, find(a, b, k)))