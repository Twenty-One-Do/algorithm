def fibo_dp(n):
    fibo = [1, 1]
    count_dp=0
    for i in range(2, n):
        count_dp+=1
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[-1]

n = int(input())
count_dp = fibo_dp(n)
print(count_dp)