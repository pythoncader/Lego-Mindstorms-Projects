#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import print, wait
from pybricks.parameters import Button, Color
from pybricks.ev3devices import *
import threading
from time import sleep


def coder():
    number = 0
    while (number < 20):
        number += 1
        print('Coders: ' +str(number))

def func1():
    print('Function 1 started')
    sleep(10)
    print('Function 1 done')
    brick.display.clear()
    brick.display.text('Function 1 done', (50, 50))

def func2():
    sleep(5)
    print("Function 2 done")
    brick.display.clear()
    brick.display.text('Function 2 done', (50, 50))

def myfunc():
    print('myfunction done')
    brick.display.clear()
    brick.display.text('myfunction done', (50, 50))

def threadstarter():
    print('Threads starting')
    brick.display.clear()
    brick.display.text('Threads starting', (50, 50))

func2thread = threading.Thread(target = func2)
func1thread = threading.Thread(target = func1)
myfuncthread = threading.Thread(target = myfunc)
coderthread = threading.Thread(target = coder)

threadstarter()
coderthread.start()
func2thread.start()
myfuncthread.start()
func1thread.start()