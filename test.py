from PIL import Image
import numpy as np
import cv2
import scipy.misc

# clipt image into box using OpenCV
im = cv2.imread("./test_1.png")
imgrey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Threshold the image
ret, im_th = cv2.threshold(imgrey, 127, 255, 0)
thresh = im_th
# Find contours in the image
contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Get rectangles contains each contour
rects =[]
for contour in contours:
    rect = cv2.boundingRect(contour)
    print rect
    print type(rect)
    rects.append(rect)
# rects = [cv2.boundingRect(contour) for contour in contours]

for rect in rects:
    # Draw the rectangles
    cv2.rectangle(im, (rect[0],rect[1]), (rect[0]+rect[2], rect[0]+rect[3]), (0,255,0), 3)
    # Make the rectangular region around the digit
    leng = int(rect[3] * 1.6)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
    # Resize the image
    roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
    roi = cv2.dilate(roi, (3, 3))
    # Calculate the HOG features
    roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
    cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

cv2.imshow(im)
# result = Image.fromarray(im)
# result.save("test.png")
