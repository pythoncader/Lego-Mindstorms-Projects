#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import socket

def whatcolor(mycolornum):
    if mycolornum == 0:
        brick.display.clear()
        brick.display.text("No color sensed...", (30, 60))
    elif mycolornum == 1:
        brick.display.clear()
        brick.display.text("Black", (60, 60))
    elif mycolornum == 2:
        brick.display.clear()
        brick.display.text("Blue", (60, 60))
    elif mycolornum == 3:
        brick.display.clear()
        brick.display.text("Green", (60, 60))
    elif mycolornum == 4:
        brick.display.clear()
        brick.display.text("Yellow", (60, 60))
    elif mycolornum == 5:
        brick.display.clear()
        brick.display.text("Red", (60, 60))
    elif mycolornum == 6:
        brick.display.clear()
        brick.display.text("White", (60, 60))
    elif mycolornum == 7:
        brick.display.clear()
        brick.display.text("Brown", (60, 60))

# Write your program here
COLOR_sense = ColorSensor(Port.S2)
my_stopwatch = StopWatch()

#brick.sound.beep()
client_connection = socket.socket()
port = 12346
client_connection.bind(('', port))
client_connection.listen(5)
print('Waiting for connection...')
brick.display.text('Waiting for connection')
brick.display.text('    with computer...')
to_client, addr = client_connection.accept()
#brick.sound.beep(1500, 200)
brick.display.clear()
brick.display.text('Connection successful!')
wait(700)


my_stopwatch.reset()
while not any(brick.buttons()):
    currentcolor = COLOR_sense.color()
    if currentcolor == None:
        currentcolor = 0
    
    whatcolor(currentcolor)

    mytime = str(my_stopwatch.time()/1000)
    if currentcolor != '' and currentcolor != None:
        mystr = mytime+',' +str(currentcolor)
    else:
        currentcolor = 0
        mystr = mytime+',' +str(currentcolor)
    
    to_client.send(mystr.encode())
    str(to_client.recv(1024).decode())
    #brick.display.clear()
    #brick.display.text( "Server: "+str(to_client.recv(1024).decode()))
brick.display.clear()
brick.display.text('A button was pressed!')
wait(500)
mystr = 'end'
to_client.send(mystr.encode())
brick.display.clear()
brick.display.text( "Server: ")
brick.display.text(str(to_client.recv(1024).decode()))
wait(800)
to_client.close()
wait(700)
brick.display.clear()
brick.display.text('Connection ended!')
wait(1000)