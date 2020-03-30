# import tkinter module 
from tkinter import *
import os
import sys

def pm():
    master.destroy()
    os.system('python ques.py')
def et():
    master.destroy()
    os.system('python example.py')
def st():
    master.destroy()
    os.system('python audio11.py')
def yp():
    master.destroy()
    os.system('python yourprogress.py')
def lo():
    master.destroy()
    os.system('python login.py')
def faq():
    master.destroy()
    os.system('python faq.py')
def au():
    master.destroy()
    os.system('python au.py')

# creating main tkinter window/toplevel 
master = Tk()
master.overrideredirect(True)
master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
master.focus_set()  # <-- move focus to this widget
master.bind("<Escape>", lambda e: e.widget.quit())

# this wil create a label widget
l1 = Label(master, text = "Autism Aid",font=('Times',80,'bold'), fg="blue") 

# grid method to arrange labels in respective 
# rows and columns as specified 
l1.grid(row = 0, column = 1,sticky = W, pady = 2,columnspan = 2) 
   
  

  

# adding image (remember image should be PNG and not JPG) 
img = PhotoImage(file = r"Autism.png") 
img1 = img.subsample(2, 2) 
  
# setting image with the help of label 
Label(master, image = img1).grid(row = 1, column = 1, columnspan = 4, rowspan = 3, padx = 5, pady = 5) 
  
# button widget 
b1 = Button(master, text = "Parents module", bg="yellow", fg="red", font=('Times', 30), command=pm) 
b2 = Button(master, text = "Eye test", bg="yellow", fg="red", font=('Times', 30), command=et) 
b3 = Button(master, text = "Speech test", bg="yellow", fg="red", font=('Times', 30), command=st) 
b4 = Button(master, text = "Your Progress", bg="yellow", fg="red", font=('Times', 30), command=yp) 
b5 = Button(master, text = "Logout", fg="red", font=('Times', 30), command=lo) 
b6 = Button(master, text = "FAQ", fg="red", font=('Times', 30), command=faq) 
b7 = Button(master, text = "About us", fg="red", font=('Times', 30), command=au) 
ls = Label(master, text="                                                                   ")
  
# arranging button widgets 
b1.grid(row = 1, column = 0, sticky = W,padx=20,pady=20) 
b2.grid(row = 2, column = 0, sticky = W,padx=20,pady=20)
b3.grid(row = 3, column = 0, sticky = W,padx=20,pady=20)
b4.grid(row = 4, column = 0, sticky = W,padx=20,pady=20)
b5.grid(row = 0, column = 4, sticky = E,padx=20,pady=20)
b6.grid(row = 4, column = 1,padx=20,pady=20)
ls.grid(row = 4, column = 2)
ls.grid(row = 4, column = 3)
b7.grid(row = 4, column = 4,padx=20,pady=20)

# infinite loop which can be terminated by keyboard 
# or mouse interrupt 
mainloop() 
    
