#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
color_sense = ColorSensor(Port.S2)
print("Black:", Color.BLACK)
print("Blue:", Color.BLUE)
print("Green:", Color.GREEN)
print("Yellow:", Color.YELLOW)
print("Red:", Color.RED)
print("White:", Color.WHITE)
print("Brown:", Color.BROWN)
currentcolor = -1
while not any(brick.buttons()):
    if color_sense.color() == None and currentcolor != 0:
        print("\nNo color sensed...")
        currentcolor = 0
    elif color_sense.color() == 1 and currentcolor != 1:
        print("\nBlack")
        currentcolor = 1
    elif color_sense.color() == 2 and currentcolor != 2:
        print("\nBlue")
        currentcolor = 2
    elif color_sense.color() == 3 and currentcolor != 3:
        print("\nGreen")
        currentcolor = 3
    elif color_sense.color() == 4 and currentcolor != 4:
        print("\nYellow")
        currentcolor = 4
    elif color_sense.color() == 5 and currentcolor != 5:
        print("\nRed")
        currentcolor = 5
    elif color_sense.color() == 6 and currentcolor != 6:
        print("\nWhite")
        currentcolor = 6
    elif color_sense.color() == 7 and currentcolor != 7:
        print("\nBrown")
        currentcolor = 7