'''
<예제>
7
6
1 2
2 3
1 5
5 2
5 6
4 7
<정답>
4
'''
num_c = int(input())
internet = {i:[] for i in range(1,num_c+1)}
for _ in range(int(input())):
    com, target = list(map(int, input().split()))
    if target not in internet[com]:
        internet[com].append(target)
    if com not in internet[target]:
        internet[target].append(com)

is_visited, queue = [], []
target = 1
while True:
    if target not in is_visited:
        is_visited.append(target)
        queue=internet[target]+queue

    if not queue:
        break
    else:
        target = queue.pop()
    
print(len(is_visited)-1)