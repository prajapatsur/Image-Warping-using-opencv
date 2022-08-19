import cv2
import numpy as np
img = cv2.imread('cards.webp')

width,height = 225,350
pts1 = np.float32([[580,247],[789,280],[542,548],[757,581]])        #we can find these all points by paints

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])      #these are the coordinates where we want our output

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('cards',img)
cv2.imshow('Output',imgOutput)

print(img.shape)
print(imgOutput.shape)
cv2.waitKey(0)