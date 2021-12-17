import base64
import  math
from lempel_ziv import enc_lempel, dec_lempel
from PIL import Image

def encode_base(img):
    with open(img, "rb") as image2string:
        enc_text = base64.b64encode(image2string.read())
        # Removed 'b and ' form base64 encoding
        orignal_text = str(enc_text)[2:-1]
        enc_lemp = enc_lempel(orignal_text)
        # print(len(enc_text), len(enc_lemp))
        dec_lemp = dec_lempel(enc_lemp)
        dec_img = base64.b64decode(dec_lemp)
        image_result = open('decode.jpg', 'wb')
        image_result.write(dec_img)

        m = 0
        for i in enc_lemp:
            if i > m:
                m = i

        m = max(math.ceil(math.log(m, 2)), 8)
        # Len of orignal text ,default size of each character(8 bits), len of encoded text, Size of each ch)
        print(len(orignal_text), 8, len(enc_lemp), m)

encode_base("col_pattern.jpg")