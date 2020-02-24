
import cv2
import numpy as np
import time
import wave
import sys

from playsound import playsound
from gaze_tracking import GazeTracking

response = [0,0,0,0,0,0]
response1 = [0,0,0,0,0,0]

k=0;   

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
counter1 =0
counter2 =0
counter3 =0
counter4 =0
counter5 =0
counter6 =0
countersc =0
flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
import threading 





while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    new_frame = np.zeros((720, 1450, 3), np.uint8)
    tic = time.perf_counter()        

    if (tic>15 and counter1==0 and flag1==0):
        counter1=+1    
    elif (tic-response1[0]>15 and counter1!=0 and counter2==0 and counter3==0 and counter4==0 and counter5==0 and counter6==0 and flag1!=0 and flag2==0):
        counter2=+1
    elif (tic-response1[1]>15 and counter1!=0 and counter2!=0 and counter3==0 and counter4==0 and counter5==0 and counter6==0 and flag2!=0 and flag3==0):
        counter3=+1
    elif (tic-response1[2]>15 and counter1!=0 and counter2!=0 and counter3!=0 and counter4==0 and counter5==0 and counter6==0 and flag3!=0 and flag4==0):
        counter4=+1
    elif (tic-response1[3]>15 and counter1!=0 and counter2!=0 and counter3!=0 and counter4!=0 and counter5==0 and counter6==0 and flag4!=0 and flag5==0):
        counter5=+1
    elif (tic-response1[4]>15 and counter1!=0 and counter2!=0 and counter3!=0 and counter4!=0 and counter5!=0 and counter6==0 and flag5!=0):
        counter6=+1
    

    def letter(x, y, text1,B, G, R):
        font_letter = cv2.FONT_HERSHEY_PLAIN
        font_scale = 15
        font_th = 8
        cv2.putText(new_frame, text1, (x, y), font_letter, font_scale, (B, G, R), font_th)
    if(counter1==0 and counter2==0):
        letter(50,200, "A", 57, 255, 20)
    elif(counter1!=0 and counter2==0):
        letter(1000,200, "B", 0, 255, 255)
        if(flag1==0):
            response1[0]=tic
            flag1=+1
    elif(counter2!=0 and counter3==0):
        letter(650,500, "C", 255, 0, 255)
        if(flag2==0):
            response1[1]=tic
            flag2=+1
    elif(counter3!=0 and counter4==0):
        letter(50,500, "D", 255, 255, 0)
        if(flag3==0):
            response1[2]=tic
            flag3=+1
    elif(counter4!=0 and counter5==0):
        letter(1000,500, "E", 0, 0, 255)
        if(flag4==0):
            response1[3]=tic
            flag4=+1
    else:
        letter(650,200, "F", 255, 0, 0)
        if(flag5==0):
            response1[4]=tic
            flag5=+1
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
        
        if(counter1!=0 and counter2==0):
            response[1]=tic
            playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\b.mp3')
            time.sleep(2)
            
            countersc=+1
            counter2=+1
            
        elif(counter4!=0 and counter5==0):
            response[4]=tic
            playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\e.mp3')
            time.sleep(2)
            
            countersc=+1
            counter5=+1
            
        #new_frame[:] = (0,0,255)
    elif gaze.is_left():
        text = "Looking left"
        
        if(counter1==0 and counter2==0):
            response[0]=tic
            playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\a.mp3')
            time.sleep(2)

            countersc=+1
            counter1=+1
        elif(counter3!=0 and counter4==0):
            response[3]=tic
            playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\d.mp3')
            time.sleep(2)
            
            countersc=+1
            counter4=+1
        #new_frame[:] = (255,0,0)
        
    elif gaze.is_center():
        text = "Looking center"
        
        if(counter2!=0 and counter3==0):
            response[2]=tic
            playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\c.mp3')
            time.sleep(2)
            
            countersc=+1
            counter3=+1

        elif(counter5!=0 and counter6==0):
            response[5]=tic
            playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\f.mp3')
            time.sleep(2)
            
            countersc=+1
            counter6=+1
            #letter(725,500,str(counter4))
            

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    cv2.imshow("New frame", new_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()

print(response)
print(response1)


# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
x = ['A', 'B', 'C', 'D', 'E', 'F']   
# corresponding y axis values
y=[0,0,0,0,0,0]
y[0]=response[0]
for i in range(1,6):
    if(response[i]!=0):
        y[i]=response[i]-response1[i-1]
# plotting the points  
plt.plot(x, y, linewidth = 3, marker='o', markerfacecolor='red', markersize=12) 
  
# naming the x axis 
plt.xlabel('objects') 
# naming the y axis 
plt.ylabel('time in seconds') 
  
# giving a title to my graph 
plt.title('Eye gaze response time') 
  
# function to show the plot 
plt.show() 
