# OpenCV Lane Detection

Lane detection software is part of my custom software package that I use in the Traffic Coordinator system designed for specific tasks. The software I developed using Python OpenCV tools and HoughLine theory can detect the lanes on the road and the position of the lanes relative to the vehicles. Thus, it is checked whether the vehicles are in the lane or not.

Video -> https://drive.google.com/drive/u/0/folders/1t4Nr6niWguqxeanHeiZitAINIwjlwLyS

![resim](https://github.com/mehmet-engineer/OpenCV_Serit_Tespit_Yazilimi/blob/main/resim2.png)

In order to detect the safety strip, the data taken from the camera is first processed through morphological processes such as blurring and masking. Then, the edge detection algorithm is run depending on the horizontal and vertical differentiation level of the pixels. Whether the detected edges are safety strips or not is determined by the Hough Line function. Hough Line theory is a customized line detection method based on geometry. Considering that the images are a 2-dimensional matrix, the distance (ρ) of the perceived edge points to the origin (0,0) is the first parameter, while the angle (θ) on the horizontal axis constitutes the second parameter. The geometric relationship between the parameters is shown in the formula below;

ρ = xcosθ + ysinθ


The data received for each point is transferred to the coordinate system called the Hough Transform plane. The distance-angle values in this plane are recorded for all points and the coordinates of the values are determined as dense regions with the help of an accumulator. The distance angle values of the intense points above a certain threshold value of the counter show the possibility that there may be a line on the image in these parameters.

![resim](https://github.com/mehmet-engineer/OpenCV_Serit_Tespit_Yazilimi/blob/main/hough_line.jpg)

The representative distance-angle plot of the points and the Hough Line transform plane are given above. The detected lines are defined by subtracting the linear function f(x)=ax+b. All (x, y) coordinates of the pixels on the function are enclosed in a loop and marked with a color change one by one. Thus, the detection of colored lines consisting of dots on the image is carried out. Finally, efficiency and sensitivity have been increased by performing optimization studies such as selecting appropriate threshold values on the algorithm. The strip detection algorithm prepared works at 30-60 FPS speeds and stands out in terms of efficiency as it does not require a heavy processing load.
