# this code gets the RGB values from a set of pixels in an image and determines the ratio of colors

#input = pixels, 'top_ratio', 'bottom_ratio'
# pixels should be a matrix of pixels with the first dimension being the pixel
# and the second dimension being the 3 columns of colors, red, then green, then blue
import numpy as np
import cv2

def get_color_ratio(pixels, top_of_ratio, bottom_of_ratio):
    map = {'red': 0, 'green':1, 'blue':2}
    ratio = np.mean((pixels[:,map[top_of_ratio]] - pixels[:,map[bottom_of_ratio]])/pixels[:,map[bottom_of_ratio]])
    return ratio

def get_area(img):
    # Select ROI
    showCrosshair = False
    fromCenter = False
    cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
    # r = cv2.selectROI('Image', img, fromCenter, showCrosshair)
    cv2.imshow('Image', img)
    # Crop image
    imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    # # Display cropped image
    # cv2.imshow("Image", imCrop)
    # cv2.waitKey(0)
    return r, imCrop
