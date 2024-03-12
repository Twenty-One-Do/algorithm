from itertools import combinations, permutations

n, m = list(map(int,input().split()))
res = []
for c in combinations(range(1,n+1),m):
    for p in permutations(c):
        res.append(p)
res.sort(key=lambda x: x)
for r in res:
    print(*r)
######################################
n, m = map(int, input().split())
nums = []


def find_nums():
    if len(nums) == m:
        str_nums = list(map(str, nums))
        print(" ".join(str_nums))
        return

    for num in range(1, n + 1):
        if num not in nums:
            nums.append(num)
            find_nums()
            nums.pop()


find_nums()