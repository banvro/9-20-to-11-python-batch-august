import cv2 as cv
import numpy as np

# image = cv.imread("my_images/images.jpeg")
# cv.imshow("my image", image)

# blank = np.zeros((500, 500, 3), dtype = 'uint8')

# blank[200:300, 300:400] = 0,255,0
blank = np.zeros((500, 500, 3), dtype = 'uint8')

# cv.rectangle(blank, (0,0), (200,400), (0,255,0), thickness = 3)


# cv.rectangle(blank, (0,0), (200,400), (0,255,0), thickness = -1)

cv.rectangle(blank, (0,0), (200,400), (0,255,0), thickness = cv.FILLED)

# cv.circle(blank, (200, 400), 100, (247, 0, 79), thickness = 4)

cv.circle(blank, (200, 400), 100, (247, 0, 79), thickness = -1)

cv.line(blank, (200, 100), (400, 500), (0, 231, 247), thickness = 5)

cv.imshow("blank Scrren", blank)

cv.waitKey(0)