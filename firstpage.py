from tkinter import *
import os
import sys

def register():
    window.destroy()
    os.system('python register.py')
def login():
    window.destroy()
    os.system('python login.py')

window = Tk()
Label(window, text="Autism Aid ", font=("Arial Bold", 30)).pack()
Label(window, text="").pack()
button = Button(window, text="Register", command=register ,font=("Arial Bold", 10))
button.pack()
Label(window, text="").pack()
button1 = Button(window, text="Login", command=login ,font=("Arial Bold", 10))
button1.pack()

Label(window, text="").pack()
window.mainloop()
