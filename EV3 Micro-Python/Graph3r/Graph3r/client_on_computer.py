import socket
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

IPaddress = str(input("Please write the ip address of the ev3...\n"))
s = socket.socket()
s.connect((IPaddress, 12345))

plt.style.use('fivethirtyeight')
fig = plt.figure(num=None, figsize=[10, 7])
ax = fig.add_subplot(111)
rcvdData = 'None'
x = []
y = []
def animate(i):
    rcvdData = s.recv(1024).decode()
    if rcvdData != 'end':
        rcvdDatalist = rcvdData.split(',')
        rcvdDatalist[0] = float(rcvdDatalist[0])
        rcvdDatalist[1] = float(rcvdDatalist[1])
        mypoint = "("+str(rcvdDatalist[0])+", "+str(rcvdDatalist[1])+")"
        # x-axis values
        x.append(rcvdDatalist[0])
        # y-axis values
        y.append(rcvdDatalist[1])
        plt.cla()
        plt.plot(x, y)
        #sendData = str(input("You: "))
        sendData = 'received data!'
        s.send(sendData.encode())
        plt.scatter(rcvdDatalist[0], rcvdDatalist[1], s = 500, color='green', marker="X")
        plt.xlabel('Time (seconds)')
        plt.ylabel('Distance (%)')
        ax.set_xlim(left=rcvdDatalist[0]-15, right=rcvdDatalist[0]+15)
        #ax.set_ylim(bottom=currenty-50, top=currenty+50)
        ax.set_ylim(bottom=0, top=110)
    else:
        sendData = 'ending process...'
        s.send(sendData.encode())
        s.close()
        sys.exit('Connection ended!')


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.show()


sendData = 'ending process...'
s.send(sendData.encode())
s.close()
sys.exit('Connection ended!')