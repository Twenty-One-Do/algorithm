# 정석
n = int(input())
res = []
for _ in range(n):
    stack = []
    for s in input():
        if len(stack) == 0 or stack[-1] == s:
            stack.append(s)
        elif stack[-1] == '(':
            stack.pop()
    res.append(('YES' if len(stack) == 0 else 'NO'))

for r in res:
    print(r)

# 편법
n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

for s in strings:
    while True:
        new_s = s.replace('()','')
        if s == new_s:
            break
        s = new_s
    print('YES' if len(s) == 0 else 'NO')
        
            