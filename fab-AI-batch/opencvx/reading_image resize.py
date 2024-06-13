def frame_rescaling(frame, scale = 0.25):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    demmsions = (width, height)

    resized_frame = cv.resize(frame, demmsions, interpolation = cv.INTER_AREA)

    return resized_frame

import cv2 as cv

image = cv.imread("my_images/pexels-pixabay-45201.jpg")


xyz = frame_rescaling(image)

cv.imshow("My Cat Image", image)

cv.imshow("resiezed image", xyz)

cv.waitKey(0)