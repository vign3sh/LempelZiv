from collections import defaultdict
import math


def decode(encoded_string):

    table = defaultdict(lambda: '$$$$$$')
    table[0] = '0'
    table[1] = '1'

    omega = encoded_string[0]
    i = 1
    output = [table[omega]]
    table_counter = 2
    current = table[omega]
    while i < len(encoded_string):
        n = encoded_string[i]
        if table[n] == '$$$$$$':
            s = table[omega]
            s += current

        else:
            s = table[n]
        output.append(s)
        current = s[0]
        table[table_counter] = table[omega] + current
        table_counter += 1
        omega = n
        i += 1

    # print(table)
    return output


def encode(string):
    # create dictionary with 0, 1 as inputs
    table = defaultdict(lambda: -1)
    table['0'] = 0
    table['1'] = 1

    omega = string[0]
    result = []
    table_counter = 2
    i = 1
    while i < len(string):
        current_char = string[i]

        if table[omega + current_char] != -1:
            if i == len(string) - 1:
                result.append(table[omega + current_char])
            omega = omega + current_char
        else:
            result.append(table[omega])
            if i == len(string) - 1:
                result.append(table[current_char])
                break
            table[omega + current_char] = table_counter
            table_counter += 1
            omega = current_char

        i += 1
    return result


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
