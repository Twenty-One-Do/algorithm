'''
A1 A2 5
B
L
LB
RB
LT

A1
A2
'''

k_pos, r_pos, n = input().split()

k_pos = [ord(k_pos[0]) - ord('A'), int(k_pos[1])-1]
r_pos = [ord(r_pos[0]) - ord('A'), int(r_pos[1])-1]

for _ in range(int(n)):
    order = input()
    move = [0,0]
    if 'L' in order: move[0] -= 1
    if 'R' in order: move[0] += 1
    if 'T' in order: move[1] += 1
    if 'B' in order: move[1] -= 1
    k_pos[0] += move[0]
    k_pos[1] += move[1]
    if not all(map(lambda x : 0<=x<=7, k_pos)):
        k_pos[0] -= move[0]
        k_pos[1] -= move[1]
        continue
    if r_pos == k_pos:
        r_pos[0] += move[0]
        r_pos[1] += move[1]
        if not all(map(lambda x : 0<=x<=7, r_pos)):
            k_pos[0] -= move[0]
            k_pos[1] -= move[1]
            r_pos[0] -= move[0]
            r_pos[1] -= move[1]
            continue

print(chr(k_pos[0]+ord('A')) + str(k_pos[1]+1))
print(chr(r_pos[0]+ord('A')) + str(r_pos[1]+1))

        
