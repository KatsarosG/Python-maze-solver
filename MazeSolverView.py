import numpy as np
import cv2
import time

image = str(input("maze?(only PNG): " ))

startTime = time.time()

def Near(yx):
    near = []
    if yx != start and yx != finish:
        if img[yx[0]+1][yx[1]] == 1:
            near.append((yx[0]+1,yx[1]))
        if img[yx[0]-1][yx[1]] == 1:
            near.append((yx[0]-1,yx[1]))
        if img[yx[0]][yx[1]+1] == 1:
            near.append((yx[0],yx[1]+1))
        if img[yx[0]][yx[1]-1] == 1:
            near.append((yx[0],yx[1]-1))
    if yx == start:
        if img[yx[0]+1][yx[1]] == 1:
            near.append((yx[0]+1,yx[1]))
        if img[yx[0]][yx[1]+1] == 1:
            near.append((yx[0],yx[1]+1))
        if img[yx[0]][yx[1]-1] == 1:
            near.append((yx[0],yx[1]-1))
    if yx == finish:
        finished = True
    return(near)
print("Loading image...")
img = cv2.imread(str(image),0)
imgshow = cv2.imread(image)
showH, showW, channels = imgshow.shape

for row in range(len(img)):
    for pixel in range(len(img[row])):
        if img[row][pixel] < 100:
            img[row][pixel] = 0
        else:
            img[row][pixel] = 1
loadingTime = time.time() - startTime
print("Loading took: " + str(loadingTime))

print("Analizing...")
#start and finish
for i in range(len(img[0])):
    if img[0][i] == 1:
        start = (0,i)
for i in range(len(img[-1])):
    if img[-1][i] == 1:
        finish = (len(img)-1, i)

print("Solving...")
here = start
#print(Near(here))

switchSpot = []
realSteps = 0
steps = []

cv2.namedWindow('Show')
cv2.moveWindow('Show', 0,0)

finished = False
while finished == False:
    #print(realSteps)     
    imgshow[here] = [0, 0, 255]
    if showW < 800:
        imgshow = cv2.resize(imgshow, (800,800), interpolation = cv2.INTER_AREA)
    cv2.imshow('Show', imgshow)
    cv2.waitKey(1)
    imgshow = cv2.resize(imgshow, (showW,showH))
    imgshow[here] = [255, 200, 100]
    for i in steps:
        imgshow[i] = [0,0,255]
    
    #print(here)
    steps.append(here)
    img[here[0]][here[1]] = 2
    
    if len(Near(here)) == 1:
        here = Near(here)[0]
    elif len(Near(here)) > 1:
        switchSpot.append(here)
        here = Near(here)[0]
    elif len(Near(here)) == 0 and here != finish:
        here = switchSpot[-1]
        
        for i in steps:
            if steps.index(i) > steps.index(switchSpot[-1]):
                imgshow[i] = [255,200,100]
                steps[steps.index(i)] = 'delete'  
               
        while 'delete' in steps:
            steps.remove('delete')

            
                
        del switchSpot[-1]
        
    elif here == finish:
        finished = True
    realSteps += 1

solvingTime = (time.time() - startTime) - loadingTime

for s in steps:
    imgshow[s] = [0, 0, 255]
outputName = 'Solved' + '_' + image
print(outputName)
cv2.imwrite(outputName, imgshow)

print("Finished!")
print("Solving time: " + str(solvingTime))
print("Steps: " + str(realSteps))
print("Solution Steps: " + str(len(steps)))

while True:
    steps = []































