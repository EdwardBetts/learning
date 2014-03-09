import cv

location = "D:\\Dropbox\\vision\\soniaImages\\"
imgName = "a.png"

image = cv.LoadImage(location+imgName)
cv.NamedWindow("original",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("original",image)

image3 = cv.LoadImage(location+imgName,0)
cv.NamedWindow("gray",cv.CV_WINDOW_AUTOSIZE)
#cv.CvtColor(image,image3,cv.CV_BGR2GRAY)
cv.ShowImage("gray",image3)

image2 = cv.CreateImage(cv.GetSize(image),cv.IPL_DEPTH_8U,3)
cv.NamedWindow("smooth",cv.CV_WINDOW_AUTOSIZE)
cv.Smooth(image,image2,smoothtype=cv.CV_GAUSSIAN, param1=3, param2=3, param3=0, param4=0L)
cv.ShowImage("smooth",image2)

image4 = cv.CreateImage(cv.GetSize(image3),image3.depth, image3.nChannels)
cv.NamedWindow("canny",cv.CV_WINDOW_AUTOSIZE)
cv.Canny(image3,image4,10,470,3)
cv.ShowImage("canny",image4)

image5 = cv.CreateImage(cv.GetSize(image3),image3.depth, image3.nChannels)
cv.NamedWindow("sobel",cv.CV_WINDOW_AUTOSIZE)
cv.Sobel(image3,image5,1,2,3)
cv.ShowImage("sobel",image5)

'''
print cv.GetSize(image)
print image3.nChannels
print cv.GetSize(image4)

'''