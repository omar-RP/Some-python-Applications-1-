# i will start by importing the specific library (module), this library gives me the ability to create shapes and control it
import turtle
# now, i will create my screen that will host my game on it and i will give my screen a variable name "wind"
wind = turtle.Screen()
# then, i will give my whole game a name that will appear on the top of the screen
wind.title("Ping Pong Game")
#choosing the background color of the game screen
wind.bgcolor("black")
# now, i will set the size and position of the main window
wind.setup(width=800, height=600)
#i will prevent the scree from updatintg itself with out any permission
wind.tracer(0) 


# the second part of the code is about create the game components(bracket1 _ bracket2 _ ball)

#starting with cretae the first bracket and set its speed to make it move without any lagging
bracket1 = turtle.Turtle()
bracket1.speed(0) #"0" here define the fastest speed that the object can move with
# here i will specify the position on the screen, the shape and the color of the bracket
bracket1.goto(350,0) # i set the location close to the edge of the screen to make the best use of the screen in the game(here on the right side) 
bracket1.shape("square")
bracket1.color("blue")
# it's necessary to deal with the shadow that "turtle()" gonna make behind the object when it's moving
bracket1.penup()
#finally for the bracket1, i will modify its size because the its default size is 20px and that's so tiny to fit the game senario
bracket1.shapesize(stretch_wid=5, stretch_len=1) # here i doubled the width 5 times and kept the length as default

#Now, it's time to create bracket2, that will take the code as bracket1 with some mofication to fit it and make it suitable for the game
#starting with create the second bracket and set its speed to make it move without any lagging
bracket2 = turtle.Turtle()
bracket2.speed(0)  #"0" here define the fastest speed that the object can move with
# here i will specify the position on the screen, the shape and the color of the bracket
bracket2.goto(-350,0) # i set the location close to the edge of the screen to make the best use of the screen in the game(here on the left side) 
bracket2.shape("square")
bracket2.color("red")
# it's necessary to deal with the shadow that "turtle()" gonna make behind the object when it's moving
bracket2.penup()
#finally for the bracket2, i will modify its size because the its default size is 20px and that's so tiny to fit the game senario
bracket2.shapesize(stretch_wid=5, stretch_len=1) # here i doubled the width 5 times and kept the length as default

# the last component will be the ball, it will have the same code lines format with more modifications
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.goto(0,0) # it means that the position of the ball will be exactly in the middle of the screen
# i won't use the ".shapesize()" as i want the default size of (20px * 20px)
ball.shape("circle")
ball.color("white")
ball.dx = 0.3 # it represents the value(2.5px) of the distance that the ball gonna cut in each movement in the "x" direction
ball.dy = 0.3 # it represents the value(2.5px) of the distance that the ball gonna cut in each movement in the "y" direction


# this step is adding the score board to the game screen(i left as my last step but put it in the right position before launch the game)
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0) # it gives the highest speed in reshaping the score without any lagging 
score.color("white")
score.penup()
score.hideturtle() # this will hide any shapes from the background and let the numbers appear clearly
score.goto(0,260) # here i put hte score board in the middle of the screen but just a little up under the screen border 
score.write("player1: 0 player2: 0",align="center", font=("courier",24,"normal"))

# Now, moving to set the functions of the game components (the senario of the game palying)
# startin with bracket1
def bracket1_up():
    y = bracket1.ycor()  #here i am making the bracket movement focuses on the "y" coordinates
    y += 20  # each time it will move, it will move by the distance of 20px in the y direction (moving up)
    bracket1.sety(y) # the bracket now is following the new "y" syntax
# put the function syntax to be able to move down     
def bracket1_down():
    y = bracket1.ycor()  #here i am making the bracket movement focuses on the "y" coordinates
    y -= 20  # each time it will move, it will move by the distance of 20px in the y direction(moving down)
    bracket1.sety(y) # the bracket now is following the new "y" syntax     

# then coming to bracket2
def bracket2_up():
    y = bracket2.ycor()  #here i am making the bracket movement focuses on the "y" coordinates
    y += 20  # each time it will move, it will move by the distance of 20px in the y direction (moving up)
    bracket2.sety(y) # the bracket now is following the new "y" syntax
# put the function syntax to be able to move down     
def bracket2_down():
    y = bracket2.ycor()  #here i am making the bracket movement focuses on the "y" coordinates
    y -= 20  # each time it will move, it will move by the distance of 20px in the y direction(moving down)
    bracket2.sety(y) # the bracket now is following the new "y" syntax  

# To make use of the previous syntax, i will do the keyboared bindings
# to call these functions with a specific key for each function
wind.listen() # this function tells the window to be ready for any keypressing that will define an order of movement
wind.onkeypress(bracket1_up,"Up")
wind.onkeypress(bracket1_down,"Down")
wind.onkeypress(bracket2_up,"w")
wind.onkeypress(bracket2_down,"s")


#i will here create the main game loop to put a condition for the game to keep operating (it will be the last line of code)
while True:
    wind.update() # update the screen each time the loop run

    # Time to make the ball moving, i will put all the functions that will define the ball movements on the screen
    ball.setx(ball.xcor() + ball.dx) # apply the change(2.5px) i put on the ball movements in the "x" direction over its current position
    ball.sety(ball.ycor() + ball.dy) # the same thing as above but this time in the "y direction"

    # Now, i will start to put the coditions for the ball movements and make it fits the game senario

    # starting with the ball movements in the "x" directions 
    if ball.xcor() >390: # represents the ball passing the 290px on the "x" coordinates
        ball.goto(0,0) # makes it stick to 290px in the "x" coordinates
        ball.dx *= -1 # that will tell the ball to move in the opposite direction with a space of 2.5px each movement
        score1 += 1
        score.clear() # this function will delete any previous number from the background and show only the latest score each time 
        score.write("player1: {} player2: {}".format(score1,score2),align="center", font=("courier",24,"normal"))

    if ball.xcor() <-390: # represents the ball passing the 290px on the "x" coordinates
        ball.goto(0,0) # makes it stick to 290px in the "x" coordinates
        ball.dx *= -1 # that will tell the ball to move in the opposite direction with a space of 2.5px each movement
        score2 += 1
        score.clear() # this function will delete any previous number from the background and show only the latest score each time 
        score.write("player1: {} player2: {}".format(score1,score2),align="center", font=("courier",24,"normal"))

    # Moving to the ball movements in the "y" directions 
    if ball.ycor() >290: # represents the ball passing the 290px on the "y" coordinates
        ball.sety(290) # makes it stick to 290px in the "y" coordinates
        ball.dy *= -1 # that will tell the ball to move in the opposite direction with a space of 2.5px each movement

    if ball.ycor() <-290: # represents the ball passing the 290px on the "y" coordinates
        ball.sety(-290) # makes it stick to 290px in the "y" coordinates
        ball.dy *= -1 # that will tell the ball to move in the opposite direction with a space of 2.5px each movement


# one important step before the end of the code and that will be,
# setting the conditions for the ball hitting the brackets and then turn back
# starting now with "bracket1" 
    if(ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() < bracket1.ycor() +40 and ball.ycor() > bracket1.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1
# Now, i will repeat the same steps with "bracket2" but with some slight changes
    if(ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor() < bracket2.ycor() +40 and ball.ycor() > bracket2.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1 












