import socket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
from time import sleep


Ev3IP = '10.50.0.117'
port = 12880
connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_with_server.connect ((Ev3IP, port))
print("Connection established with EV3 on port {}!". format (port))



plt.style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(111)

x = []
y = []

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def __str__(self):
        return '('+str(self._x)+', '+str(self._y)+')'
    def changevalue(self, x, y):
        self._x = x
        self._y = y

    def movex(self, startvalue, amount):
        self._x = startvalue + amount

    def movey(self, startvalue, amount):
        self._y = startvalue + amount

    def graph(self):
        # x-axis values 
        x.append(self._x)
        # y-axis values 
        y.append(self._y)
        plt.cla()
        plt.plot(x, y)
    def getCurrentSpot(self):
        CurrentSpot = [self._x, self._y]
        return CurrentSpot





wherebeen = []
received_message = connection_with_server.recv(1024) # length of the message <1024
decoded_message = received_message.decode()
print('This is the decoded message:', decoded_message)
pos = decoded_message.split(",")
pos = [float(pos[0]),float(pos[1])]
currentx, currenty = pos[0], pos[1]
myrobot = Point(currentx, currenty)
#print(myrobot)

def animate(i):
    received_message = connection_with_server.recv(1024) # length of the message <1024
    decoded_message = received_message.decode()
    #print(decoded_message)
    pos = decoded_message.split(",")

    if pos[0] != 'end' and pos[0] != '' and pos[1] != '':
        print(pos)
        xpos = pos[0]
        ypos = pos[1]
        currentx = float(xpos)
        currenty = float(ypos)
        myrobot.changevalue(currentx, currenty)
        wherebeen.append([currentx, currenty])
        myrobot.graph()

    else:
        connection_with_server.close() # close connection
        sys.exit('Connection ended!')
    
    plt.scatter(currentx, currenty, s = 500, color='green', marker="X")
    ax.set_xlim(left=currentx-50, right=currentx+50)
    #ax.set_ylim(bottom=currenty-50, top=currenty+50)
    ax.set_ylim(bottom=0, top=110)


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.tight_layout()
plt.show()
print('Myrobot is at this point:', myrobot.getCurrentSpot())
connection_with_server.close() # close connection
sys.exit('Connection ended!')