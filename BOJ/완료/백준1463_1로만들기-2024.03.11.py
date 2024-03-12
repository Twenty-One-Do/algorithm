n = int(input())

count = 0
min_cases = [0 for _ in range(n+1)]
if n<4:
    print(1 if n != 1 else 0)
else:
    min_cases[1] = 0
    min_cases[2] = 1
    min_cases[3] = 1

    for i in range(4,n+1):
        candidate = [min_cases[i-1]]
        if i%3 == 0:
            candidate.append(min_cases[i//3])
        if i%2 == 0:
            candidate.append(min_cases[i//2])
        min_cases[i] = min(candidate)+1

    print(min_cases[n])