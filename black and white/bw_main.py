import math
from PIL import Image
import numpy as np
from lzw import *


def main():
    image = Image.open('spiral.jpg')
    image = image.convert('1')  # convert arr black and white

    # convert image to numpy array
    arr = np.asarray(image)
    sh = arr.shape

    processed_input = []

    # flatten the 2d array to arr list
    for i in range(sh[0]):
        for j in range(sh[1]):
            processed_input.append(str(int(arr[i][j])))

    encoded_string = encode(processed_input)

    # Find the size of maximum character
    encoded_size = 0
    for i in encoded_string:
        if encoded_size < i:
            encoded_size = i

    # Len of orignal text ,default size of each character(8 bits), len of encoded text, Size of each ch)
    input_size = len(processed_input)
    output_size = len(encoded_string) * math.ceil(math.log(encoded_size, 2))
    print("Input Image size: ", input_size)
    print("Output Image size: ", output_size)
    print("Compression:", input_size / output_size)

    # decoding
    dec_string = decode(encoded_string)
    save(arr, sh, ''.join(dec_string))


def save(a, sh, s):
    k = 0
    #Convert String back to 2-D array
    for i in range(sh[0]):
        for j in range(sh[1]):
            a[i][j] = int(s[k])
            k += 1

    i = Image.fromarray(a)
    i.mode = '1'
    i.show()
    i.save('output.jpg')


main()
