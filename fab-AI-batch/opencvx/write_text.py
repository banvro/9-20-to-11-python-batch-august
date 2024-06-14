import numpy as np
import cv2 as cv

blank = np.zeros((500, 500, 3), dtype = 'uint8')

cv.putText(blank, "hellow world", (50, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness = 4)

cv.imshow("Blank Screen", blank)


cv.waitKey(0)