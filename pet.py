from tkinter import *
import platform
import requests
from random import randint
from helpers.retrieve import getMessage
import time

#global Variables
root = Tk()
current = "./gifs/professor_walking.gif"
frameCount = {"./gifs/professor_walking.gif": 2, "./gifs/left_professor_walking.gif": 2, 
              "./gifs/professor_standing.gif": 9, "./gifs/professor_standing.gif": 9,
              "./gifs/pikachu_walking.gif": 16, "./gifs/left_pikachu_walking.gif": 16}
frames = [PhotoImage(file="./gifs/professor_walking.gif", format = 'gif -index %i' %(i)) for i in range(frameCount["./gifs/professor_walking.gif"])]
framesPair = {"./gifs/professor_walking.gif": "./gifs/professor_standing.gif", "./gifs/professor_standing.gif": "./gifs/professor_walking.gif",
              "./gifs/left_professor_walking.gif": "./gifs/professor_standing.gif", "./gifs/professor_standing.gif": "./gifs/left_professor_walking.gif"} 
frame_width = frames[0].width()
frame_height = frames[0].height() -4
screen_width  =  root.winfo_screenwidth()
screen_height =  root.winfo_screenheight()
walk_pos = - frame_width
left_boundary = 0 - (frame_width)
right_boundary = screen_width - (frame_width * 2)
velocity = 5
waitTime = 4 # Initial Wait Time
globalTime = time.time()

#animate gif
def gif(ind, walk_pos):
    global velocity
    global waitTime
    global globalTime
    global frames
    global framesPair
    global current

    frame = frames[ind%frameCount[current]]
    pet.configure(image=frame) 
    ind += 1
  
    #Change directions
    if ((time.time() -globalTime > waitTime) and (velocity != 0)):
        velocity = 0
        waitTime = randint(6,10)
        globalTime = time.time()
        if (current in framesPair):
            current = framesPair[current]
            frames = [PhotoImage(file=current, format = 'gif -index %i' %(i)) for i in range(frameCount[current])]
            
    elif ((time.time() -globalTime > waitTime) and (velocity == 0)):
        velocity = 5 if randint(0,1) == 1 else -5
        waitTime = randint(8,12)
        globalTime = time.time()
        if (current in framesPair):
            current = framesPair[current]
            frames = [PhotoImage(file=current, format = 'gif -index %i' %(i)) for i in range(frameCount[current])]
    
        # Case when they stop near the edge
        if walk_pos > right_boundary:
            velocity = -abs(velocity)

        elif walk_pos < left_boundary:
            velocity = abs(velocity)
        
    else:
        if walk_pos > right_boundary:
            velocity = -velocity
        elif walk_pos < left_boundary:
            velocity = -velocity

    # Change orientation if walking base on velocity
    
    if ((velocity < 0 ) and ("walking" in current) and ("left_" not in current)):
            current = "./gifs/" + "left_"+current[7:]
            frames = [PhotoImage(file=current, format = 'gif -index %i' %(i)) for i in range(frameCount[current])]
    if ((velocity > 0 ) and ("walking" in current) and ("left_" in current)):
            current = "./gifs/" + current[12:]
            frames = [PhotoImage(file=current, format = 'gif -index %i' %(i)) for i in range(frameCount[current])]


    walk_pos += velocity
    root.after(150, gif, ind,walk_pos)
    root.geometry("{0}x{1}+{2}+{3}".format(frame_width * 3, frame_height*2, walk_pos,screen_height - (frame_height * 2)))
   

#window configurations
root.config(highlightbackground='black', background='black')
root.overrideredirect(True)

#setting transparency
if (platform.system() == 'Windows'):
  root.wm_attributes("-transparentcolor", 'black')
  messagebox = Label( root, text="", bd=0, bg='black', pady=10, fg='white')
   
else:
  root.wm_attributes("-transparent", True)
  root.config(bg='systemTransparent')
  messagebox = Label( root, text="", bd=0, bg='systemTransparent', pady=10)


# windowclick
def mouseClick( event ):  
    message = getMessage("mom")
    messagebox.configure(text= message, font=('Times', 15))

#setting label
root.after(0, gif,0, walk_pos)
messagebox.pack()

pet = Label(root, bd=0, bg='black')
pet.bind( "<Button-1>", mouseClick )
pet.pack()

def pikachuChange():
    global frames
    global frame_height
    global current
    global velocity
    current = './gifs/pikachu.gif'
    if (velocity >= 0):
        current = './gifs/pikachu_walking.gif'
    else:
        current = './gifs/left_pikachu_walking.gif'
    
    frames = [PhotoImage(file=current, format = 'gif -index %i' %(i)) for i in range(frameCount[current])]
    frame_height = frames[0].height() +10
    messagebox.configure(text= "", font=('Times', 15))

def gasskoChange():
    global frames
    global frame_height
    global velocity
    global current

    if (velocity == 0):
        current = './gifs/professor_standing.gif'
        frames = [PhotoImage(file='./gifs/professor_standing.gif', format = 'gif -index %i' %(i)) for i in range(frameCount["./gifs/professor_standing.gif"])]
        frame_height = frames[0].height() -4

    else:
        
        if (velocity > 0):
            current = './gifs/professor_walking.gif'
        else:
            current = './gifs/left_professor_walking.gif'
        frames = [PhotoImage(file=current, format = 'gif -index %i' %(i)) for i in range(frameCount[current])]
        frame_height = frames[0].height() -6

    messagebox.configure(text= "", font=('Times', 15))

menu = Menu(root)
menu.add_command(label='Pikachu',command=pikachuChange)
menu.add_separator()
menu.add_command(label="Gassko", command=gasskoChange)

if (platform.system() == 'Darwin'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))

# Start the main event loop
root.mainloop()




