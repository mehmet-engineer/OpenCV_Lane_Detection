import cv2, line_detector, line_controller

cam = cv2.VideoCapture("a.mp4")

while True:
    _,img = cam.read()
    img = cv2.resize(img,(720,400))
    lines = line_detector.detect_lines(img)
    main_left_line, main_right_line = line_controller.process(img,lines)
    
    #line_detector.display_all_lines(img,lines)
    
    cv2.imshow("detection",img)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()