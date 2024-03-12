
def get_cases(i, fixed):
    global n, arr, count
    if i == n:
        count+=1
        return
    else:
        for j in range(i, n):
            is_right = True
            for f_idx, f in enumerate(fixed):
                if i-f_idx == abs(f-arr[j]):
                    is_right = False
                    break
            
            if is_right:
                arr[i], arr[j] = arr[j], arr[i]   
                fixed.append(arr[i])
                get_cases(i+1, fixed)
                fixed.pop()
                arr[i], arr[j] = arr[j], arr[i]   

n = int(input())
arr = list(range(1,n+1))
count = 0

get_cases(0, [])
print(count)