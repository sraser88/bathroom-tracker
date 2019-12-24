from guizero import App, Text, PushButton, TextBox, Picture
import os, time, math, datetime
from sense_hat import SenseHat

d = datetime.datetime.today()
inputFilename = 'log.txt'
bathroomLog = open(inputFilename, 'a')
bathroomLog.write('Current date and time: %s \n' % d)
fileOpen= True
startTime = 0.0
directions1 = "Please enter your name & period"
directions2 = " and leave your cell phone by the computer."

sense = SenseHat()
red = (255,0, 0)
green = (0, 255, 0)

app = App(bg="white", layout="grid")




def studentLeaving():
    global bathroomLog, startTime, fileOpen, period, firstName, lastName, cellLeft
    if not fileOpen:
        bathroomLog = open(inputFilename, 'a')
        fileOpen = True
    bathroomLog.write('%s %s %s %s' % (period.value, firstName.value, lastName.value, cellLeft.value))
    bathroomLog.write("\t")
    startTime = time.time()
    sense.clear(red)


def studentReturning():
    global startTime, fileOpen, firstName, lastName, period, cellLeft
    endTime = time.time()
    totalTime = endTime - startTime
    bathroomLog.write(str(round(totalTime)))
    bathroomLog.write('\n')
    bathroomLog.close()
    firstName.clear()
    lastName.clear()
    period.clear()
    cellLeft.clear()
    fileOpen = False
    sense.clear(green)


label = Text(app, "Bathroom Tracker", size=18, grid=[1,0])
instructions = Text(app, text = directions1, size=10, grid=[0,1])
instructions2 = Text(app, text=directions2, size=10, grid=[1,1])
fNameLabel = Text(app, text="First Name", grid = [0,2])
firstName = TextBox(app, text="", grid=[1,2])
lNameLabel = Text(app, text="Last Name", grid=[0,3])
lastName = TextBox(app, text="", grid=[1,3])
periodLabel = Text(app, text="Period", grid=[0,4])
period = TextBox(app, text="", grid=[1,4])
cellLabel = Text(app, text="Cell Phone Left?", grid=[0,5])
cellLeft = TextBox(app, text="", grid=[1,5])
leaveButton = PushButton(app, text="Leave Class", command=studentLeaving, grid=[0,6])
returnButton = PushButton(app, text="Return to Class", command=studentReturning, grid=[1,6])
logo = Picture(app, image="/home/pi/Desktop/CHS_logo.png", height=200, width=200, grid=[1,7])

app.display()

