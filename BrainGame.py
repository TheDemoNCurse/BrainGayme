# Ex1.py / BrainGame

from gturtle import *
from random import*
from soundsystem import *

def showLamp(col): #creating the lamp in the middle that shows the sequence
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

def showButton(): #creating the 4 buttons around the middle lamp
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
    
def setup(): #starting the game
    showSequence()
    showButton()
    
    
def showSequence(): #showing the sequence
    for i in range(n):
        col = seq[i]
        showLamp(col)
        delay(1000)
        showLamp(5)
        delay(500)

@onMousePressed #clicking on the outer buttons and changing the lamp's color
def pressed(x, y):
        global buttonIndex
        buttonIndex = 0
        moveTo(x, y)
        if getPixelColorStr() == "red":
            buttonIndex = 0
        elif getPixelColorStr() == "yellow":
            buttonIndex = 1
        elif getPixelColorStr() == "green":
            buttonIndex = 2
        elif getPixelColorStr() == "blue":
            buttonIndex = 3
        elif getPixelColorStr() == "white":
            buttonIndex = -1
        elif getPixelColorStr() == "black":
            buttonIndex = -2
        showLamp(buttonIndex)    

@onMouseReleased #when mouse button is released, testing if sequence is right
def release(x, y):
    global clickCount
    global buttonIndex
    global n
    global col
    global seq
    showLamp(-1)
    if seq[clickCount] == buttonIndex:
        clickCount += 1
        if clickCount == len(seq): #if the whole sequence has been done and everything was right then mission passed
            setStatusText("Mission passed, Respect +")
            
            openSoundPlayerMP3("gta_safull.mp3") #play gta theme song just for fun 
            play()
            msgDlg("RESPECT +")
            
            cont = askYesNo("Continue? Difficulty will increase.") #play again with +1 sequence
            if cont == True:
                clear("black")
                n += 1
                setStatusText("Showing sequences with length: " + str(n) + "...")
                clickCount = 0
                del seq[:]
                for i in range(n):
                    seq.append(randint(0, 3))
                print(seq)
                setup()
                
            elif cont == False: #if user chooses no then exiting program
                msgDlg("Thank you for playing! You reached Stage " + str(n-2) + ".")
                exit()
    else: #if not everything was right mission failed
        setStatusText("Misson failed, we´ll get em next time!")
        tryagain = askYesNo("Try again?")
        if tryagain == True: #setting up the game again to try again
            clickCount = 0
            setStatusText("Showing sequences with length: " + str(n) + "...")
            del seq[:]
            for i in range(n):
                seq.append(randint(0, 3))   
            setup()
        elif tryagain == False: #exiting the game if user chooses no
            msgDlg("Thank you for playing! You reached Stage " + str(n-3) + ".")
            exit()
            
# ------------------ main ------------------
Options.setPlaygroundSize(400, 400)    
makeTurtle()
ht()
penUp()
clear("black")
setTitle("Brain Game")
addStatusBar(30) #setting up the field

clickCount = 0
n = 3
setStatusText("Showing sequences with length: " + str(n) + "...")
seq = []
for i in range(n):
    seq.append(randint(0, 3))
setup()