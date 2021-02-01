# Developer - Smruti Prakash Rout (Smruti-official)


import turtle as tu


Smruti = tu.Turtle() #Turtle object
wn = tu.Screen() #Screen Object

wn.bgcolor("black") #Screen Bg color
Smruti.left(90) #moving the turtle 90 degrees towards left
Smruti.speed(20000000000000000000000)#setting the speed of the turtle


def  draw(l): #recursive function taking length 'l' as argument
    if(l<10):
        return
    else:

        Smruti.pensize(2) #Setting Pensize
        Smruti.pencolor("yellow") #Setting Pencolor as yellow
        Smruti.forward(l) #moving turtle forward by 'l'
        Smruti.left(30) #moving the turtle 30 degrees towards left
        draw(3*l/4) #drawing a fractal on the left of the turtle object 'Smruti' with 3/4th of its length
        Smruti.right(60) #moving the turtle 60 degrees towards right
        draw(3*l/4) #drawing a fractal on the right of the turtle object 'Smruti' with 3/4th of its length
        Smruti.left(30) #moving the turtle 30 degrees towards left
        Smruti.pensize(2)
        Smruti.backward(l) #returning the turtle back to its original psition

draw (20) # drawing 20 times 

Smruti.right(90)
Smruti.speed(20000000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(2)
        Smruti.pencolor("magenta") #magenta
        Smruti.forward(l)
        Smruti.left(30)
        draw(3*l/4)
        Smruti.right(60)
        draw(3*l/4)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)

draw (20)


Smruti.left(270)
Smruti.speed(20000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(2)
        Smruti.pencolor("red") #red
        Smruti.forward(l)
        Smruti.left(30)
        draw(3*l/4)
        Smruti.right(60)
        draw(3*l/4)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)

draw (20)

Smruti.right(90)
Smruti.speed(200000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(2)
        Smruti.pencolor('#FFF8DC') #white
        Smruti.forward(l)
        Smruti.left(30)
        draw(3*l/4)
        Smruti.right(60)
        draw(3*l/4)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)

draw(20)
########################################################

def  draw(l):
    if(l<10):
        return
    else:

        Smruti.pensize(3)
        Smruti.pencolor("lightgreen") #lightgreen
        Smruti.forward(l)
        Smruti.left(30)
        draw(4*l/5)
        Smruti.right(60)
        draw(4*l/5)
        Smruti.left(30)
        Smruti.pensize(3)
        Smruti.backward(l)

draw (40)

Smruti.right(90)
Smruti.speed(2000000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(3)
        Smruti.pencolor("red") #red
        Smruti.forward(l)
        Smruti.left(30)
        draw(4*l/5)
        Smruti.right(60)
        draw(4*l/5)
        Smruti.left(30)
        Smruti.pensize(3)
        Smruti.backward(l)

draw (40)


Smruti.left(270)
Smruti.speed(2000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(3)
        Smruti.pencolor("yellow") #yellow
        Smruti.forward(l)
        Smruti.left(30)
        draw(4*l/5)
        Smruti.right(60)
        draw(4*l/5)
        Smruti.left(30)
        Smruti.pensize(3)
        Smruti.backward(l)

draw (40)

Smruti.right(90)
Smruti.speed(20000000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(3)
        Smruti.pencolor('#FFF8DC') #white
        Smruti.forward(l)
        Smruti.left(30)
        draw(4*l/5)
        Smruti.right(60)
        draw(4*l/5)
        Smruti.left(30)
        Smruti.pensize(3)
        Smruti.backward(l)

draw (40)

########################################################
def  draw(l):
    if(l<10):
        return
    else:
        
        Smruti.pensize(2)
        Smruti.pencolor("cyan") #cyan
        Smruti.forward(l)
        Smruti.left(30)
        draw(6*l/7)
        Smruti.right(60)
        draw(6*l/7)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)
        
draw (60)

Smruti.right(90)
Smruti.speed(20000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(2)
        Smruti.pencolor("yellow") #yellow
        Smruti.forward(l)
        Smruti.left(30)
        draw(6*l/7)
        Smruti.right(60)
        draw(6*l/7)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)
        
draw (60)


Smruti.left(270)
Smruti.speed(20000000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(2)
        Smruti.pencolor("#FE0809") #red
        Smruti.forward(l)
        Smruti.left(30)
        draw(6*l/7)
        Smruti.right(60)
        draw(6*l/7)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)
        
draw (60)

Smruti.right(90)
Smruti.speed(20000000000000000)

#recursion
def  draw(l):
    if(l<10):
        return
    else:
        Smruti.pensize(2)
        Smruti.pencolor('#83FFC1') #light green
        Smruti.forward(l)
        Smruti.left(30)
        draw(6*l/7)
        Smruti.right(60)
        draw(6*l/7)
        Smruti.left(30)
        Smruti.pensize(2)
        Smruti.backward(l)
draw(60)
wn.exitonclick()
