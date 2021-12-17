import base64
import math
from lzw import encode, decode


def main(input_file, output_file):

    with open(input_file, "rb") as image2string:
        # encoding
        image_string = base64.b64encode(image2string.read())
        # Removed 'b and ' form base64 encoding
        encoded_image = str(image_string)[2:-1]
        encoded_image = encode(encoded_image)

        # decoding
        decoded_image = decode(encoded_image)
        decoded_image = base64.b64decode(decoded_image)
        image_result = open(output_file, 'wb')
        image_result.write(decoded_image)

        encoded_bits = 0
        for i in encoded_image:
            if i > encoded_bits:
                encoded_bits = i

        encoded_bits = max(math.ceil(math.log(encoded_bits, 2)), 8)
        # Len of orignal text ,default size of each character(8 bits), len of encoded text, Size of each ch)
        input_size = len(image_string) * 8
        output_size = len(encoded_image) * encoded_bits
        print("Input Image size: ", input_size)
        print("Output Image size: ", output_size)
        print("Compression:", input_size / output_size)


main("pattern.jpg", "pattern_decoded.jpg")
main('sample.jpg', "sample_decoded.jpg")
