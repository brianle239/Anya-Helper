from tkinter import *
import platform
import requests
from random import randint

category = ['sleep', 'dissapointed', 'watching']
response = requests.get("http://34.238.250.217:8000/"+category[0])

#global Variables
root = Tk()
frameCnt = 16
frames = [PhotoImage(file='pikachu.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]
frame_width = frames[0].width()
frame_height = frames[0].height() 
screen_width  =  root.winfo_screenwidth()
screen_height =  root.winfo_screenheight()
walk_pos = (frame_width * 2)
left_boundary = (frame_width * 2)
right_boundary = screen_width - (frame_width * 2)
velocity = 5

#animate gif
def gif(ind, walk_pos,velocity):
    frame = frames[ind]
    pet.configure(image=frame) 

    #iterating through frames
    ind += 1
    if ind == frameCnt:
        ind = 0

    #Change directions
    if walk_pos > right_boundary:
        velocity = -velocity
    elif walk_pos < left_boundary:
        velocity = -velocity

    walk_pos += velocity
    root.after(150, gif, ind,walk_pos, velocity)
    root.geometry("{0}x{1}+{2}+{3}".format(frame_width * 3, frame_height*2, walk_pos,screen_height - (frame_height * 2)))
   

#window configurations
root.config(highlightbackground='black', background='black')
root.overrideredirect(True)

#setting transparency
if (platform.system() == 'Windows'):
  root.wm_attributes("-transparentcolor", 'black')
  messagebox = Label( root, text="", bd=0, bg='black', pady=10)
   
else:
  root.wm_attributes("-transparent", True)
  root.config(bg='systemTransparent')
  messagebox = Label( root, text="", bd=0, bg='systemTransparent', pady=10)

#setting label
root.after(0, gif,0, walk_pos, velocity)
messagebox.pack()

pet = Label(root, bd=0, bg='black')
pet.pack()

def mouseClick( event ):  
    Dick = response.json()
    message = Dick[str(randint(0,2))]
    messagebox.configure(text= message, font=('Times', 15))
   
 
pet.bind( "<Button>", mouseClick )

#calling loop
root.mainloop()



