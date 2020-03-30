from tkinter import *
import os
import sys
import pyrebase
import firebase

def end1():
        window.destroy()
        os.system('python dashboard.py')
        
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="")
            right += 1
        else:
            label = Label(view, text="")
        label.pack()
        view.after(100, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question, font=("Arial Bold", 12), padx="10" , pady="10").pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view), bg="yellow", fg="red", font=("Arial Bold", 10), padx="10" , pady="3" ).pack()
        Label(view, text="").pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view), bg="yellow", fg="red", font=("Arial Bold", 10), padx="10" , pady="3").pack()
        Label(view, text="").pack()
        #Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        #Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

    def end():
        window.destroy()
        os.system('python dashboard.py')


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Your Autism charecteristics is " + str(right) + " of " + str(number_of_questions)).pack()
        button = Button(window, text="Back", command=end ,font=("Arial Bold", 10)).pack()
        
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
        str1='ques'
        str2=str(right)
        data={str1:str2}
        
        file1 = open("C:\\Users\\Angad Gosain\\Desktop\\BE Project\\login.txt","r")
        line1 = file1.readline()
        print(line)
        db.child("users").child(str(line1)).set(data)
        return

    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range(2):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.focus_set()  # <-- move focus to this widget
window.bind("<Escape>", lambda e: e.widget.quit())

Label(window, text="Autism Aid ", font=("Arial Bold", 30)).pack()
Label(window, text="").pack()
button = Button(window, text="Parents Module", command=askQuestion ,font=("Arial Bold", 10))
button.pack()
button1 = Button(window, text="Back", command=end1 ,font=("Arial Bold", 10))
button1.pack()
Label(window, text="").pack()
Label(window, text="").pack()
window.mainloop()
