import socket
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import sleep

def whatcolor(mycolornum):
    if mycolornum == 0:
        print("\nNo color sensed...")
        return 'White'
    elif mycolornum == 1:
        print("\nBlack")
        return 'Black'
    elif mycolornum == 2:
        print("\nBlue")
        return 'Blue'
    elif mycolornum == 3:
        print("\nGreen")
        return 'Green'
    elif mycolornum == 4:
        print("\nYellow")
        return 'Yellow'
    elif mycolornum == 5:
        print("\nRed")
        return 'Red'
    elif mycolornum == 6:
        print("\nWhite")
        return 'White'
    elif mycolornum == 7:
        print("\nBrown")
        return 'Brown'
s = socket.socket()
s.connect(('10.50.0.119', 12346))

plt.style.use('fivethirtyeight')
fig = plt.figure(num=None, figsize=[10, 7])
ax = fig.add_subplot(111)
rcvdData = ''
myloopnum = 1
x = []
y = []
def animate(i):
    rcvdData = s.recv(1024).decode()
    while rcvdData != 'end':
        rcvdDatalist = rcvdData.split(',')
        if 'None' not in rcvdDatalist and '' not in rcvdDatalist:
            rcvdDatalist[0] = float(rcvdDatalist[0])
            rcvdDatalist[1] = float(rcvdDatalist[1])
            # x-axis values
            x.append(rcvdDatalist[0])
            # y-axis values
            y.append(rcvdDatalist[1])
            plt.cla()
            plt.plot(x, y)
            #sendData = str(input("You: "))
            sendData = 'received data!'
            s.send(sendData.encode())
            mycolor = whatcolor(y[-1])
            plt.scatter(rcvdDatalist[0], rcvdDatalist[1], s = 3000, color=mycolor, marker=".")
            plt.xlabel('Time (seconds)')
            
            if y[-1] != 0:
                plt.ylabel(mycolor)
            else:
                plt.ylabel('No color sensed')

            ax.set_xlim(left=rcvdDatalist[0]-15, right=rcvdDatalist[0]+15)
            #ax.set_ylim(bottom=currenty-50, top=currenty+50)
            ax.set_ylim(bottom=0, top=7.4)
            break
        else:
            print('faulty list:', rcvdDatalist)
            sendData = 'ending process...'
            s.send(sendData.encode())
            s.close()
            sys.exit('Connection ended! (the color sensor was probably unplugged)')
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