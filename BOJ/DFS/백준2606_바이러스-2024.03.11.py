def infect(com, infected):
    global internet, count
    for target in internet[com]:
        if target not in infected:
            count+=1
            infected.append(target)
            infect(target, infected)

count = 0
num_c = int(input())
internet = {i:[] for i in range(1,num_c+1)}
for _ in range(int(input())):
    com, target = list(map(int, input().split()))
    if target not in internet[com]:
        internet[com].append(target)
    if com not in internet[target]:
        internet[target].append(com)

infect(1, [1])
print(count)