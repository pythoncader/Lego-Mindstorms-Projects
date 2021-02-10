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
right_motor = Motor(Port.D)
left_motor = Motor(Port.A)
IR_sense = InfraredSensor(Port.S4)
brick.display.text('Waiting for connection')
brick.display.text('   with computer...')
print('Waiting for connection with computer...')


main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # build a socket (family address type internet, TCP protocol)
main_connection.bind(('', 12880)) # prepares to listen (all potential customers, on port 12800)
main_connection.listen(5) # listen to up to 5 customers before validation
connection_with_client, connection_info = main_connection.accept() # blocks the program as long as there is no customer request
# returns the client socket, (client IP, client port)

brick.display.clear()
brick.display.text('Connection Successful!')
print('Connection Successful!')


brick.display.clear()
myloopnum = 0
while not any(brick.buttons()): # as long as the brick's buttons aren't pressed
    myloopnum += 0.2
    message = str(myloopnum) + "," + str(IR_sense.distance()) + ","
    message = message.encode() # transform string into binary for transmission
    connection_with_client.send(message)
    brick.display.text(str(message))
    if myloopnum % 7 == 0 and myloopnum > 7:
        brick.display.clear()

connection_with_client.send(b"end")
connection_with_client.close() # end of connection to the graphical client
print("Connection ended!")
brick.display.clear()
brick.display.text('Connection ended!')
wait(1000)
