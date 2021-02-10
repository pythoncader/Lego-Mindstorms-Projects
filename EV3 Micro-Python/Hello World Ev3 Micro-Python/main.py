#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import print, wait
from pybricks.parameters import Button, Color

while True:
    print("Hello World!")

    brick.display.clear()

    brick.display.text("Hello", (50, 50))
    wait(1000)
    brick.display.text("World!")

    print(str(brick.battery.voltage()/1000) + " volts")
    print(str(brick.battery.current()/1000) + " amps")

    if(brick.battery.voltage() < 5000):
        print("Battery low")
        brick.display.clear()
        brick.display.text("Battery", (50, 50))
        wait(1000)
        brick.display.text("  Low")
        wait(2000)
        brick.display.clear()
        brick.display.text("Exiting Program...", (20, 50))
        wait(1000)
        break
    brick.light(Color.RED)
    # Play a sound.
    brick.sound.beep()
    # Initialize a motor at port B.
    test_motor = Motor(Port.B)
    # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
    test_motor.run_target(1, 360*10)
    # Play another beep sound.
    # This time with a higher pitch (1000 Hz) and longer duration (500 ms).
    brick.sound.beep(1000, 500)

    if Button.LEFT in brick.buttons():
        print("The left button is pressed.")

    while not any (brick.buttons()):
        wait(10)
        brick.sound.beep(1, 200)
        brick.light(Color.ORANGE)

    while any (brick.buttons()):
        wait(10)
        brick.sound.beep(2000, 200)
        brick.light(Color.GREEN)

    brick.light(Color.BLACK)
    wait(100)
    print(str(test_motor.angle()))
    test_motor.reset_angle(0)
    print(str(test_motor.angle()))
    break
