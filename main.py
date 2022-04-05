from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

PORT_A = "A" # left light sensor
PORT_B = "B" # right light sensor
PORT_C = "C" # left motor
PORT_D = "D" # right motor
#PORT_F - big motor

hub = PrimeHub()
right_motor = Motor(PORT_D)
left_motor = Motor(PORT_C)

def move_forward(speed: int):
    right_motor.start(speed)
    left_motor.start(-speed)

def move_backward(speed: int):
    right_motor.start(-speed)
    left_motor.start(speed)

def turn_right(speed: int, degrees: int):
    stop()
    hub.motion_sensor.reset_yaw_angle()
    left_motor.start(-speed)
    while True:
        turn_angle = hub.motion_sensor.get_yaw_angle()
        if turn_angle > degrees or turn_angle < 0:
            stop()
            break

def turn_left(speed: int, degrees: int):
    stop()
    hub.motion_sensor.reset_yaw_angle()
    right_motor.start(speed)
    while True:
        turn_angle = hub.motion_sensor.get_yaw_angle()
        if turn_angle < -degrees or turn_angle > 0:
            stop()
            break

def stop():
    right_motor.stop()
    left_motor.stop()

def main():
    while True:
        if hub.right_button.was_pressed():
            turn_left(50, 179)
            

main()
