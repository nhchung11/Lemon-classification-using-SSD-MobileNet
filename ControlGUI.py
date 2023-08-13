import keyboard
import time
from adafruit_servokit import ServoKit
# Set channels to the number of servo channels on your kit.
# 16 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
# kit.servo[2].angle = 90

import tkinter as tk 

def arrow_pressed(direction):
    if direction == "up":
        move_up()
    elif direction == "down":
        move_down()
    elif direction == "left":
        move_left()
    elif direction == "right":
        move_right()

        
mAS = kit.servo[0]
cHS = kit.servo[1]
cAS = kit.servo[2]
cAS2 = kit.servo[3]
pS = kit.servo[5]
finished = True

def initArm():
    cHS.angle = 90
    time.sleep(0.5)

    cAS.angle = 120
    time.sleep(0.5)

    mAS.angle = 130
    time.sleep(0.5)

    cAS2.angle = 135
    time.sleep(0.5)

    pS.angle = 35
    time.sleep(0.5)

initArm()

def move_left():
    cHS.angle=cHS.angle+10
    time.sleep(0.1)
def move_right():
    cHS.angle=cHS.angle-10
    time.sleep(0.1)
def move_down():
    if mAS.angle > 150:
        cAS.angle=cAS.angle - 5
        time.sleep(0.1)
    else:
        mAS.angle=mAS.angle + 5
    
def move_up():
    time.sleep(0.1)
    if mAS.angle < 120:
        cAS.angle = cAS.angle + 5
        time.sleep(0.1)
    else:
         mAS.angle=mAS.angle-10

def grab():
    pS.angle = 75
    
def release():
    pS.angle = 35

root = tk.Tk()
root.geometry("200x200")

# Create the arrow buttons
up_button = tk.Button(root, text="↑", command=lambda: arrow_pressed("up"))
up_button.pack(side=tk.TOP)

down_button = tk.Button(root, text="↓", command=lambda: arrow_pressed("down"))
down_button.pack(side=tk.BOTTOM)

left_button = tk.Button(root, text="←", command=lambda: arrow_pressed("left"))
left_button.pack(side=tk.LEFT)

right_button = tk.Button(root, text="→", command=lambda: arrow_pressed("right"))
right_button.pack(side=tk.RIGHT)

grab_button = tk.Button(root, text = "Grab", command = grab)
grab_button.place(x = 60, y = 50)

release_button = tk.Button(root, text = "Release", command = release)
release_button.place(x = 60, y = 80)

# Start the GUI loop
root.mainloop()
    