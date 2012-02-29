#! /usr/bin/env python
import cv
#capture = cv.CaptureFromCAM(0)
#print capture
#img = cv.QueryFrame(capture)
img = cv.LoadImage("Screenshot-1.png", cv.CV_LOAD_IMAGE_GRAYSCALE)
eig_image = cv.CreateMat(img.height, img.width, cv.CV_32FC1)
temp_image = cv.CreateMat(img.height, img.width, cv.CV_32FC1)
lx = 0
ly = 0
i = 1
totalx = 0
for (x,y) in cv.GoodFeaturesToTrack(img, eig_image, temp_image, 16, 0.04, 15.0, blockSize = 25 ,useHarris = True):
	#print "good feature at", x,y
	c = cv.Scalar(255)
	cv.Rectangle(img, (x-8, y-8), (x+8, y+8), c)
	#cv.Line(img, (lx,ly), (x,y),c)
	cv.PutText(img, str(i) , (x-8,y-8), cv.InitFont(0,0.75,0.75),c)
	lx = x
	ly = y
	i +=1
	totalx += x 
cv.Line(img, (img.width/2, 0),(img.width/2, img.height),c);
cv.Line(img, (0, img.height/2),(img.width,img.height/2),c);
#print img.width
#print img.width/2
print totalx/(i) - img.width/2
print "yeah"
cv.SaveImage("Screenshot-1ed.png", img)
cv.ShowImage("OOOOOOooooooooo......",img)
buttonID = cv.WaitKey(1000)
print "whoo"
