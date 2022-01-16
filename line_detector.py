import cv2, time
import numpy as np

def detect_lines(img):

    imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.blur(imgGRAY,(4,4))
    canny = cv2.Canny(imgBlurred,180,250,apertureSize=3)

    Way_corners = np.array([[(80,390),(470,390),(400,190),(180,190)]],dtype=np.int32)
    mask = np.zeros_like(imgGRAY)
    cv2.fillPoly(mask,Way_corners,255)
    masked_way = cv2.bitwise_and(canny,mask)
    #cv2.imshow("masked",masked_way)

    lines = cv2.HoughLinesP(masked_way,2,np.pi/180,120,minLineLength=20,maxLineGap=50)
    return lines

def display_all_lines(img,lines):

    if lines is not None:
        for line in lines:  
            for x1,y1,x2,y2 in line:
                slope = (y2-y1)/(x2-x1)
                slope = float(slope) * 57.29   # to degree
                if slope > 0:
                    cv2.line(img,(x1,y1),(x2,y2),[0,127,255],3)
                else:
                    cv2.line(img,(x1,y1),(x2,y2),[0,127,255],3)


    

