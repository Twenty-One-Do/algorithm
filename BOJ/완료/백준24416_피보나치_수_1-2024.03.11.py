def fibo_re(n):
    global count_re

    if n == 1 or n == 2:
        count_re += 1
        return 1
    else:
        return fibo_re(n-1) + fibo_re(n-2)

def fibo_dp(n):
    fibo = [1, 1]
    count_dp=0
    for i in range(2, n):
        count_dp+=1
        fibo.append(fibo[i-1]+fibo[i-2])
    return count_dp

n = int(input())
count_re = 0
fibo_re(n)
count_dp = fibo_dp(n)
print(count_re)
print(count_dp)