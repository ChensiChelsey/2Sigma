from PIL import Image, ImageDraw
import PIL.ImageOps
import numpy as np
import cv2
import scipy.misc
from scipy.misc import imsave

# clipt image into box using OpenCV
# i = Image.open("./test_T.png")
# i = PIL.ImageOps.invert(i)
# print type(i)

# image_file = Image.open("test_T.png") # open colour image
# # image_file= image_file.convert('L') # convert image to monochrome - this works
# image_file= image_file.convert('1') # convert image to black and white
# imsave('test_T_new.png', image_file)

im = cv2.imread("./test_T.png")
kernel = np.ones((5,5),np.uint8)
im = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
# im = cv2.bitwise_not(im_inv)
image = Image.fromarray(im)
image.save("temp.png")
imgrey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgrey, 127, 255, 0)
im2, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

num = 1
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    if x is 0: continue
    symbolImage = image.crop((x, y, x+w, y+h))
    symbolImage.save(str(num) + ".png")
    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x+w, y+h), fill = 'white')
    cv2.rectangle(im, (x,y), (x+w, y+h), (0,255,0), 2)
    num = num + 1
image = Image.fromarray(im)    
image.save("test.png")
