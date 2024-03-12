n = int(input())
res = 0
for _ in range(n):
    stack = []
    for s in input():
        if len(stack) == 0 or stack[-1] != s:
            stack.append(s)
        elif stack[-1] == s:
            stack.pop()
    if len(stack) == 0:
        res += 1

print(res)