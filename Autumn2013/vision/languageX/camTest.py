import cv

cv.NamedWindow("hello_world",cv.CV_WINDOW_AUTOSIZE)
camera = cv.CaptureFromCAM(-1)

while True:
    image = cv.QueryFrame(camera)
    key = cv.WaitKey(50)
    
    if (key == 'q') :
        break
    elif (key != -1) :
        cv.ShowImage("hello_world",image)

cv.DestroyWindow("hello_world")               