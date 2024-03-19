'''
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
'''
T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    numbers = input()
    possible = []
    num_len = n//4
    for _ in range(num_len):
        for i in range(0, len(numbers), num_len):
            possible.append(int('0x'+''.join(numbers[i:i+num_len]),16))
        numbers = numbers[-1]+numbers[:-1]
    possible = sorted(list(set(possible)), reverse=True)
    print(f'#{test_case} {possible[k-1]}')