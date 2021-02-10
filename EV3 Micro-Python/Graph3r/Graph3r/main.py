#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import socket
import math

# Write your program here

color = ColorSensor(Port.S3)
turnerIR = InfraredSensor(Port.S2)
frontIR = InfraredSensor(Port.S1)
ltrack = Motor(Port.C)
rtrack = Motor(Port.B)
IRturner = Motor(Port.A)


def turn(angle, speed=720, mywait=True):
    turnamount = (angle/90)*500
    rtrack.run_target(speed, -turnamount, Stop.BRAKE, False)
    ltrack.run_target(speed, turnamount, Stop.BRAKE, mywait)
    wait(200)

def turnleftmotor(angle, speed=720, mywait=True):
    turnamount = (angle/90)*1000
    rtrack.run_target(speed, -(0.15*turnamount), Stop.BRAKE, False)
    ltrack.run_target(speed, turnamount, Stop.BRAKE, mywait)
    wait(200)


def lookleft(turner):
    turner.run_target(5000, -10)
    wait(500)
    return turnerIR.distance()

def lookforward(turner):
    turner.run_target(5000, 90)
    wait(500)
    return turnerIR.distance()

def lookright(turner):
    turner.run_target(5000, 155)
    wait(500) 
    return turnerIR.distance()

def lookback(turner):
    return frontIR.distance()


IRturner.reset_angle(90)
ltrack.reset_angle(0)
rtrack.reset_angle(0)

rotation = 90
positionx = 0
positiony = 0



turnleftmotor(90)
wait(5000)

while frontIR.distance() > 40:
    positiony += ltrack.angle()
    ltrack.run(720)
    rtrack.run(720)

ltrack.stop(stop_type=Stop.BRAKE)
rtrack.stop(stop_type=Stop.BRAKE)
wait(500)
rtrack.reset_angle(0)
ltrack.reset_angle(0)
rtrack.run_target(720, 510, Stop.BRAKE, wait=False)
ltrack.run_target(720, -510, Stop.BRAKE)

rotation += 90

lookright(IRturner)
wait(500)




while not any(brick.buttons()):
    if frontIR.distance() > 40:
        if turnerIR.distance() < 40 and turnerIR.distance() > 25:
            print("Going Forward...")
            positiony += (math.sin(rotation) * 0.4) #sin(0) = y/d or sin(0) * d = y
            #Multiply the distance by the sine of that angle to get the change in y value
            #(0.4 because the robot moves that many rotations in 200 milliseconds)
            
            positionx += (math.cos(rotation) * 0.4)
            #same thing for the x value except it is the cosine

            ltrack.run(720)
            rtrack.run(720)
            wait(200)
            print("Position: ("+str(positionx)+","+str(positiony)+")")

        elif turnerIR.distance() > 40:
            print("Wall too far away... Turning")
            ltrack.stop(stop_type=Stop.BRAKE)
            rtrack.stop(stop_type=Stop.BRAKE)
            wait(1000)
            turnleftmotor(5)
            wait(1000)
                

        elif turnerIR.distance() < 25:
            print("Wall too close... Turning")
            #turn
    else:
        print("Obstacle detected in front... Turning")
        rtrack.run(720)
        ltrack.run(-720)
        wait(200)