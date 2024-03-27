'''
9

55
'''
n = int(input())
p = [1, 2]
if n <=2:
    print(p[n-1])
else:
    for i in range(2,n):
        p_n = p[i-1]+p[i-2]
        p.append(p_n)
    
    print(p[-1]%10007)
