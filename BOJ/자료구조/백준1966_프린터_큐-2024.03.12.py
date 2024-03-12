T = int(input())

counts = []
for _ in range(T):
    n, target = list(map(int, input().split()))
    queue, count = [], 0
    for idx, p in enumerate(list(map(int, input().split()))):
        queue.append([idx, p])
    
    while True:
        now_print = queue.pop(0)
        _print = True
        for q in queue:
            if now_print[-1] < q[-1]:
                queue.append(now_print)
                _print = False
                break
        if _print:
            count +=1
            if now_print[0] == target:
                print(count)
                break

for c in counts:
    print(c)