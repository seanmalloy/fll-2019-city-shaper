from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

PORT_A = "A" # left light sensor
PORT_B = "B" # right light sensor
PORT_C = "C" # left motor
PORT_D = "D" # right motor
#PORT_F - big motor

hub = PrimeHub()
motor_pair = MotorPair(PORT_C, PORT_D) 
right_motor = Motor(PORT_D)
left_motor = Motor(PORT_C)

def move_forward(distance: float, speed: int):
    motor_pair.move(distance, "in", 0, speed) # TODO: don't hard code these parameters

def move_backward(distance: float, speed: int):
    #right_motor.start(-speed)
    #left_motor.start(speed)
    motor_pair.move(distance, "in", 0, -speed) # TODO: don't hard code these parameters

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
    motor_percent_speed = 50
    while True:
        if hub.right_button.was_pressed():
            # Push red house into red circle and return
            move_forward(25, motor_percent_speed)
            move_backward(25, motor_percent_speed)
        if hub.left_button.was_pressed():
            # Climb the bridge
            move_forward(41, motor_percent_speed)
            turn_left(motor_percent_speed, 115)
            move_forward(28, motor_percent_speed)
            

main()
