l, c = list(map(int,input().split()))
binarys = []
for i in range(2**c):
    b = bin(i).split('b')[-1].zfill(c)
    if b.count('1') == l:
        binarys.append([int(b_) for b_ in b[::-1]])

words = sorted(input().split(), reverse = True)

for binary in binarys[::-1]:
    consonant, vowel = 0, 0
    _case = [w for b, w in zip(binary, words) if b][::-1]
    for c in _case:
        if c in 'aeiou':
            vowel+=1
        else:
            consonant+=1
    if vowel>=1 and consonant >=2:
        print(''.join(_case))
