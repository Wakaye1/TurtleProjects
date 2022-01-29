import turtle
import time

screen = turtle.Screen() #turtle screen
screen.bgcolor("white") #background of the screen
screen.setup(width=600, height=600) #geometry of the GUI
screen.title("WAKAYE") #title of the GUI
screen.tracer(0) #tracer for the GUI

abba = turtle.Turtle() #the turtle
abba.hideturtle() #make the turtle invisible
abba.speed(0) #setting the speed to 0
abba.pensize(3) #setting the pensize to 3


def clock(period, minutee, secondd, abba): #function with 4 parameters

    abba.up() #not ready to draw
    abba.goto(0, 210) #positioning the turtle
    abba.setheading(180) #setting the heading to 180
    abba.color("red") #setting the color of the pen to red
    abba.pendown() #starting to draw
    abba.circle(210) #a circle with the radius 210

    abba.up() #not ready to draw
    abba.goto(0, 0) #positioning the turtle
    abba.setheading(90) #same as seth(90) in newer version

    for z in range(12): #loop 
        abba.fd(190) #moving forward at 190 units
        abba.pendown() #starting to draw
        abba.fd(20) #forward at 20
        abba.penup() #not ready to draw
        abba.goto(0, 0) #positioning the turtle
        abba.rt(30) #right at an angle of 30 degrees

    hands = [("black", 80, 12), ("black", 150, 60), ("black", 110, 60)] #the color and the hands set
    time_set = (period, minutee, secondd) #setting the time

    for hand in hands: #loop
        time_part = time_set[hands.index(hand)] #time part in the hand index in hands of time_Set
        angle = (time_part/hand[2])*360 #setting the angle for the clock
        abba.penup() #not ready to draw
        abba.goto(0, 0) #positioning the turtle
        abba.color(hand[0]) #setting the color of the hand
        abba.setheading(90) #same as seth(90)
        abba.rt(angle) #right at an angle of "right"
        abba.pendown() #ready to draw
        abba.fd(hand[1]) 


while True:
    period = int(time.strftime("%I")) 
    minutee = int(time.strftime("%M")) 
    secondd = int(time.strftime("%S")) 

    clock(period, minutee, secondd, abba)  
    time.sleep(1)
    abba.clear() 
