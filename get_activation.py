import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import get_color_ratio as gcr
# if __name__ == '__main__' :

pathname = '../Dogbone1 white balance 2'
full_activated = 'purpleUV.jpg'
activated_relaxed_filename = 'purple.jpg'
bleached_filename = 'reverted.jpg'

#ignore those files
ignore_files = [full_activated, activated_relaxed_filename, bleached_filename]

# create the list of files that should be only the testing set
file_list = [os.path.join(pathname,f) for f in os.listdir(pathname) if f.endswith('.jpg') and not f in ignore_files ]
file_list.sort()

last_filename = file_list[-1]
lastim = plt.imread(last_filename)
height, width = lastim.shape[:2]
width = int(width/100)
height = int(height/100)
print(height,width)
cv2.namedWindow("jpg", cv2.WINDOW_NORMAL)
cv2.resizeWindow("jpg", (height, width))
r = cv2.selectROI("jpg", lastim)#, fromCenter, showCrosshair)
cv2.waitKey(0)
# r,cimcrop = gcr.get_area(lastim)
print('done')
#
# for im_file in file_list:
#     img = plt.imread(im_file)
#     img = np.rot90(img)
#     plt.imshow(img)
#     plt.pause(0.001)
#
# plt.show()
