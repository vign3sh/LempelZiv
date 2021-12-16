import math

from PIL import Image
import numpy as np
from en import *


def encode():
    im = Image.open('spiral.jpg')
    im = im.convert('1')  # convert a gray scale
    print(im.mode)
    # px = im_file.getdata()
    # print(len(px))
    a = np.asarray(im)
    sh = np.shape(a)
    a.flatten()
    print(sh)
    s = []

    for i in range(sh[0]):
        for j in range(sh[1]):
            s.append(str(int(a[i][j])))

    # save(a, sh, s)
    enc_s = enc(s)
    m = 0
    for i in enc_s:
        if m<i:
            m=i

    print(len(s), len(enc_s), math.ceil(math.log(m, 2)))
    dec_s = dec(enc_s)
    #print(dec_s)
    #print(''.join(str(dec_s)))
    save(a, sh, ''.join(dec_s))


def save(a, sh, s):

    k = 0
    for i in range(sh[0]):
        for j in range(sh[1]):
            a[i][j] = int(s[k])
            k += 1

    i = Image.fromarray(a)
    i.mode = '1'
    i.show()
    i.save('bg1.png')


encode()