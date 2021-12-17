from collections import defaultdict


def dec_lempel(str):
    s_dict = defaultdict(lambda: '$$$$$$')
    for i in range(0, 256):
        s_dict[i] = chr(i)

    old = str[0]
    i = 1
    output = s_dict[old]
    c=output[0]
    li = 256
    while i < len(str):
        n = str[i]

        if s_dict[n] == '$$$$$$':
            s = s_dict[old]
            s += c

        else:
            s = s_dict[n]
        output += s
        c = s[0]
        s_dict[li] = s_dict[old] + c
        li += 1
        old = n
        i += 1

    #print(s_dict)
    return output


def enc_lempel(s):
    s_dict = defaultdict(lambda: 0)
    a = s[0]
    output = []
    m = 256
    for i in range(0, 256):
        s_dict[chr(i)] = i
    # print(s_dict)
    i = 1
    while i < len(s):
        b = s[i]
        if s_dict[a + b] != 0:
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
inp = 'BABAABAAC'
encoded_text = enc_lempel(inp)
print(encoded_text)
decoded_text = dec_lempel(encoded_text)
print(decoded_text)
'''