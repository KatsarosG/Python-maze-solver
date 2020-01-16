import numpy as np
import cv2
import time
import threading

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
    elif yx == start:
        if img[yx[0]+1][yx[1]] == 1:
            near.append((yx[0]+1,yx[1]))
        if img[yx[0]][yx[1]+1] == 1:
            near.append((yx[0],yx[1]+1))
        if img[yx[0]][yx[1]-1] == 1:
            near.append((yx[0],yx[1]-1))
    elif yx == finish:
        finished = True
    return(near)

print("Loading image...")
img = cv2.imread(str(image),0)
imgshow = cv2.imread(image)

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

finished = False
while finished == False:
    if realSteps%1000 == 0:
        print('Steps so far: ' + str(realSteps), end='\r')

    #print(realSteps)
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
        
        #for i in steps:
            #if steps.index(i) > steps.index(switchSpot[-1]):
                #steps[steps.index(i)] = 'delete'     
        #while 'delete' in steps:
            #steps.remove('delete')
        
        ##print(steps)
        ##print('hehe')

        for i in range(steps.index(switchSpot[-1])+1, len(steps)):
            steps[i] = 'delete'
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

#file = open('hehe.txt', 'r')
#writen = file.read()
#file.close()

#file = open('hehe.txt', 'w')
#file.write(writen)
#file.write(str(solvingTime) + '    /   ')
#file.close()

print("Finished!")
print("Solving time: " + str(solvingTime))
print("Steps: " + str(realSteps))
print("Solution Steps: " + str(len(steps)))
#print(steps)

while True:
    steps = []































