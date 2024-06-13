import cv2 as cv

# capture = cv.VideoCapture("my_videos/979689-hd_1920_1080_30fps.mp4")
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv.imshow("My Video", frame)

    if cv.waitKey(20) & 0xFF == ord("x"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)






# def car():
#     a = "hello"
#     b = 10000

#     return a, b

# xyz, abc = car()

# print(abc)