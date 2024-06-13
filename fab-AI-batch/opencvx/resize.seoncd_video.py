import cv2 as cv


def frame_rescaling(frame, scale = 0.25):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    demmsions = (width, height)

    resized_frame = cv.resize(frame, demmsions, interpolation = cv.INTER_AREA)

    return resized_frame








capture = cv.VideoCapture("my_videos/4828605-uhd_4096_2160_25fps.mp4")
# capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    resized_video = frame_rescaling(frame, scale = 0.5)

    cv.imshow("My Video", frame)

    cv.imshow("resized video", resized_video)

    if cv.waitKey(20) & 0xFF == ord("x"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
