import pyrebase
from datetime import datetime
import matplotlib.pyplot as plt
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
db = firebase.database()

file = open("login.txt","r")
line = file.readline()

d = db.child("eye").child(str(line)).get()
l=[]
l = d.val()

x = list(l)
y=[]
z1=[]
z2=[]
k=0
for i in x:
    y.append(l[str(i)])
    items = y[k].items()
    for item in items:
        z1.append(item[0])
        z2.append(float(item[1]))
    k=k+1

    
print(l)
print(x[0])
print(y)
print(z1)
print(z2)

# plotting the points  
plt.plot(z1, z2, linewidth = 3, marker='o', markerfacecolor='red', markersize=12) 
  
# naming the x axis 
plt.xlabel('test dates') 
# naming the y axis 
plt.ylabel('time in seconds') 
  
# giving a title to my graph 
plt.title('Eye gaze response time') 
  
# function to show the plot 
plt.show()

