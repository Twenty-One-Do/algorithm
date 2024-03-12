stack = []
stick, res = 0, 0

for s in input():
    if len(stack) == 0 or stack[-1] == s:
        stick+=1
        stack.append(s)
        cut = True
    elif stack[-1] != s:
        stick-=1
        stack.pop()
        if cut:
            res+=stick
            cut = False
        else:
            res+=1

print(res)