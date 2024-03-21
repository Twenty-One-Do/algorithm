'''
010079010+010079=
106010+010=
BYE

010079010+010079=010106106
106010+010=106093
'''
codes = ['0111111', '0001010', '1011101', '1001111', '1101010', '1100111', '1110111', '0001011', '1111111', '1101011']
code_to_num = {int(code,2):idx for idx, code in enumerate(codes)}
num_to_code = {idx:int(code,2) for idx, code in enumerate(codes)}

def decode(value):
    len_num = len(value)//3
    res = 0
    for i in range(0,len(value),3):
        res+=code_to_num[int(value[i:i+3])]*(10**(len_num-i//3-1))
    
    return res

def encode(value):
    res = []
    while value != 0:
        res.append(str(num_to_code[value%10]).zfill(3))
        value = value//10
    res.reverse()
    return ''.join(res)

while True:
    inp = input()
    if inp == 'BYE':
        break
    else:
        value_1, value_2 = inp[:-1].split('+')
        value_1, value_2 = decode(value_1), decode(value_2)
        value = encode(value_1+value_2)
        print(inp+value)
