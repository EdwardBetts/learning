import cv

location = "D:\\Dropbox\\vision\\soniaImages\\"
imgName = "a.png"

img = cv.LoadImage(location+imgName)
out = cv.CreateMemStorage()
haar = cv.LoadHaarClassifierCascade('haarcascade_frontalface_default.xml')
allFaces = cv.HaarDetectObjects(image, haar, out, 1.2, 2, cv. CV_HAAR_DO_CANNY_PRUNING,(100,100))
if allFaces:
	for face in allFaces:
		print face
