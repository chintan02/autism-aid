from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyaudio
import time
import os
import matplotlib.pyplot as plt
import pyrebase
from datetime import datetime



from playsound import playsound

def back():
    window.destroy()
    os.system('python dashboard.py')

def test():
    i=0
    score= [0,0,0,0,0,0]
    response = [0,0,0,0,0,0]
    while(i<3):
        i=i+1
        playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\a.mp3')
     
    r=sr.Recognizer()
    flag = 0
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        #Label(window, text="A for apple ", font=("Arial Bold", 30)).pack()
        print("Say Something!")
        start_time = time.time()
        audio=r.listen(source)
        print("time over")
        end_time = time.time()
        print(end_time-start_time)
    try:
        a=r.recognize_google(audio)
        print(a)
        x="apple"
        y="a"
        z="A for apple"
        if z in a:
            flag=flag+3
        elif x in a:
            flag=flag+2
        elif y in a:
            flag=flag+1
        score[0]=flag
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
   
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    print(flag)

    i=0
    while(i<3):
        i=i+1
        playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\b.mp3')
     
    r=sr.Recognizer()
    flag=0
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        #Label(window, text="B for Ball ", font=("Arial Bold", 30)).pack()
        print("Say Something!")
        start_time = time.time()
        audio=r.listen(source)
        print("time over")
        end_time = time.time()
        print(end_time-start_time)
    try:
        a=r.recognize_google(audio)
        print(a)
        x="baseball"
        y="b"
        z="B for baseball"
        if z in a:
            flag=flag+3
        elif x in a:
            flag=flag+2
        elif y in a:
            flag=flag+1
        score[1]=flag
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
   
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    i=0
    while(i<3):
        i=i+1
        playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\c.mp3')
     
    r=sr.Recognizer()
    flag=0
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        #Label(window, text="B for Ball ", font=("Arial Bold", 30)).pack()
        print("Say Something!")
        start_time = time.time()
        audio=r.listen(source)
        print("time over")
        end_time = time.time()
        print(end_time-start_time)
    try:
        a=r.recognize_google(audio)
        print(a)
        x="clock"
        y="c"
        z="C for clock"
        if z in a:
            flag=flag+3
        elif x in a:
            flag=flag+2
        elif y in a:
            flag=flag+1
        score[2]=flag
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
   
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    i=0
    while(i<3):
        i=i+1
        playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\d.mp3')
     
    r=sr.Recognizer()
    flag=0
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        #Label(window, text="B for Ball ", font=("Arial Bold", 30)).pack()
        print("Say Something!")
        start_time = time.time()
        audio=r.listen(source)
        print("time over")
        end_time = time.time()
        print(end_time-start_time)
    try:
        a=r.recognize_google(audio)
        print(a)
        x="donkey"
        y="d"
        z="D for donkey"
        if z in a:
            flag=flag+3
        elif x in a:
            flag=flag+2
        elif y in a:
            flag=flag+1
        score[3]=flag
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
   
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    i=0
    while(i<3):
        i=i+1
        playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\e.mp3')
     
    r=sr.Recognizer()
    flag=0
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        #Label(window, text="B for Ball ", font=("Arial Bold", 30)).pack()
        print("Say Something!")
        start_time = time.time()
        audio=r.listen(source)
        print("time over")
        end_time = time.time()
        print(end_time-start_time)
    try:
        a=r.recognize_google(audio)
        print(a)
        x="elephant"
        y="e"
        z="E for elephant"
        if z in a:
            flag=flag+3
        elif x in a:
            flag=flag+2
        elif y in a:
            flag=flag+1
        score[4]=flag
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
   
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    i=0
    while(i<3):
        i=i+1
        playsound('C:\\Users\\Angad Gosain\\Desktop\\BE Project\\sounds\\f.mp3')
     
    r=sr.Recognizer()
    flag=0
    #Microphone(device_index=i, sample_rate=48000)
    with sr.Microphone( sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source)
        #Label(window, text="B for Ball ", font=("Arial Bold", 30)).pack()
        print("Say Something!")
        start_time = time.time()
        audio=r.listen(source)
        print("time over")
        end_time = time.time()
        print(end_time-start_time)
    try:
        a=r.recognize_google(audio)
        print(a)
        x="father"
        y="f"
        z="f for father"
        if z in a:
            flag=flag+3
        elif x in a:
            flag=flag+2
        elif y in a:
            flag=flag+1
        score[5]=flag
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
   
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # x axis values 
    x = ['A', 'B', 'C', 'D', 'E', 'F']   
    # corresponding y axis values
    y=[0,0,0,0,0,0]
    y[0]=score[0]
    avg=0
    for i in range(1,6):
        y[i]=score[i]
        avg = avg+y[i]


    avg = avg/6
    firebaseConfig ={
            "apiKey": "AIzaSyDbEslT3tpBwDTDQfP_8ZOMRBGObKEUjao",
            "authDomain": "autism-aid.firebaseapp.com",
            "databaseURL": "https://autism-aid.firebaseio.com",
            "projectId": "autism-aid",
            "storageBucket": "autism-aid.appspot.com",
            "messagingSenderId": "616345484183",
            "appId": "1:616345484183:web:406ce8cb76552cf5b9a2d2",
            "measurementId": "G-9HBX2L5ZWE"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    now = datetime.now()
    date1 = now.strftime("%d-%m-%y")
    str1=str(date1)
    str2=str(avg)
    db = firebase.database()
    data={str1:str2}

    file = open("C:\\Users\\Angad Gosain\\Desktop\\BE Project\\login.txt","r")
    line = file.readline()
    print(line)
    db.child("speech").child(str(line)).push(data)

    # plotting the points  
    plt.plot(x, y, linewidth = 3, marker='o', markerfacecolor='red', markersize=12) 
  
    # naming the x axis 
    plt.xlabel('test dates') 
    # naming the y axis 
    plt.ylabel('time in seconds') 
  
    # giving a title to my graph 
    plt.title('Eye gaze response time') 

    plt.savefig("test.png")
    storage = firebase.storage()
    st = "speech/"+line+"/"+date1+".png"
    storage.child(st).put("test.png")
    # function to show the plot 
    plt.show()
    

    
window = Tk()
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.focus_set()  # <-- move focus to this widget
window.bind("<Escape>", lambda e: e.widget.quit())

Label(window, text="Autism Aid ", font=("Arial Bold", 30)).pack()
Label(window, text="").pack()
button = Button(window, text="speech test", command=test,font=("Arial Bold", 10))
button.pack()
button = Button(window, text="back", command=back,font=("Arial Bold", 10))
button.pack()

Label(window, text="").pack()
window.mainloop()


   
