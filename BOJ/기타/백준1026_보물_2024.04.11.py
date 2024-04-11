"""
5
1 1 1 6 0
2 7 8 3 1

18
"""

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort()
s = 0
for a_el, b_el in zip(a,b):
    s+=a_el*b_el
print(s)