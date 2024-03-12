word_to_num = {'p':1,'q':-1,'b':2,'d':-2}
num_to_word = {1:'p',-1:'q',2:'b',-2:'d'}

T = int(input())

for test_case in range(1, T + 1):
    inp = input()
    mirror = ''.join([num_to_word[-1*word_to_num[k]] for k in inp[::-1]])
    print(f"#{test_case} {mirror}")