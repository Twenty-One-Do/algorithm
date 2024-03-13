'''
<예제>
4 2 10
7 4 5 6
<정답>
8
'''
from collections import deque

n, w, l = list(map(int,input().split()))
trucks = list(map(int,input().split()))[::-1]

bridge = deque([0 for _ in range(w)],maxlen=w)
count = 0
while trucks:
    count+=1
    if sum(bridge) - bridge[-1] + trucks[-1] <= l:
        bridge.pop()
        bridge.appendleft(trucks.pop())
    else:
        bridge.pop()
        bridge.appendleft(0)

print(count+w)
