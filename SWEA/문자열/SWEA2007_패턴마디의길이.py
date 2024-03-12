T = int(input())

for test_case in range(1, T + 1):
    string = input()
    len_str = len(string)
    for i in range(1, len(string)):
        is_p = True
        p = string[0:i]
        for j in range(i, len(string), i):
            compare = string[j:len_str] if j+i > len_str else string[j:j+i]
            if p[:len(compare)] != compare:
                is_p = False
                break
        if is_p:
            print(f"#{test_case} {i}")
            break

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    len_str = len(string)
    for i in range(1, len(string)):
        split_str = string.split(string[0:i])
        str_join = ''.join(split_str[:-1])
        if len(str_join) == 0:
            print(f'{test_case} {i}')
            break