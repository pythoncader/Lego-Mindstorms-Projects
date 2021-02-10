#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import socket

# Write your program here
ULTRASONIC_sense = UltrasonicSensor(Port.S3)
my_stopwatch = StopWatch()

#brick.sound.beep()
client_connection = socket.socket()
port = 12345
client_connection.bind(('', port))
client_connection.listen(5)
print('Waiting for connection...')
brick.display.text('Waiting for connection')
brick.display.text('    with computer...')
to_client, addr = client_connection.accept()
#brick.sound.beep(1500, 200)
brick.display.clear()
brick.display.text('Connection successful!')
wait(500)


my_stopwatch.reset()
while not any(brick.buttons()):
    #mystr = str(input("You: "))
    mystr = str(my_stopwatch.time()/1000)+',' +str(ULTRASONIC_sense.distance())
    to_client.send(mystr.encode())
    str(to_client.recv(1024).decode())
    #brick.display.clear()
    #brick.display.text( "Server: "+str(to_client.recv(1024).decode()))

mystr = 'end'
to_client.send(mystr.encode())
brick.display.clear()
brick.display.text( "Server: ")
brick.display.text(str(to_client.recv(1024).decode()))
to_client.close()
wait(700)
brick.display.clear()
brick.display.text('Connection ended!')
wait(1000)