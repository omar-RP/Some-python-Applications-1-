# Starting with importing the essential libraries that gonna supply all the functions that i am gonna need to program the game
import random
import curses


# name a variable for the whole screen view , and from the curses library , call for the ".initscr()".
# then from "curses" library i call for the function ".curs_set()" and make it equal to 0, to tell the cursor to not appear on the the screen
s = curses.initscr()
curses.curs_set(0)

# then, i will make 2 variables who will represent the screen height & width and they will be "sh & sw" 
# and i will call for ".getmaxyx()" thta will return the dimension of the screen in a tuple (y,x), they represent the height and the width of the window
sh, sw = s.getmaxyx()

# creating a variable that represents a new window through this function ".newwin()" ,
# it's typical foem is "newwin(nlines,ncols, begin_y, begin_x)", as left_upper corner in (begin_y, begin_x) & the height_width as (nlines,ncols)
w = curses.newwin(sh, sw, 0, 0)

# telling the computer that the user is going to use the keyboard by using ".keypad()"
# also i can set a refresh rate for my screen by using ".timeout()" 
w.keypad(1)
w.timeout(100)

# put the location of the snake when the game starts;
snk_x = sw // 4  # it means that the snake will appear in a quater value of the screen width, if th screen width = 100px, snk_x = 25px
snk_y = sh //2   # it means that the snake will appear in the middle of the screen height

# this list gonna hold the coordinates of the snake body parts when the game starts
snake = [
    [snk_y,snk_x]
    [snk_y,snk_x-1]
    [snk_y,snk_x-2]
]

# Now, deciding the locatio, attributes and theshape of the food for the snake
# the ".Acs_pi()", choose the presenting way of the snake, also"w.add(y,x,ch[,attr])
# by default,the character position and attribute are the current settings for the window object
food = [sh // 2, sw//2]
w.addch(food[0],food[1], curses.ACS_PI) 

# DECIDING THE THE FIRST DIRECTION FOR THE Snake and here it will be to the right;
key = curses.KEY.RIGHT

# Her, i will start creating an infinite loop of the snake moving, to make it keep running until the user lose 
# Then, i used the ".getch()" to recieve the user input (the next key direction),
# Note, it will be the same key if he didn't press any new keys
while True :
    next_key = w.getch()
    key = key if next_key == -1 else next_key

# Now, i will put the senarios for the snake to crash, and these are;
# snake[0,0] in [0,sh] it means that the snake hit the screen from top or bottom, also
# snake[0,1] in [0,sw] it means that the snake hit the scren from left or right, finally
# snake[0] in [1:] it means that the snake hit itself
if snake[0][0] in [0,sh] or snake[0][0] in [0,sw] or snake[0] in snake [1:]:
    curses.endwin()
    quit()

# i will make the prediction for the snake, next move
new_head = [snake[0][0], snake[0][1]]

# NOW, i am putting all the possible direction that the user can move the snake in and that's by;
# putting 4 if conditions that represent the 4 directions of moving for the snake 
# the, i use the ".insert()" to insert the new direction of the head 
if key == curses.KEY_DOWN:
    new_head[0] += 1
if key == curses.KEY_UP:
    new_head[0] -= 1
if key == curses.KEY_RIGHT:
    new_head[1] += 1
if key == curses.KEY_LEFT:
    new_head[1] -= 1

# putting the steps for the snake eating the food, but i need first to create the food, then
# use the "random" library to make the position of the food not expected at all
if snake[0] == food :
    food = None
    while food is none:
        # we gonna use ".rundint()" and make the position of the food from the first point on the screen
        # (height or width) until before the border of the screen by only 1 point .
        nf = [
            random. rundint(1, sh-1), 
            random. randint(1, sw-1)
        ]

# put a condition that makes the food appear in any random position except the sanke's body itself
    food = nf if nf not in snake else None

# now, i will give a specific look and a way for the food to appear for snake on the screen by using "curses.ASC_PI"
    w.addch(food[0], food[1], curses.ACS_API) 

# i am putting a very important step as, if the snake didn't eat the food, the tail shouldn't grow 
# and that gonna be by using ".pop()" as it deletes the last value in the list 
# ex: list = [1,2,3,4], list.pop() ,  list -> [1,2,3]
else:
    tail = snake.pop()
    w.addch(tail[0], tail[1], ' ') # here i am putting the coordinates of the snake tail and replace it with no value

# Here, the fnal code line that will show the final form of the snake when i'm starting my program
    w.addch(sbake[0][0], snake[0][1], curses.ASC_CKBOARD)





























