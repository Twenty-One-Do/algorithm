n, k = map(int,input().split())
rows = []
cols = ['' for _ in range(n)]
for i in range(n):
    line = input().split()
    rows.append(''.join(line))
    for idx, l in enumerate(line):
        cols[idx] += l

string = ''
for r, c in zip(rows, cols):
    string+='0'+r+'0'+c+'0'

search = '0'+'1'*k+'0'
res = 0

for i in range(len(string)-len(search)+1):
    string.count(search)
    if string[i:i+len(search)] == search:
        res += 1

print(f'#{1} {res}')

