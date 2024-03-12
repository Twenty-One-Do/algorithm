# 재귀
def get_cases(n):
    global count
    if n == 0:
        count+=1
    elif n>0:
        for i in range(1,4):
            get_cases(n-i)

T = int(input())
counts = []
for _ in range(T):
    count = 0 
    n = int(input())
    get_cases(n)
    counts.append(count)

for c in counts:
    print(c)


# DP
T = int(input())

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    tmp = int(input())
    print(dp[tmp])