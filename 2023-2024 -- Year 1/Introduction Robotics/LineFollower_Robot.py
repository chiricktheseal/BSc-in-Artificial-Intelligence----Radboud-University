#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:26:36 2024

@author: maria
"""

from hub import hardware_id, light_matrix, port
import color_sensor
import color
import motor
import runloop

# the threshold is set to 40% of the light that is reflected from the color_sensor (the light reflected when half is white, half is black)
threshold = 60

# The error_list contains all errors. This is needed in the derivative and integral part of the PID controller
error_list = []

# The default speed is the speed at whhich the motors run when there is equal amount of black and white detected (reflection at 40%)
default_speed = 200

# Kp, Kd and Ki are the three constants used in the PID controller: Kp used in P_Controller(), Kd used in D_Controller(), Ki used in I_Controller()
Kp = 5
Kd = 7
Ki = 0.005

def follow_line():
    '''
    Function that corrects the motors of a robot so that the robot is following a line
    In this function the reflection detected by a color sensor is used to determine the error that is than given to a PID controller.
    Based on the resulting error from the PID controller, the motor speed is changed.
    '''
    global threshold
    global error_list
    global default_speed

    #print("0")
    reflection = color_sensor.reflection(port.C)
    #print("a")
    error = threshold - reflection
    #print(error)
    error_list.append(error)
    #print("b")

    correction = PID_Controller(error_list)
    #print("c")

    speed_leftMotor = default_speed - correction
    speed_rightMotor = default_speed + correction
    #print("d")
    #print(speed_leftMotor, speed_rightMotor)

    motor.run(port.F, int(-speed_leftMotor))
    motor.run(port.B, int(speed_rightMotor))
    #print("e")


def P_Controller(error_list):
    '''
    Calculates the proportional error of a PID controller.

    Parameters :
        error_list (list): list of all errors that were previously calculated

    Return :
        the proportional error based on the last element of error_list
    '''
    return Kp * error_list[-1]

def I_Controller(error_list):
    '''
    Calculates the integral error of a PID controller.

    Parameters :
        error_list (list): list of all errors that were previously calculated

    Return :
        the integral error based on the summation of errors in error_list 
    '''
    return sum(error_list) * Ki

def D_Controller(error_list):
    '''
    Calculates the derivative error of a PID controller.

    Parameters :
        error_list (list): list of all errors that were previously calculated

    Return :
        the derivative error based on last two errors in error_list 
    '''
    if (len(error_list) >= 2):
        return (error_list[-1] - error_list[-2]) * Kd
    else:
        return 0

def PID_Controller(error_list):
    '''
    Calculates the error of a PID controller.
    The error consists of an integral, a proportional and a derivative part that are all summed together

    Parameters :
        error_list (list): list of all errors that were previously calculated

    Return :
        the sum of the integral, proportional and derivative errors
    '''
    return P_Controller(error_list) + I_Controller(error_list) + D_Controller(error_list)


def main():
    '''
    Main function that is called at the start of the program.
    It calls the follow_line() function in a loop
    '''
    motor.run(port.B, 20)
    motor.run(port.F, 20)
    while (True):
        #print("loop")
        follow_line()

main()
 
#runloop.run(main())
