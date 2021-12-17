from collections import defaultdict


def decode(encoded_string):
    table = defaultdict(lambda: '$$$$$$')
    for i in range(0, 256):
        table[i] = chr(i)

    omega = encoded_string[0]
    i = 1
    output = table[omega]
    current = output[0]
    table_counter = 256
    while i < len(encoded_string):
        n = encoded_string[i]

        if table[n] == '$$$$$$':
            s = table[omega]
            s += current

        else:
            s = table[n]
        output += s
        current = s[0]
        table[table_counter] = table[omega] + current
        table_counter += 1
        omega = n
        i += 1

    #print(table)
    return output


def encode(string):
    # initialize table
    table = defaultdict(lambda: 0)
    table_counter = 256
    for i in range(0, 256):
        table[chr(i)] = i
    # print(table)

    omega = string[0]
    output = []
    i = 1
    while i < len(string):
        current_character = string[i]
        if table[omega + current_character] != 0:
            if i == len(string) - 1:
                output.append(table[omega + current_character])
            omega = omega + current_character
        else:
            output.append(table[omega])
            if i == len(string) - 1:
                output.append(table[current_character])
                break
            table[omega + current_character] = table_counter
            table_counter += 1
            omega = current_character
        i += 1
    return output



'''
inp = 'BABAABAAC'
encoded_text = enc_lempel(inp)
print(encoded_text)
decoded_text = dec_lempel(encoded_text)
print(decoded_text)
'''