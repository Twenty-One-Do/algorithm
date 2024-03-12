def get_n(arr, i, s):
    global count, k

    if s == k:
        count+=1
    elif i <len(arr) and s<k:
        get_n(arr, i+1, s+arr[i])
        get_n(arr, i+1, s)
T = int(input())

for test_case in range(1, T + 1):
    count = 0
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    get_n(arr, 0, 0)

    print(f'#{test_case} {count}')

