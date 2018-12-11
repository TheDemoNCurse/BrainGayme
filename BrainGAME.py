# Ex1.py

from gturtle import *
from random import*

def showLamp(col):
    setPos(0, 0)
    setPenColor(col)
    dot(100)
    if (col == 0):
        setPenColor("red")
        dot(100)
    elif (col == 1):
        setPenColor("yellow")
        dot(100)
    elif (col == 2):
        setPenColor("green")
        dot(100)
    elif (col == 3):
        setPenColor("blue")
        dot(100)
    else:
        setPenColor("white")
        dot(100)        

def showButton():
    setPos(100, 0)
    setPenColor("red")
    dot(50)
    setPos(-100, 0)
    setPenColor("green")
    dot(50)
    setPos(0, 100)
    setPenColor("blue")
    dot(50)
    setPos(0, -100)
    setPenColor("yellow")
    dot(50)
    
def setup():
    col = 5
    showButton()
    showSequence()
    
def showSequence():
    for i in range(n):
        col = seq[i]
        showLamp(col)
        delay(1000)
        showLamp(5)
        delay(500)
        
@onMousePressed
def pressed(x, y):
    moveTo(x, y):
        if getPixelColorStr() == "red":
            

# ------------------ main ------------------
Options.setPlaygroundSize(400, 400)    
makeTurtle()
ht()
penUp()
clear("black")
setTitle("Brain Game")
addStatusBar(30)


n = randint(1,3)
setStatusText("Showing sequences with length: " + str(n) + "...")
seq = []
for i in range(n):
    seq.append(randint(0, 3))
setup()