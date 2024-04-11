"""
15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5

7
"""

n = int(input())
arr = list(map(int,input().split()))
cnt_max = 0
for i in range(n):
    now_height = arr[i]
    cnt = 0
    l_grad, r_grad = float('inf'), -float('inf')
    for j in range(1, n):
        left, right = i-j, i+j
        if left>=0:
            new_grad = (now_height-arr[left])/j
            if new_grad<l_grad:
                cnt+=1
                l_grad = new_grad
        if right<n:
            new_grad = (arr[right]-now_height)/j
            if new_grad>r_grad:
                cnt+=1
                r_grad = new_grad
    if cnt_max<cnt:
        cnt_max = cnt

print(cnt_max)
