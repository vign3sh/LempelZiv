import math

from PIL import Image
import numpy as np
from en import *


def encode():
    im = Image.open('spiral.jpg')
    im = im.convert('1')  # convert a gray scale
    #print(im.mode)
    a = np.asarray(im)
    sh = np.shape(a)
    print(sh)
    s = []

    #flatten the 2d array to a list
    for i in range(sh[0]):
        for j in range(sh[1]):
            s.append(str(int(a[i][j])))

    enc_s = enc(s)
    # Find the size of maximum character
    m = 0
    for i in enc_s:
        if m<i:
            m=i

    # Len of orignal text ,default size of each character(1 bit), len of encoded text, Size of each ch)
    print(len(s), len(enc_s), math.ceil(math.log(m, 2)))
    dec_s = dec(enc_s)
    save(a, sh, ''.join(dec_s))


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


encode()