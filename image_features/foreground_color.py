import numpy as np
import cv2
from matplotlib import pyplot as plt

def compute_average_image_color(img1):
    width, height = img1.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img1.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)

img = cv2.imread('../img/test/example.png')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

# plt.imshow(img),plt.colorbar(),plt.show()

from PIL import Image



# img = Image.open('image.png')
#img = img.resize((50,50))  # Small optimization
average_color = compute_average_image_color(img)
print(average_color)
