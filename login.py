import pyrebase
import os
import sys

from tkinter import *
class MyEntry:
    def __init__(self, root):
        self.f = Frame(root,height=400, width=500)
        self.f.propagate(0)
        self.f.pack()
        #labels
        self.l1=Label(text='Enter User name: ')
        self.l2=Label(text='Enter Password: ')
        self.button = Button(text="Login",font=("Arial Bold", 10),command= lambda:self.dbentry())
        #Create entry widget for user name
        self.e1=Entry(self.f, width=25, bg='yellow', fg='blue', font=('Arial', 14))
        #Create entry widget for Password. The text in the widget is replaced by *
        self.e2=Entry(self.f, width=25, bg='yellow', fg='blue', show='*')
        
        #Place labels and entry widgets in the frame
        self.l1.place(x=50, y=100)
        self.e1.place(x=200, y=100)
        self.l2.place(x=50, y=150)
        self.e2.place(x=200, y=150)
        self.button.place(x=200, y=300)
    def dbentry(self):
        # retrieve the values from the entry widget
        str1 = self.e1.get()
        str2 = self.e2.get()
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
        auth = firebase.auth()
        try:
           login = auth.sign_in_with_email_and_password(str1, str2) 
        except Exception as e:
            lb1=Label(text='Incorrect password').place(x=50, y=250)

        else:
            lb1=Label(text='Successul login....').place(x=50, y=250)
            root.destroy()
            os.system('python ques.py')

#Create root window
root = Tk()
#Create an object to MyButton class
mb=MyEntry(root)
#The root window handles the mouse click event
root.mainloop()
