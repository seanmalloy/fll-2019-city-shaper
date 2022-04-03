from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

PORT_A = "A" # left light sensor
PORT_B = "B" # right light sensor
PORT_C = "C" # left motor
PORT_D = "D" # right motor
# PORT F - big motor with small gear

hub = PrimeHub()
right_motor = Motor(PORT_D)
left_motor = Motor(PORT_C)

def main():
    while True:
        if hub.right_button.was_pressed():
            # TODO: create a move forward function
            # TODO: crate a move backware function
            right_motor.start(50)
            left_motor.start(-50)


main()
