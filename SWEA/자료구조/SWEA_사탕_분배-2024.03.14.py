'''
6
4 9 1
4 9 2
5 6 10000000
1000000000 99999999 2000000000
500 2001 2000000000
1 1 2000000

1
1 1000000000 2000000000
'''
import sys
T = int(input())

def bst_search(tree, value, idx, root):
    node = root
    while True:
        if node == value:
            return tree[node][0]
        elif node < value:
            next_node = tree[node][2]
            if next_node is None:
                tree[node][2] = value
                tree[value] = [idx,None,None]
                return False
            else:
                node = next_node
        else:
            next_node = tree[node][1]
            if next_node is None:
                tree[node][1] = value
                tree[value] = [idx,None,None]
                return False
            else:
                node = next_node


for test_case in range(1, T + 1):
    a, b, k = map(int,input().split())
    sum_candy = a+b
    is_zero = False
    root = a
    tree = {root:[0, None, None]}
    for k_num in range(1, k+1):
        if a == b:
            is_zero = True
            break
        elif a>b:
            a, b = a-b, 2*b
        else:
            a, b = 2*a, b-a
        res = bst_search(tree, a, k_num, root)
        if res:
            break

    if is_zero:
        print(f'#{test_case} 0')
    else:
        if k != k_num:
            find_idx = k%k_num+res
            for (key, v) in tree.items():
                if v[0] == find_idx:
                    a = key
                    break
        b = sum_candy-a
        print(f'#{test_case} {min(a,b)}')