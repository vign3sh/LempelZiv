from collections import defaultdict
import math

def dec(str):
    s_dict = defaultdict(lambda: '$$$$$$')
    s_dict[0] = '0'
    s_dict[1] = '1'
    old = str[0]
    i = 1
    output = [s_dict[old]]
    li = 2
    c = s_dict[old]
    while i < len(str):
        n = str[i]
        if s_dict[n] == '$$$$$$':
            s = s_dict[old]
            s += c

        else:
            s = s_dict[n]
        output.append(s)
        c = s[0]
        s_dict[li] = s_dict[old] + c
        li += 1
        old = n
        i += 1

    # print(s_dict)
    return output


def enc(s):
    s_dict = defaultdict(lambda: -1)
    a = s[0]
    s_dict['0'] = 0
    s_dict['1'] = 1
    output = []
    m = 2
    # print(s_dict)
    i = 1
    while i < len(s):
        b = s[i]
        if s_dict[a + b] != -1:
            if i == len(s) - 1:
                output.append(s_dict[a + b])
            a = a + b
        else:
            output.append(s_dict[a])
            if i == len(s) - 1:
                output.append(s_dict[b])
                break
            s_dict[a + b] = m
            m += 1
            a = b
        i += 1
    return output


'''
inp = ['B', 'A', 'B', 'A', 'A', 'B', 'A', 'A','A']
encoded_text = enc(inp)
m=0
for i in encoded_text:
    if m<i:
        m=i
print(len(inp), len(encoded_text), math.ceil(math.log(m, 2)))
'''
# print(encoded_text)
# decoded_text = dec(encoded_text)
# print(decoded_text)
