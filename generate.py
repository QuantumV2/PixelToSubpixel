import numpy as np
from PIL import Image
import math 
import argparse
parser = argparse.ArgumentParser(
                    prog='Pixel To Subpixel',
                    description='Converts 1 bit pixelart to images that look the same on LCD subpixels, can be seen in more detail with a digital camera\n...or squinting',)
parser.add_argument('filename')  
args = parser.parse_args()

def create_image(rgb_array, image_size):
    image = Image.new("RGB", image_size)
    
    pixels = image.load()
    
    for y in range(image_size[1]): 
        for x in range(image_size[0]): 
            position = y * image_size[0] + x
            if position < len(rgb_array):
                pixels[x, y] = tuple(rgb_array[position])
    
    return image
def convert_1bit_to_rgb_array(image_path):
    image = Image.open(image_path).convert('1')
    width, height = image.size
    pixel_values = list(image.getdata()) 

    rgb_array = []
    for y in range(height):
        for x in range(0, width, 3):
            rgb = []
            for offset in range(3):
                if x + offset < width:
                    value = pixel_values[y * width + x + offset]
                    rgb.append(value)
            while len(rgb) < 3:
                rgb.append(0)
            rgb_array.append(rgb)
    return rgb_array, math.ceil(width / 3), height

image_path = args.filename
rgb_array, width, height = convert_1bit_to_rgb_array(image_path)
img = create_image(rgb_array, (width, height))
img.save("generated.png")
img.show()