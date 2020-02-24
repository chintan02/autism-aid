from tkinter import *
import os
import sys




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
    os.system('python example.py')


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Your Autism charecteristics is " + str(right) + " of " + str(number_of_questions)).pack()
        button = Button(window, text="Eye test", command=end ,font=("Arial Bold", 10)).pack()
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
Label(window, text="Autism Aid ", font=("Arial Bold", 30)).pack()
Label(window, text="").pack()
button = Button(window, text="Parents Module", command=askQuestion ,font=("Arial Bold", 10))
button.pack()
Label(window, text="").pack()
button1 = Button(window, text="Eye Test", command=end ,font=("Arial Bold", 10))
button1.pack()
Label(window, text="").pack()
window.mainloop()
