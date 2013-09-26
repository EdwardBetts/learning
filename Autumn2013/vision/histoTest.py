import cv
import numpy as np

location = "D:\\Dropbox\\vision\\soniaImages\\"
imgName = "a.png"

image = cv.LoadImage(location+imgName)
cv.NamedWindow("original",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("original",image)

histo = np.zeros(cv.GetSize(image))

bins = np.arange(256).reshape(256,1)
color = [(255,0,0),(0,255,0),(0,0,255)]
for ch,color in enumerate(color):
    hist_item = 