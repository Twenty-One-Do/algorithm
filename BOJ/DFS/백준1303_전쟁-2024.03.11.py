n, m = list(map(int,input().split()))
bf = [['X' for _ in range(n+2)] for _ in range(m+2)]


for i in range(m):
    for s_i, s in enumerate(input()):
        bf[i+1][s_i+1] = s

def get_power(y, x, c):
    if bf[y][x] == c:
        bf[y][x] = 'X'
        return 1+get_power(y-1, x, c)+get_power(y+1, x, c)+get_power(y, x-1, c)+get_power(y, x+1, c)
    else:
        return 0

w_power, b_power = 0, 0

for x in range(1,n+1):
    for y in range(1,m+1):
        w_power += (get_power(y,x,'W'))**2
        b_power += (get_power(y,x,'B'))**2

print(f'{w_power} {b_power}')