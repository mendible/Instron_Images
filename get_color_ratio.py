# this code gets the RGB values from a set of pixels in an image and determines the ratio of colors

#input = pixels, 'top_ratio', 'bottom_ratio'
# pixels should be a matrix of pixels with the first dimension being the pixel
# and the second dimension being the 3 columns of colors, red, then green, then blue
import numpy as np

def get_color_ratio(pixels, top_of_ratio, bottom_of_ratio):
    map = {'red': 0, 'green':1, 'blue':2}
    ratio = np.mean((pixels[:,map[top_of_ratio]] - pixels[:,map[bottom_of_ratio]])/pixels[:,map[bottom_of_ratio]])
    return ratio
