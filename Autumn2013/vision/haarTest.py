import cv

location = "/home/bork/Data/learning/Autumn2013/vision/"
imgName = "people.jpg"

img = cv.LoadImage(location+imgName)
out = cv.CreateMemStorage()
haar = cv.Load('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml') #HaarClassifierCascade
allFaces = cv.HaarDetectObjects(img, haar, out, 1.2, 2, cv. CV_HAAR_DO_CANNY_PRUNING,(100,100))
if allFaces:
	for face in allFaces:
		print face
		print 'hello'
		cv.ShowImage(face)
cv.waitKey(0)
