def get_cases(i):
    global n, arr, count
    if i == n:
        count+=1
        return
    else:
        ban = []
        for f_idx, f in enumerate(arr[:i]):
            ban+=[f-(i-f_idx), f+(i-f_idx)]
        ban = set([b for b in ban if n>=b>=0])
        for j in range(i,n):
            if arr[j] not in ban:
                arr[i], arr[j] = arr[j], arr[i]   
                get_cases(i+1)
                arr[i], arr[j] = arr[j], arr[i]   

n = int(input())
arr = list(range(n))
count = 0

get_cases(0)
print(count)