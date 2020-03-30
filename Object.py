from tkinter import*
from random import*
####Set veriables
colors=["mintcream","orangered","gold","coral","red", "orange", "yellow", "green", "blue","violet","midnightblue"]
canvas_height=1080
canvas_width=1920
canvas_colour='black'
line_width=1
randomh=random.randint(1,1080)
randomw=random.randint(1,1920)
randomh2=random.randint(1,1080)
randomw2=random.randint(1,1920)
####Define function
def square(self):
     canvas.create_line(randomh,randomw,randomh2,randomw2, width=line_width,          fill=random.choice(colors))
     canvas.create_line(300,100,400,100, width=line_width, fill=random.choice(colors))
     canvas.create_line(400,100,400,200, width=line_width, fill=random.choice(colors))
     canvas.create_line(400,200,300,200, width=line_width, fill=random.choice(colors))
###Main program
window=Tk()
window.title("Daniel Random Amazballs lines")
canvas=Canvas(bg=canvas_colour,height=canvas_height,width=canvas_width, highlightthickness=0)
canvas.pack()
###Click in window to start
window.bind("<Button-1>",square)
window.mainloop()
