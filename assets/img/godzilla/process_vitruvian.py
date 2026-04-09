import cv2 
import os 
p = './vitruvian.png'
img = cv2.imread(p)
#make right square black , like from r-thresh:r to 0, end col-thresh:c to 0 
r,c = img.shape[:2]
thresh = 200
# r_thres = int(r/2)
# c_thres = int(c/2)
# img[r_thres:r,c_thresh:c] = 0
img[r- thresh:r,c- thresh:c] = 0
cv2.imwrite('./vitruvian_cropped.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])