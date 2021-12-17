from collections import defaultdict
import math


def dec(encoded_string):
    table = defaultdict(lambda: '$$$$$$')
    for i in range(0, 256):
        table[i] = chr(i)

    omega = encoded_string[0]
    i = 1
    output = [table[omega]]
    current = output[0]
    table_counter = 256
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

    return output


def encode(input_string):
    # Initialize dictionary
    table = defaultdict(lambda: -1)
    table_counter = 256
    for i in range(0, 256):
        table[chr(i)] = i

    omega = input_string[0]
    output = []
    i = 1
    while i < len(input_string):
        current_char = input_string[i]

        if table[omega + current_char] != -1:
            if i == len(input_string) - 1:
                output.append(table[omega + current_char])
            omega = omega + current_char
        else:
            output.append(table[omega])
            if i == len(input_string) - 1:
                output.append(table[current_char])
                break
            table[omega + current_char] = table_counter
            table_counter += 1
            omega = current_char
        i += 1
    return output


def main():
    input_string = list(input("Please enter a String"))

    encoded_text = encode(input_string)

    # calculate compression
    output_bits = 0
    for i in encoded_text:
        if output_bits < i:
            output_bits = i
    output_bits = max(math.ceil(math.log(output_bits, 2)), 8)

    # Len of orignal text ,default size of each character(8 bits), len of encoded text, Size of each ch)
    print(len(input_string), 8, len(encoded_text), output_bits)
    print(encoded_text)

    # decoding
    decoded_text = dec(encoded_text)
    print(decoded_text)


main()
