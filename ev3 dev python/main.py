#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

# TODO: Add code here
ts = TouchSensor(INPUT_1)
leds = Leds()
m = LargeMotor(OUTPUT_A)

print("Press the touch sensor to change the LED color!")

while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
        m.on_for_rotations(SpeedPercent(75), 5)
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")