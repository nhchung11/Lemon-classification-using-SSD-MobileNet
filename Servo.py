import time
from adafruit_servokit import ServoKit
# Set channels to the number of servo channels on your kit.
# 16 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
# kit.servo[2].angle = 90

mAS = kit.servo[0]
cHS = kit.servo[1]
cAS = kit.servo[2]
cAS2 = kit.servo[3]
pS = kit.servo[5]
finished = True

def initArm():
    initHeight = 80
    initPosition = 150
    initAngle = 120
    initAngle2 = 139
    initCap = 30


    cHS.angle = initHeight
    time.sleep(0.5)

    cAS.angle = initAngle
    time.sleep(0.5)

    mAS.angle = initPosition
    time.sleep(0.5)

    cAS2.angle = initAngle2
    time.sleep(0.5)

    pS.angle = initCap
    time.sleep(0.5)

def movServo(nameServo, initAngle, desAngle, speed):
    dis = abs(initAngle - desAngle)
    step = int(dis/2)
    for i in range(1, step, 1):
        if(desAngle >=initAngle):
            initAngle +=2
            nameServo.angle=initAngle
            time.sleep(speed/1000)
        else:
            initAngle -=2
            nameServo.angle=initAngle
            time.sleep(speed/1000)

def move_to_good_box():
    time.sleep(6)
    movServo(cHS, 150, 35, 50)
    time.sleep(0.001)
    movServo(mAS, 90, 150, 50)
    time.sleep(0.001)
    movServo(cAS, 90, 98, 50)
    time.sleep(0.001)
    movServo(pS, 30, 80, 50)
    time.sleep(0.001)
            
    movServo(mAS, 150, 130, 50)
    time.sleep(0.001)
    movServo(cHS, 35, 135, 50)
    time.sleep(0.001)
    movServo(cAS, 98, 90, 50)
    time.sleep(0.001)
    movServo(pS, 80, 30, 50)
    time.sleep(0.001)
    movServo(cAS, 70, 105, 50)


def move_to_bad_box():
    time.sleep(6)
    movServo(cHS, 150, 35, 50)
    time.sleep(0.001)
    movServo(mAS, 90, 150, 50)
    time.sleep(0.001)
    movServo(cAS, 90, 98, 50)
    time.sleep(0.001)
    movServo(pS, 30, 80, 50)
    time.sleep(0.001)
            
    movServo(mAS, 150, 130, 50)
    time.sleep(0.001)
    movServo(cHS, 35, 180, 50)
    time.sleep(0.001)
    movServo(cAS, 98, 70, 50)
    time.sleep(0.001)
    movServo(pS, 80, 30, 50)
    time.sleep(0.001)
    movServo(cAS, 70, 105, 50)